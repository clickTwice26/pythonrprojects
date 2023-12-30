import os
from json import loads, load, dumps, dump
from datetime import datetime
currentWorkingDirectory = os.getcwd()
project_configuration = load(open(f"{currentWorkingDirectory}/project_config.json", "r"))


print(project_configuration)



