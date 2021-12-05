import os 
import datetime 
from plyer import notification
import time
import pyttsx3

def voice(msg):
    var = pyttsx3.init()
    var.say(msg)
    var.runAndWait()


os.system('CLS')
alarm_Hour = int(input("Hour\n-"))
alarm_Min = int(input("Minute\n-"))
alarm_AmOrPm = str(input("AM or PM\n-"))
get_message = str(input("What do you want your message to be? \n-"))
time.sleep(1)
print("\nYou have set the alarm for", alarm_Hour,":",alarm_Min,alarm_AmOrPm.upper())
time.sleep(0.5)
print("="*45)
print("\nWaitng for alarm to ring!")
time.sleep(1)
print("="*45)
print("You will be notified by the desktop notifier about the alarm and you should be hearing a voice message.")

if (alarm_AmOrPm.upper() == "PM"):
    alarm_Hour = alarm_Hour + 12

while True:
    if (alarm_Hour == datetime.datetime.now().hour and alarm_Min == datetime.datetime.now().minute):
        notification.notify(title = 'ALARM', message = (get_message), timeout = 10)
        voice(get_message)
        break
