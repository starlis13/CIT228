#8-3
def make_shirt(size, message):
    print(f"A {size} sized shirt has been printed with the phrase '{message}' on it")
    
    
make_shirt("Large", "Hello World!")
make_shirt(message="I need a nap.", size="small")

#8-4
def make_shirt(size = "Large", message = "I Love Python."):
    print(f"A {size} sized shirt has been printed with the phrase '{message}' on it")
    
make_shirt()
make_shirt("Medium")