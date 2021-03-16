import matplotlib.pyplot as plt

cubed=[]
inputVal=[1,2,3,4,5]

for num in inputVal:
    cubed.append(num ** 3) 
    
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal, cubed, c="#acacac", lw="3.1415926", ls="-.", marker="o")

plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

#plot 2
results=[]
inputVal=[1,2,3,4,5]

for num in inputVal:
    results.append(num**2) 
    
ax2 = plt.subplot(1,2,2)    
plt.style.use("seaborn")

#subplot is 1 now, 2 columns, second column
plt.title("Numbers Raised", c="red", fontfamily="Impact", fontsize="14")
plt.subplots_adjust(top=1,wspace=2)
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")

ax2.plot(inputVal, results)

plt.suptitle( "Fun with Numbers")
plt.show()