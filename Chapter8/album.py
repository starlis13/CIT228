#8-7
def make_album(artistName, albumTitle, numberOfSongs = 0):
    newAlbum = {
        artistName:[albumTitle, numberOfSongs]
    }
    
    return newAlbum;

print(make_album("Def Tiger", "Off Through the Day"))
print(make_album("White Saturday", "Amateur of Fallacy"))
print(make_album("I1", "Forgettable Water"))
print(make_album("AA Bottom", "AAA", 31))

#8-8
continueCreating = True

while continueCreating:
    bandName = input("Enter a band name:\n")
    albumName = input("Enter an album name:\n")
    
    try:
        numberOfTracks = int(input("How many songs are there?\n"))
        
        print(make_album(bandName, albumName, numberOfTracks))
    except ValueError:
        print("You didn't enter an actual number of tracks...")
        
    continueCreating = input("Keep creating albums? Type 'q' to exit, or any key to continue\n") != 'q'