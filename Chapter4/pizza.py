import random

# Chapter 4 Exercise 1
print('-----------------------------------------------------------------------')
lstPizzas = ["Neapolitan", "Meat Lovers", "Four Cheese"]
lstSentences = ["%s is new to my list of favorite pizza types", 
                "One of my childhood favorite pizzas is %s", 
                "You've never tried %s pizza?! Are you crazy?!"
                ]

for pizza in lstPizzas:
    print(pizza)
    
for pizza in lstPizzas:
    print(lstSentences[random.randint(0, 2)]%pizza)