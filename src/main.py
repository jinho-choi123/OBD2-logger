import obd 
import logging

def log_rpm(r):
    print(f'timestamp {r.time} | RPM {r.value}')


if __name__ == "__main__":
    # LOG CONFIG
    obd.logger.setLevel(obd.logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    obd.logger.addHandler(stream_handler)

    # LOG FILE SAVE CONFIG
    file_handler = logging.FileHandler("log/data.log")
    file_handler.setFormatter(formatter)
    obd.logger.addHandler(file_handler)

    # FIXME when running Emulator
    OBD_CONNECT_STRING = '/dev/ttys010'

    # FIXME 
    # Debug mode... Remove at Production

    # Make connection to OBD2 system
    connection = obd.OBD(fast=False, timeout=30, portstr="/dev/ttys010", baudrate=115200)

    obd.logger.critical("OBD CONNECTION ESTABLISHED...")
    # query a command
    r = connection.query(obd.commands.RPM)
    if not r.is_null():
        obd.logger.info(f"timestamp {r.time} | {r.value}")

    connection.close()
    obd.logger.critical("OBD CONNECTION CLOSED...")



