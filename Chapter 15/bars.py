import matplotlib.pyplot as plt  
import numpy as np 
# percentage of fast food consumption per day by different sexes and age groups    
#https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]

barWidth=.25

#position of bar on x axis
br1 = np.arange(len(men)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.xticks([r + barWidth for r in range( len(age_range) )], age_range) 

# creating the bar plot 
plt.bar(br1, men, color ='darkgreen', width=barWidth, label="Men")
plt.bar(br2, women, color="maroon",  width=barWidth, label="Women")
plt.bar(br3, total, color="grey", width=barWidth,  label="Total")
  
plt.ylabel("Percentages") 
plt.xlabel("2013 - 2016") 
plt.title("Fast Food Consumption Per Day") 
plt.legend(loc="best")
plt.show() 