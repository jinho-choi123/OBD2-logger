import obd 
import logging
import time
from fetchData import fetchAll

def log_rpm(r):
    print(f'timestamp {r.time} | RPM {r.value}')


if __name__ == "__main__":
    # LOG CONFIG
    # obd.logger.setLevel(obd.logging.DEBUG)
    DATALogger = logging.getLogger("data")
    DATALogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    obd.logger.addHandler(stream_handler)
    DATALogger.addHandler(stream_handler)

    # LOG FILE SAVE CONFIG
    debug_file_handler = logging.FileHandler("log/obd-runtime.log")
    debug_file_handler.setFormatter(formatter)
    obd.logger.addHandler(debug_file_handler)

    data_file_handler = logging.FileHandler("log/obd-data.log")
    data_file_handler.setFormatter(formatter)
    DATALogger.addHandler(data_file_handler)

    # FIXME 
    # Debug mode... Remove at Production

    # fetch all
    fetchAll(DATALogger)
    



