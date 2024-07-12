import argparse
from dsmr_parser import telegram_specifications
from dsmr_parser.clients import AsyncSerialReader, SERIAL_SETTINGS_V5
import influxdb_client
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from aiohttp.client_exceptions import ClientConnectorError

from loguru import logger
import json
import asyncio


async def parse_telegram_influx(name, queue: asyncio.Queue, config_file: str):
    while True:
        telegram = await queue.get()

        logger.info("Parsing telegram")
        parsed_telegram = json.loads(telegram.to_json())
        logger.info("Data to write:")
        p_elect = (
            influxdb_client.Point("electricity")
            .tag("unit", "kWh")
            .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"])
        )
        for key in [
            "ELECTRICITY_USED_TARIFF_1",
            "ELECTRICITY_USED_TARIFF_2",
            "ELECTRICITY_DELIVERED_TARIFF_1",
            "ELECTRICITY_DELIVERED_TARIFF_2",
        ]:
            if key not in parsed_telegram:
                logger.error("Key not in telegram")
                continue
            if parsed_telegram[key]["unit"] != "kWh":
                logger.error("Unit is not kWh")
                continue
            p_elect.field(key.lower(), parsed_telegram[key]["value"])
        p_elect.time(parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"])

        p_elect_flow = (
            influxdb_client.Point("electricity_current")
            .tag("unit", "kW")
            .tag("actief_tarief", parsed_telegram["ELECTRICITY_ACTIVE_TARIFF"]["value"])
            .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"])
        )
        for key in [
            "CURRENT_ELECTRICITY_USAGE",
            "CURRENT_ELECTRICITY_DELIVERY",
            "INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE",
            "INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE",
            "INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE",
            "INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE",
            "INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE",
            "INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE",
        ]:
            if key not in parsed_telegram:
                logger.error("Key not in telegram")
                continue
            if parsed_telegram[key]["unit"] != "kW":
                logger.error("Unit is not kW")
                continue
            p_elect_flow.field(key.lower(), parsed_telegram[key]["value"])
        p_elect_flow.time(parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"])

        p_voltage = (
            influxdb_client.Point("voltage")
            .tag("unit", "V")
            .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"])
        )
        for key in [
            "INSTANTANEOUS_VOLTAGE_L1",
            "INSTANTANEOUS_VOLTAGE_L2",
            "INSTANTANEOUS_VOLTAGE_L3",
        ]:
            if key not in parsed_telegram:
                logger.error("Key not in telegram")
                continue
            if parsed_telegram[key]["unit"] != "V":
                logger.error("Unit is not V")
                continue
            p_voltage.field(key.lower(), parsed_telegram[key]["value"])
        p_voltage.time(parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"])

        p_current = (
            influxdb_client.Point("current")
            .tag("unit", "A")
            .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"])
        )

        for key in [
            "INSTANTANEOUS_CURRENT_L1",
            "INSTANTANEOUS_CURRENT_L2",
            "INSTANTANEOUS_CURRENT_L3",
        ]:
            if key not in parsed_telegram:
                logger.error("Key not in telegram")
                continue
            if parsed_telegram[key]["unit"] != "A":
                logger.error("Unit is not A")
                continue
            p_current.field(key.lower(), parsed_telegram[key]["value"])
        p_current.time(parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"])

        p_gas = (
            influxdb_client.Point("gas")
            .tag("unit", "m3")
            .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER_GAS"]["value"])
        )
        if "HOURLY_GAS_METER_READING" in parsed_telegram:
            p_gas.field("hourly", parsed_telegram["HOURLY_GAS_METER_READING"]["value"]).time(
                parsed_telegram["HOURLY_GAS_METER_READING"]["datetime"]
            )

        logger.debug("Energy: " + str(p_elect.to_line_protocol()))
        logger.debug("Flow: " + str(p_elect_flow.to_line_protocol()))
        logger.debug("Voltage: " + str(p_voltage.to_line_protocol()))
        logger.debug("Current: " + str(p_current.to_line_protocol()))
        logger.debug("Gas: " + str(p_gas.to_line_protocol()))
        info_list = [
            ("latest_energy", p_elect),
            ("latest_energy_current", p_elect_flow),
            ("latest_voltage_current", p_voltage),
            ("latest_voltage_current", p_current),
            ("latest_gas", p_gas),
        ]
        logger.info("Opening InfluxDBClient")
        async with InfluxDBClientAsync.from_config_file(config_file) as client:
            logger.info("Writing to influxdb")
            write_api = client.write_api()
            writetasks = []
            for item in info_list:
                writetasks.append(write_api.write(bucket=item[0], record=item[1]))

            results = await asyncio.gather(*writetasks, return_exceptions=True)
            for bucket_info, result in enumerate(zip(info_list, results)):
                if isinstance(result, ClientConnectorError):
                    logger.error(f"Error connecting to influxdb: {result}")
                    raise result
                elif isinstance(result, Exception):
                    logger.error(f"Error writing to bucket {bucket_info[0]}: {result.with_traceback()}")
                    raise result
                else:
                    logger.info(f"Writing to bucket {result[0][0]} succeeded")
        queue.task_done()


async def main(config_file="./p1_influx_db/config.toml"):
    queue = asyncio.Queue()
    logger.info("Opening SerialReader")
    serial_reader = AsyncSerialReader(
        device="/dev/serial0",
        serial_settings=SERIAL_SETTINGS_V5,
        telegram_specification=telegram_specifications.V5,
    )
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(parse_telegram_influx(f"worker-{i}", queue, config_file=config_file)))

    await serial_reader.read_as_object(queue)
    result = await asyncio.gather(*tasks, return_exceptions=True)
    for r in result:
        if isinstance(r, ClientConnectorError):
            raise r
        elif isinstance(r, Exception):
            raise r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="config file", default="./config.toml")
    args = parser.parse_args()

    asyncio.run(main(args.config))
