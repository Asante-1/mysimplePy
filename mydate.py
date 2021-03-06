

# gvr = datetime.date(2000, 7, 21)
# now = datetime.time(4, 56, 00)
#
# kumi = "07/21/2010"
#
# print(gvr.strftime("%A, %B, %d, %Y"))
# moon_landing = datetime.datetime.strptime(kumi, "%m/%d/%Y")
# print(moon_landing)
# print(now)

from datetime import datetime, timedelta

now = datetime.now()
print(now)

then = datetime(2016, 5, 23)
delta  = now-then
print(delta.days)

print(delta.seconds)




