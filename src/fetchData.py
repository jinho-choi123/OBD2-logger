import obd
import time
import logging

def fetchELM_VOLTAGE(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.ELM_VOLTAGE, callback=lambda r: dataLogger.info(f'timestamp {r.time} | ELM_VOLTAGE {r.value}'))

def fetchDTC(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.GET_DTC, callback=lambda r: dataLogger.info(f'timestamp {r.time} | DTC {r.value}'))

def fetchRPM(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.RPM, callback=lambda r:dataLogger.info(f'timestamp {r.time} | RPM {r.value}'))

def fetchFUEL_STATUS(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.FUEL_STATUS, callback=lambda r:dataLogger.info(f'timestamp {r.time} | FUEL_STATUS {r.value}'))

def fetchENGINE_LOAD(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.ENGINE_LOAD, callback=lambda r:dataLogger.info(f'timestamp {r.time} | ENGINE_LOAD {r.value}'))

def fetchCOOLANT_TEMP(dataLogger: logging.Logger, conn: obd.Async):
    conn.watch(obd.commands.COOLANT_TEMP, callback=lambda r:dataLogger.info(f'timestamp {r.time} | COOLANT_TEMP {r.value}'))

def fetchAll(dataLogger: logging.Logger):
    OBD_CONNECT_STRING = '/dev/pts/21'
    connection = obd.Async(fast=False, timeout=30, portstr=OBD_CONNECT_STRING, baudrate=115200)
    fetchDTC(dataLogger, connection)
    fetchRPM(dataLogger, connection)
    fetchELM_VOLTAGE(dataLogger, connection)
    fetchFUEL_STATUS(dataLogger, connection)
    fetchENGINE_LOAD(dataLogger, connection)
    fetchCOOLANT_TEMP(dataLogger, connection)

    connection.start()
    time.sleep(60 * 5)
    connection.stop()

