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
    dataToReturn = {}
    dataToReturn['CPU'] = data
    dataToReturn['Health'] = 'Healthy'
    CPUdata = {}
    total = 4000
    used = 2053
    unused = total - 2053
    CPUdata['Used MB'] = used
    CPUdata['UnUsed MB'] = unused

    dataToReturn['CPUcurrent'] = CPUdata
    logger.info(dataToReturn)
    return dataToReturn


def getLocalCPUlevels():
    """CPU data returned in JSON
    # Memory Stats in MB """

    from controller import logger_Global
    logger = logger_Global()
    data={}
    MemoryUsage=psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024
    CPUAvail = MemoryUsage.available >> 20
    CPUTotal = MemoryUsage.total >>20
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
        #data = returnSampleData()  # Sample Data - Remove if needed
        return data


def return_root_log():
    """function to return the alias of logged in users"""
    from controller import logger_Global
    logger = logger_Global()
    import subprocess
    logged_in_users = subprocess.check_output("who").splitlines()
    logger.info(logged_in_users)
    data_to_return = {}
    data = []
    for i in logged_in_users:
        a = []
        for word in i.split():
            a.append(word)
        data.append(a)
    print data
    users = []
    locations = []
    times = []
    for i in data:
        users.append(i[0])
        locations.append(i[1])
        times.append(i[4])
    data_to_return['USERS'] = users
    data_to_return['LOCATIONS'] = locations
    data_to_return['TIMES'] = times

    logger.info(data_to_return)
    return data_to_return

def getApacheLogs():
    return 'OK'