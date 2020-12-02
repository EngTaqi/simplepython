#to import a module in python
#to delay the show of a file
import sys
sys.builtin_module_names #to git the build in modules
import time
time.sleep(5) #lag time 5 sec
while True:
    with open("fruits.txt") as file:
        file.read()
        time.sleep(2)
#if my file dosenot exist but i want to keep running
import os
os.path.exists("fruits") #gives ture
while True:
    time.sleep(2)
    if os.path.exists("fruits"):
    with open("fruits.txt") as file:
        file.read()
        time.sleep(2)
    else:
        print("file doesnot exist")
import pandas