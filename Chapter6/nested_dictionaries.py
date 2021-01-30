dictEngine = {
    "Cooling":"Radiator",
    "CountCynlinders":12,
    "FuelInjected":"Yes"
}

dictCabinOptions = {
    "CountSeating":"5",
    "HasRadio":"Yes",
    "HasHEatedSeats":"No"
}

dictCarParts = {
    "Engine":dictEngine,
    "Cabin":dictCabinOptions
}

for key, val in dictCarParts.items():
    print(f"The {key} has these features:")
    for feature, detail in val.items():
        print(f"\t{feature} : {detail}")