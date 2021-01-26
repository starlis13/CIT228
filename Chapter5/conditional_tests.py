carMake = "Impala"
chipBrand = "Pringles"
isCellPhoneOn = True
isCellPhoneFunctional = True
higherInteger = 40
lowerInteger = 12
lstMicrophones = []
isProgrammerDoneWithAssignment = True

#Eval as true
print("Predicting chipBrand == Pringles")
if chipBrand == "Pringles":
    print(chipBrand == "Pringles")
    
print(f"Predicting that {higherInteger} > {lowerInteger}")
if higherInteger > lowerInteger:
    print(higherInteger > lowerInteger)
    
print(f"Predicting that the car make is an Impala")
if carMake == "Monte Carlo":
    print("The car isn't an Impala")
elif carMake == "Thunderbird":
    print("The car is not an Impala... Again...")
else:
    print(carMake == "Impala")
    
print("Predicting that the cellPhone is on AND is functioning")
if isCellPhoneOn == True and isCellPhoneFunctional == True:
    print(f"{isCellPhoneOn} and {isCellPhoneFunctional}")

    
#Eval as false
print(f"Predicting that {higherInteger} != {lowerInteger}")
if higherInteger == lowerInteger:
    print("guess I was wrong")
else:
    print(f"{higherInteger} is not, in fact, equal to {lowerInteger}")

print(f"Predicting that the list of microphones is populated")
if lstMicrophones:
    print(f"There are no microphones, only Zuul")
else:
    print(f"I was right!")
    
lstMicrophones = ["AudioTechnica AT2035", "Blue Yeti"]
print(f"Predicting that the list of microphones has 3 items")
if len(lstMicrophones) == 3:
    print("The list does indeed have three items")
    
print("Predicting that the sum of higherInteger and lower integer is 90")
if higherInteger + lowerInteger == 90:
    print(higherInteger + lowerInteger == 90)
    
print("Predicting that I'm not done with this section of the assignment")
if isProgrammerDoneWithAssignment == False:
    print("Thank God I'm wrong.")
    
#5-2
if "Yale" == "Oxford":
    print("Yale" == "Oxford")

if "Yale" != "Oxford":
    print("Yale" == "Oxford")

if("YaLe".lower() == "yAlE".lower()):
    print("YaLe".lower() == "yAlE".lower())
    
if "YaLe".lower() == "yAlE".lower():
    print("YaLe".lower() == "kAlE".lower())
    
if 3 > 2 or 2 < 1 or 1 != 6 or 1 == 1.5 or 5 >= 4 or 4 <= 5:
    print("This is supposed to print when of the conditions is true")
else:
    print("Oops, you've reached this because none of the conditions were true")
    
if 4 > 3 and 5 < 10:
    print("using a keyword")
    
lstItems = ["item1", "item2"]
if lstItems and "item1" in lstItems:
    print("the list exists and there's an expected item in it")
    
if "item3" not in lstItems:
    print("item3 is NOT in the list")