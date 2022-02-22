import datetime
t = int(input("Enter time in seconds :"))
conversion = datetime.timedelta(seconds=t)
converted_time = str(conversion)
print(converted_time)