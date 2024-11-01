import datetime

now = datetime.datetime.now()
print(now)

day1 = now.strftime("%Y-%m-%d")
print(day1)
day2 = now.strftime("%H:%H:%S")
print(day2)