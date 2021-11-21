import os 
import datetime 
from plyer import notification
import time

os.system('CLS')
alarm_Hour = int(input("Hour\n-"))
alarm_Min = int(input("Minute\n-"))
alarm_AmOrPm = str(input("AM or PM\n-"))
time.sleep(1)
print("You have set the alarm for", alarm_Hour,":",alarm_Min,alarm_AmOrPm.upper())
time.sleep(0.5)
print("Waitng for alarm to ring!")
time.sleep(1)
print("You will be notified by the desktop notifier about the alarm.")

if (alarm_AmOrPm.upper() == "PM"):
    alarm_Hour = alarm_Hour + 12

while True:
    if (alarm_Hour == datetime.datetime.now().hour and alarm_Min == datetime.datetime.now().minute):
        notification.notify(title = 'ALARM', message = 'MESSAGE HERE', timeout = 10)
        break
