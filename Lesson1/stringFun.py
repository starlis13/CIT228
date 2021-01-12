# Exercise 1 - use your own first and last name
print("----------------------------------------------")
print("Exercise 1")
name="Steven Starlin"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# Exercise 2 - make up your own noun, adjective, verb, and ending
#  use concatenation to create sentence1
# use an f-string to create sentence2
print("----------------------------------------------")
noun = "squid"
adj = "funky"
verb = "saunters"
ending = "into the discotech"

sentence1 = "the " + adj + " little " + noun + " " + verb + " " + ending
sentence2 = f"the {adj} little {noun} {verb} {ending}"
print(sentence1)
print(sentence2)

# Exercise 3 
print("----------------------------------------------")

sentence1 = """It is by the goodness of God that in our country 
we have those three unspeakably precious things: 
freedom of speech, freedom of conscience, and the 
prudence never to practice either of them.\n-Mark Twain"""

print(sentence1)

# Exercise 4
print("-----------------------------------------------")

sentence1 = "You\t\tcan't\nalways\t\tget\nwhat\t\tyou\nwant\t\tBut\nif\t\tyou\ntry\t\tsometimes\nyou\t\tfind\nYou\t\tget\nwhat\t\tyou\nneed"

print(sentence1)