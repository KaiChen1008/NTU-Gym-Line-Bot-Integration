import os, requests, schedule, time, datetime, pytz, csv, json
from modules.utils import *

LOG_NAME = 'capacity.csv'
PERIOD   = 10
TW       = pytz.timezone('Asia/Taipei')
logger   = Logger(log_name=LOG_NAME, header=['time', 'capacity'])

def log_capacity():
    curr     = get_time(time_zone=TW)
    capacity = get_gym_capacity()
    logger.update([curr, capacity])


if __name__ == '__main__':
    schedule.every(PERIOD).minutes.do(log_capacity)
    # schedule.every(3).secognds.do(log_capacity)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
