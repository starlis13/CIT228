lstSodas = ["Vernors", "Pepsi", "Coke", "Faygo"]
print(f"Initial list: {lstSodas}")

print(f"Interpolated list: {lstSodas}")

print(f"Print Index: {lstSodas[1]}")

print(f"Print in Title case: {lstSodas[1].title()}")

print(f"Print Last: {lstSodas[-1]}")

print(f"Print Last: {lstSodas[-1]}")

lstSodas.append("Northwoods")
print(f"Append: {lstSodas}")

lstSodas.insert(1, "MUG")
print(f"Insert: {lstSodas}")

del lstSodas[1]
print(f"Del: {lstSodas}")

lstSodas.pop(3)
print(f"Pop(3): {lstSodas}")

lstSodas.pop()
print(f"Pop Last: {lstSodas}")

lstSodas.remove("Vernors")
print(f"Remove: {lstSodas}")

sortedList = sorted(lstSodas)
print(f"Sorted: {sortedList}")

lstSodas.sort()
print(f"Sort: {lstSodas}")

lstSodas.sort(reverse=True)
print(f"Manual Reverse Sort: {lstSodas}")

print(f"The list of soda brand names has {len(lstSodas)} items in it.")

lstSodas[0] = "Canada Dry"
print(f"New Index 0: {lstSodas[0]}")