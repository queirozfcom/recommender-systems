from datetime import datetime

def day_of_week_from_timestamp(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return(date.weekday())

def day_of_month_from_timestamp(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return(date.day)

def am_pm_from_timestamp(timestamp):
    date = datetime.fromtimestamp(int(timestamp))

    if date.hour < 12:
        return(0)
    else:
        return(1)    


