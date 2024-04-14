import os

def setdir(new_path):
    os.chdir(new_path)

def getdir():
    return os.getcwd()
