# April 12, 2016

def next_day(day):
  ans = {
    'mon':'tue',
    'tue':'wed',
    'wed':'thu',
    'thu':'fri',
    'fri':'sat',
    'sat':'sun',
    'sun':'mon'
  }

  return ans[day]

def first_days_of_month(year):
  days_in_month = [
    ['jan',31]
    , ['feb',28]
    , ['mar',31]
    , ['apr',30]
    , ['may',31]
    , ['jun',30]
    , ['jul',31]
    , ['aug',31]
    , ['sep',30]
    , ['oct',31]
    , ['nov',30]
    , ['dec',31]
    ]

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        days_in_month[1][1] = 29
    else:
      days_in_month[1][1] = 29

  first_days = [1]
  for month in days_in_month[:-1]:
    first_days.append(first_days[-1]+month[1])

  num_days = sum([x[1] for x in days_in_month])

  return first_days, num_days

day = 'tue'
year = 1901
count_sunday = 0

while year <= 2000:
  first_days, days_in_year = first_days_of_month(year)

  for d in range(1,days_in_year+1):
    if d in first_days and day == 'sun':
      count_sunday += 1
    day = next_day(day)
  year += 1

print count_sunday
