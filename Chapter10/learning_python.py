#10-1
filename = "learning_python.txt"

with open(filename) as pythonCapability:
    fileContents = pythonCapability.read()
    
print(f"-------------------Output from {filename}.read()---------------------")
print(fileContents)

print(f"-------------------Output from a for loop using Open--------------------")
with open(filename) as pythonCapability:
    for line in pythonCapability:
        print(line)

print(f"-------------------Output from a list object--------------------")
with open(filename) as pythonCapability:
    lstLines = pythonCapability.readlines()
    
for line in lstLines:
    print(line)
    
#10-2
print(f"-------------------Replacing Python with C--------------------")
with open(filename) as pythonCapability:
    for line in pythonCapability:
        print(line.replace("Python", "C"))
