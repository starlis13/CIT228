import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numUsedOnSites = [376, 348, 153, 104, 19]
explode = (0, .1, 0, 0, 0)
colors=('tab:pink','tab:olive','tab:cyan','tab:orange', 'tab:purple')

fig1, ax1 = plt.subplots()
ax1.pie(numUsedOnSites, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=70, colors=colors)
ax1.axis('equal')
plt.suptitle("Image Types Used On Sites")

plt.show()