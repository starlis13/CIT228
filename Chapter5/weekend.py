import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

now = datetime.date.today()
dayOfWeek = now.weekday()
today = weekDays[dayOfWeek]
daysToWeekend = 6-dayOfWeek

print(f"There are {daysToWeekend - 1} days until the weekend")

quotePrinted = True

for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == False:
        print("It's the last day off before the work week")
        quotePrinted = True
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == False:
        print("Gaining momentum may be difficult, but you're doing great!")
        quotePrinted = True
    elif today == "Thursday" and quotePrinted == False:
        print(f"Only {left} more days until the weekend")
        quotePrinted = True
    elif quotePrinted == False:
        print("Enjoy your weekend, you earned it!")
        quotePrinted = True
    else:
        print(left)