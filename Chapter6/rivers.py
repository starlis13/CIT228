#6-5
lstRivers = {
    "Euphrates":"Turkey",
    "Tigris": "Iraq",
    "Mekong":"China"
}

for river in lstRivers:
    print(f"The {river} flows through {lstRivers.get(river)}")
    
print(f"Rivers: {list(lstRivers.keys())}")
print(f"Countries: {list(lstRivers.values())}")