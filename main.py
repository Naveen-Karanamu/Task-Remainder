# Modules
import time

# Welcome
name=input("Hello user! please enter you name 🙃 ")
print ("*"*20,"WELCOME TO THE TASK REMAINDER 😌","*"*20)

task=input(f"{name} please enter the task that you should be remainded off! ")

def repeats_func():
    repeats=input("Please Enter the number of times you want us to remaind your task ")
    if(repeats.isnumeric()):
        return repeats
    else:
        print("Invalid input ⚠️ Please Enter a valid input!")
        repeats_func()
    
times=int(repeats_func())

print("Tell us the unit of time after which you want to be remainded about the task ")

def unit_func():
    unit=input("Type 'S' for seconds, 'M' for minutes and 'H' for hours ").upper()
    if(unit=='S' or unit=='M' or unit =='H'):
        pass
    else:
        print("Please Check your Time unit selection and enter again ⚠️")
        unit_func()

    t=int(input("Enter the Time for your selected unit to Soonze your alert 😉 "))

    if(unit=='S'):
        soonze=t
        return soonze
    elif(unit=='M'):
        soonze=60*t
        return soonze
    elif(unit=='H'):
        soonze=60*60*t
        return soonze
    else:
        print("⚠️ Enter a valid time period Unit")
        unit_func()
soonze=unit_func()

while (times>0):
    time.sleep(soonze)
    print(f"{name} !!!, it's time to {task}")
    times-=1