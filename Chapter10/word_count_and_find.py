def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
        
def find_words(filename, search_term):
    fileLines = []
    occurences = 0
    try:
        with open(filename, "r") as excerpt:
            fileLines = excerpt.readlines()
    except Exception as ex:
        print("There was an error opening the file\n")
        print(ex)
    else:
        for line in fileLines:
            count = line.lower().count(search_term.lower())
            occurences += count
    finally:
        print(f"Your search for '{search_term}' was found {occurences} times in the excerpt saved in {filename}")

filenames = ['trishaInTheWoods.txt', 'theRaven.txt', 'theScreamingStaircase.txt']
for filename in filenames:
    count_words(filename)
    
userSearchTerm = input("What word would you like to search for?\n")
for file in filenames:
    find_words(file, userSearchTerm)