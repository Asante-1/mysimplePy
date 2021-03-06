import datetime
tday = datetime.date.today()
tdelta = datetime.timedelta(7)

print(tday + tdelta)
bday = datetime.date(2020, 7, 21)

till_bday = bday - tday
#print(till_bday)
