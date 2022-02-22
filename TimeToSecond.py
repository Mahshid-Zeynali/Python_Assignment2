from posixpath import split


t = input()
time = t.split(":")
second = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
print("time to second is :" , second)
