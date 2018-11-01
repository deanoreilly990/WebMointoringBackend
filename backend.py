#Backend processing for the mointoring tool
#Required backend packages
from __future__ import print_function
import psutil
import os


def getLocalCPUlevels():

    print (psutil.__version__)
    print(psutil.cpu_percent(interval=None))
    MemoryUsage=psutil.virtual_memory()
    print(MemoryUsage)
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 30  # memory use in GB...I think
    print('memory use:', memoryUse)
    THRESHOLD = 100 * 1024 * 1024
    CPUusage = MemoryUsage.available >> 30
    CPUTotal = MemoryUsage.total >>30
    CPUused = MemoryUsage.used >>30

    if MemoryUsage.available <= THRESHOLD:
        print ('Warning Treshold Met')
    else:
        print('Memory Usage Free :',CPUusage, 'GB')
        print('Memery Total:',CPUTotal)
        print('Memory Used',CPUused)



getLocalCPUlevels()