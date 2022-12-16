def add_time(start, duration, day=False):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  hours = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"]
  days_past = 0
  new_day = ""

#split out input arguments into variables
  start_split = start.split()
  AM_PM_start = start_split[1]
  start_time_split = (start_split[0]).split(':')
  start_hrs = int(start_time_split[0])
  start_mins = int(start_time_split[1])
  dur_split = duration.split(':')
  dur_hrs = int(dur_split[0])
  dur_mins = int(dur_split[1])
  if day:
    start_day = day.lower().capitalize()

#calculations
  new_mins = str((start_mins + dur_mins) % 60)
  if len(new_mins) == 1:
    new_mins = '0' + new_mins
  add_hrs = ((start_mins + dur_mins) // 60) + dur_hrs
  start_hrs_index = hours.index(start_time_split[0] + ' ' + AM_PM_start)
  new_hrs_index = start_hrs_index + add_hrs
  if new_hrs_index > 23:
    while new_hrs_index > 23:
      days_past += 1
      new_hrs_index -= 24

  if day:
    new_day_index = (days.index(start_day) + days_past) % 7
    new_day = days[new_day_index]

  new_hrs_split = hours[new_hrs_index].split()
  new_hrs = new_hrs_split[0]
  AM_PM_new = new_hrs_split[1]
  new_time = new_hrs + ':' + str(new_mins) + ' ' + AM_PM_new

  if days_past != 0:
    days_later = 'next day' if days_past == 1 else f"{days_past}{' days later'}"
    return (f"{new_time}{' ('}{days_later}{')'}" if day == False else f"{new_time}{', '}{new_day}{' ('}{days_later}{')'}")
  else:
    return new_time if day == False else f"{new_time}{', '}{new_day}"
