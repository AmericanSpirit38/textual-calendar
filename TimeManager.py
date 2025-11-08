import datetime

def TodayDate():
    now = datetime.date.today()
    x = str(now).split("-")[::-1]
    x[2] = x[2][2:]
    s = x[0] + "-" + x[1] + "-" + x[2]
    return s
def TommorowDate():
    now = datetime.date.today() + datetime.timedelta(days=1)
    x = str(now).split("-")[::-1]
    x[2] = x[2][2:]
    s = x[0] + "-" + x[1] + "-" + x[2]
    return s
def ThisWeekDate():
    now = datetime.date.today()
    weekday = now.weekday() # Monday is 0 and Sunday is 6
    dates = []
    for i in range(7 - weekday):
        day = now + datetime.timedelta(days=i)
        x = str(day).split("-")[::-1]
        x[2] = x[2][2:]
        s = x[0] + "-" + x[1] + "-" + x[2]
        dates.append(s)
    return dates
def NextWeekDate():
    now = datetime.date.today()
    weekday = now.weekday() # Monday is 0 and Sunday is 6
    dates = []
    for i in range(7 - weekday, 14 - weekday):
        day = now + datetime.timedelta(days=i)
        x = str(day).split("-")[::-1]
        x[2] = x[2][2:]
        s = x[0] + "-" + x[1] + "-" + x[2]
        dates.append(s)
    return dates

print(ThisWeekDate())