import pytz
import datetime

# Wrong
str_time = '2022-11-04 12:19:31.507025-04:00'
test_obj = datetime.datetime.fromisoformat(str_time)
tz = pytz.timezone('America/New_York')
datetime_obj = datetime.datetime(2022, 11, 4, 12, 19, 31, 0,   tz)
print(test_obj < datetime_obj)

# Correct
str_time = '2022-11-04 12:19:31.507025-04:00'
test_obj = datetime.datetime.fromisoformat(str_time)
tz = pytz.timezone('America/New_York')
datetime_obj = tz.localize(datetime.datetime(2022, 11, 4, 12, 19, 31, 0))
print(test_obj < datetime_obj)
