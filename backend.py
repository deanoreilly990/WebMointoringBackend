#Backend processing for the mointoring tool
# Required backend packages -

import psutil


def alert():
    #This function is used to send instant notifications to the endpoint selected.
    #The details for this endpoint are configured in the UserConsole.
    # The data is stored in a local encypted file.dd
    from twilobackend import sendEmergencyMessage
    EmergencyMesage = 'Emegency in place. CPU hitting treshold.'
    sendEmergencyMessage(EmergencyMesage)


def returnSampleData():
    # Used to return sample data to front end to
    from controller import logger_Global
    logger = logger_Global()
    data = {}
    data['SUN'] = '0.1'
    data['MON'] = '0.3'
    data['TUE'] = '0.8'
    data['WED'] = '0.4'
    data['THU'] = '0.7'
    data['FRI'] = '0.8'
    data['SAT'] = '0.9'
    logger.info(data)
    return data


def getLocalCPUlevels():
    # CPU data returned in JSON
    # Memory Stats in MB
    from controller import logger_Global
    logger = logger_Global()
    data={}
    MemoryUsage=psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024
    CPUAvail = MemoryUsage.available >> 20
    CPUTotal = MemoryUsage.total >>10
    CPUused = MemoryUsage.used >>20
    if MemoryUsage.available <= THRESHOLD:
        alert()
        data['CPU Available'] = CPUAvail
        data['CPU Total'] = CPUTotal
        data['CPU Used'] = CPUused
        data ['CPU Message'] = 'FAIL'
        logger.debug(data)
        alert()
        return data
    else:
        data['CPU Available'] = CPUAvail
        data['CPU Total'] = CPUTotal
        data['CPU Used'] = CPUused
        data['CPU Message'] = 'OK'
        logger.debug(data)
        data = returnSampleData()  # Sample Data - Remove if needed
        return data
def getApacheLogs():
    return 'OK'