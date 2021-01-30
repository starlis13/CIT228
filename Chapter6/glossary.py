# Try it yourself 6-3
lstWords = {
    "Tuple":"An immutable list",
    "Dictionary":"Similar to a KeyValuePair in C#",
    "Array":"A semi-rigid complex object that holds other variable types",
    "Conditional":"A term used to refer to a statement that evaluates to true or false for use in 'if' statements and while loops",
    "If":"A keyword followed by a comparison that evalutes to true or false. See Conditional"
}

for entry in lstWords:
    print(entry + ":")
    print(f"\t{lstWords.get(entry)}\n")
    
    
#6-4
for entry in lstWords:
    print(f"{entry}:\n\t{lstWords.get(entry)}\n")