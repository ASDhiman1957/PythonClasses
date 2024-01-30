# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime

# this program is made my Amitoj Singh
# import time 
# currenthour = time.strftime('%H')
# print(currenthour)
# if(currenthour<=18 and  currenthour==18):
#     print("good morning")
# elif(currenthour<18):
#     print("good afternoon")
# else:
#     print("good evening")


import datetime

current_hour = datetime.datetime.now().hour
print(current_hour)

if current_hour <= 18 and current_hour == 18:
    print("good morning")
elif current_hour < 18:
    print("good afternoon")
else:
    print("good evening")


 