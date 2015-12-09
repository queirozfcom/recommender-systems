from datetime import datetime

def get_day_of_week_from_timestamp(timestamp):
	date = datetime.fromtimestamp(int(timestamp))
	return(date.weekday())

