# Python Packages

import os
import logging
import json
from dateutil.parser import parse


# PyPi packages

import pendulum

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)
fmt = logging.Formatter("%(asctime)s %(funcName)s %(levelname)s %(message)s")
ch = logging.StreamHandler()
fh = logging.FileHandler('thelog.log')
ch.setFormatter(fmt)
fh.setFormatter(fmt)
logger.addHandler(fh)
logger.addHandler(ch)

"""Logging Levels = https://docs.python.org/3/howto/logging.html"""

# These below se up cross-platform filepaths

appDir = os.path.abspath((os.path.dirname(__file__)))
users = os.path.join(appDir, 'users')
stories = os.path.join(appDir, 'storymeta')

tz = pendulum.timezone('US/Pacific') # Original data was scraped on the west coast of the USA. This will be used to make sure any datetime string will be properly converted to epoch

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

for filename in os.listdir(users):
    path = os.path.abspath(os.path.join(users, filename))
    with open(path) as f:
        data = json.load(f)
        for i in data:
            print(data[i])
        print(data)
        userID = data['User ID']
        storiesWritten = data['Stories']
        print("User ID is {}, Data was Scraped at None, The Stories they wrote was {}".format(userID, storiesWritten))