import datetime

if __name__ == '__main__':
    time_diff = datetime.timedelta(hours=1)
    print(datetime.datetime.now() - time_diff)
    print(datetime.datetime.now())
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

