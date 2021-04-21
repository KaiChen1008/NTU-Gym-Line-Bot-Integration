import os, requests, schedule, time, datetime, pytz, csv, json

class Logger():
    def __init__(self, log_name='default.csv', header=None):
        assert header != None, 'please specify the header'

        self.log    = log_name
        self.header = header
        self.reset()
    
    def reset(self):
        with open(self.log, 'w') as f:
            logwriter = csv.writer(f, delimiter=',')
            logwriter.writerow(self.header)

    def update(self, data):
        with open(self.log, 'a') as f:
            logwriter = csv.writer(f, delimiter=',')
            logwriter.writerow(data)


def get_gym_capacity():
    url = 'https://ntusportscenter.ntu.edu.tw/counter.txt'
    r   = requests.get(url)
    if r.status_code == requests.codes.ok:
        r = json.loads(r.text)
        capacity = r['CounterData'][0]['innerCount'].split(';')[0]
        return capacity

def get_time(time_zone):
    return datetime.datetime.now().replace(tzinfo=time_zone).strftime("%m:%d:%w:%H:%M")

