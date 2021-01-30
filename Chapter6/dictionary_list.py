dictCaffeineContent = {
    "Monster":"86 mg of caffeine",
    "Coca-Cola":"34 mg of caffeine",
    "Coffee":"95 mg of caffeine"
}

dictCaloriesInFoods = {
    "Steak":"679 calories",
    "Caesar Salad":"94 calories",
    "Kimchi":"50 calories"
}

dictCarbsInConsumables = {
    "Brownie":"14g",
    "Orange Juice":"9g",
    "Bread":"15g"
}

lstCoolNutritionFacts = [dictCaffeineContent, dictCaloriesInFoods, dictCarbsInConsumables]

for dictionary in lstCoolNutritionFacts:
    for item in dictionary:
        print(f"{item} : {dictionary.get(item)}")
    print()
    
