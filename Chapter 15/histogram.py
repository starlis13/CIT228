import matplotlib.pyplot as plt

#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards
fitness_test=[1760, 1850, 1890, 2050, 2220, 2250, 2265, 2400, 2500, 2625, 2824, 2900, 2901, 2975, 3000, 3000, 3200, 3235, 3550]

# I chose three bins based on the relative magnitude categories of each set of numbers
# Added a column width to create spacing between columns for readability
plt.hist(fitness_test, bins=3, color='lime', rwidth=0.9)
plt.ylabel("Number of Students")
plt.xlabel("Yards")
plt.suptitle("Yards Run By Students in 12 Minutes")

plt.show()