import os
import math, datetime, sys

working_director = os.getcwd()

def return_user_id():
    print(os.getuid())

def return_user_name():
    print(os.uname())

def operating_system_information():
    print(os.cpu_count())

print(datetime.date.today())

print(sys.path)
