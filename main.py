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
t=input("Type 'S' for seconds, 'M' for minutes and 'H' for hours ")



while (times>0):
    time.sleep(3)
    print(f"{name} !!!, it's time to {task}")
    times-=1