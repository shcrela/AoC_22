import os
import sys
import requests
import numpy as np

def get_data(day):
    """Once you're logged in to AoC website,
    you can find your session ID in the cookie
    (In the browser, Press F12 -> Application).
    I then stored mine in environment variable
    called `AOC22_SESSIONID`."""
    
    SESSIONID = os.environ.get("AOC22_SESSIONID")
    uri = f'http://adventofcode.com/2022/day/{day}/input'
    response = requests.get(uri, cookies={'session': SESSIONID})
    return response.content.decode().strip()

day = int(sys.argv[1])

data = get_data(day)
lines = data.split("\n")