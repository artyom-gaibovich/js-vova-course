import datetime

start_date = 1739124540

current_date = 1739297240

interval = 86400


def timestamp_converter(timestamp):
  datetime_obj = datetime.datetime.fromtimestamp(timestamp)
  time_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
  return time_str

 days_start_to_current = (current_date - start_date) // interval
 day_before = start_date + days_start_to_current * interval
 next_day = start_date + (days_start_to_current + 1) * interval
 print(day_before, next_day)

 formatted_day_before = timestamp_converter(day_before)
 formatted_next_day = timestamp_converter(next_day)


 def fullfilled:
     if (current_date >= date_to_update):
        next_day = next_day + interval
     if (is_fullfilled):
        is_fullfilled= False
     if (not(is_fullfilled)):
        date_to_update = next_day
        is_fullfilled= "Fail"
     if (is_fullfilled):
        date_to_update = next_day
        is_fullfilled= True
