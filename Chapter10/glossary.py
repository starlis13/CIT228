from json import dump as jsonDump, dumps as jsonDumps, load as jsonLoad
filename = "glossary.json"

lstWords = {
    "Tuple":"An immutable list",
    "Dictionary":"Similar to a KeyValuePair in C#",
    "Array":"A semi-rigid complex object that holds other variable types",
    "Conditional":"A term used to refer to a statement that evaluates to true or false for use in 'if' statements and while loops",
    "If":"A keyword followed by a comparison that evalutes to true or false. See Conditional"
}

def WriteGlossaryToFile(fileName):
    with open(fileName, "w") as write_file:
        jsonDump(lstWords, write_file, indent = 4, sort_keys=True)
        
def ReadGlossaryFromFile(fileName):
    with open(filename, "r") as read_file:
        file = jsonLoad(read_file)

    for key, value in file.items():
        print(f"{key} : {value}")
        
def AppendGlossaryEntriesToFile(fileName):
    try:
        newKey = input("Enter a word you'd like to define:\n")
        newValue = input("Enter the definition:\n")
        newEntry = { newKey : newValue}
        
        with open(filename, "r+") as append_file:
            finalEntry = jsonLoad(append_file)
            finalEntry.update(newEntry)
            append_file.seek(0)          
            jsonDump(finalEntry, append_file, indent = 4, sort_keys=True)
    except Exception as ex:
        print("An error occured--------------------")
        print(ex)
    else:
        print("Entry added")


def displayMenu():
    print("\n\n||------------------------------------- Glossary Options ------------------------------------------||")
    print("\t(1) Create the glossary file")
    print("\t(2) Show the current entries")
    print("\t(3) Add a definition")
    print("\t(4) Quit the program")
    
    try:
        choice = int(input("\nPlease choose a menu option:\n"))
    except:
        print("Your menu option was invalid")
    else:
        while choice != 4:
            if choice == 1:
                WriteGlossaryToFile(filename)
            
            if choice == 2:
                ReadGlossaryFromFile(filename)
            
            if choice == 3:
                AppendGlossaryEntriesToFile(filename)
        
            print("\n")
            choice = int(input("\nPlease choose a menu option:\n"))
        

# MAIN PROGRAM
displayMenu()