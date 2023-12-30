import os
from json import loads, load, dumps, dump
from datetime import datetime


def currentime(wdm="both"):
    now = datetime.now()
    if wdm == "date":
        return str(now).split(" ")[0]
    if wdm == "time":
        return str(now).split(" ")[1].split(".")[0]
    elif wdm == "both":
        return now


currentWorkingDirectory = os.getcwd()
project_configuration = load(open(f"{currentWorkingDirectory}/project_config.json", "r"))

print(project_configuration)
print(currentime("time"))
