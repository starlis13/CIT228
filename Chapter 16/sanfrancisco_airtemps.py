import csv
import matplotlib.pyplot as plt
import datetime


dates=[]
buckets=[]
highs=[]
lows=[]

with open('sanfrancisco_airtemp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    
    for row in csv_reader:
        row_date = datetime.datetime.strptime(row[2], '%Y-%m-%d')
        
        if not buckets.__contains__(row_date.month):
            buckets.append(row_date.month)
        
            dates.append(f"{row_date.month}/{row_date.day}/{row_date.year}")
            
            if row[3]=='NULL':
                highs.append(0)
            else:
                highs.append(float(row[4]))
                
            if row[4]=='NULL':
                lows.append(0)
            else:
                lows.append(float(row[5]))

fig = plt.figure()
ax1 = fig.add_subplot()
ax2 = fig.add_subplot()  

ax1.scatter(dates, highs, c=highs, cmap=plt.cm.Reds, label="Highs")
ax1.scatter(dates, lows, c=lows, cmap=plt.cm.Blues, label="Lows")

ax1.set_ylabel("Temperature (*F)")
ax1.set_xticklabels(dates)
ax1.set_title("San Francisco Temperatures (03/01/2020 - 03/01/2021)")

plt.suptitle("Temp Analysis")
plt.show() 