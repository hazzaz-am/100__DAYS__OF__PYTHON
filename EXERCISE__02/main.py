import time

time_stamp_str = time.strftime("%H")
time_stamp = int(time_stamp_str)


if (time_stamp < 12):
  print("Good Morning")
elif (time_stamp < 14):
  print("Good Afternoon")
elif (time_stamp < 18):
  print("Good Evening")
else: 
  print("Good Night")