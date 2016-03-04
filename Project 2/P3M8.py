#!/usr/bin/env python
import os
# need to use os.system to issue commands, takes in as string
day = 1
os.system("cd Desktop/cuckoo") #placing the terminal in the right place
#need to call every day in march at 2pm
while day <= 31:
    os.system('python ./utils/submit.py ­­platform windows ­­machine WindowsXPSP3 ­­timeout 180 --clock "03-'+str(day)+'-2016 14:00:00" ../malware/PhaseIII/malware8.exe'')
    day = day +1 
#create loop that runs through every day