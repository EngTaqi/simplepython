#to import a module in python
#to delay the show of a file
import sys
sys.builtin_module_names #to git the build in modules
import time
time.sleep(5) #lag time 5 sec
while True:
    with open("fruits.txt") as file:
        file.read()
        time.sleep(10)
