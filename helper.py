import os
import sys
import requests
import numpy as np

def get_data(day):
    SESSIONID = os.environ.get("AOC22_SESSIONID")
    uri = f'http://adventofcode.com/2022/day/{day}/input'
    response = requests.get(uri, cookies={'session': SESSIONID})
    return response.content.decode().strip()

day = int(sys.argv[1])

data = get_data(day)
lines = data.split("\n")