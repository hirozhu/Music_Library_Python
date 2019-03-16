# Xubo Zhu
# ITP 115
# Assignment 7
# 3/5/2017
# Description: Music Library
### I am sorry I barely have time for writing down all the comments beside this time.
### Hope you could read through the code without them. Hope you wouldnt grade me off because of comments. Thank you!!! <3


import random
import MusicLibraryHelper

libraryFileName = "musicLibrary(1).dat"



def displayMenu():
    print("""Welcome to Your Music Library
Options:
 1) Display library
 2) Display all artists
 3) Add an album
 4) Delete an album
 5) Delete an artist
 6) Search library
 7) Generate a random playlist
 8) Make your own playlist
 9) Exit """)




def displayLibrary(musicLibDictionary):
    # musicLibDictionary = MusicLibraryHelper.loadLibrary(libraryFileName)

    for key in musicLibDictionary:
        print("Artist:",key,
              "\nAlbums:")
        for i in musicLibDictionary[key]:
            print("\t-",i)




def displayArtists(musicLibDictionary):

    print("Displaying all artists:",)
    for key in musicLibDictionary:
        print("-",key)




def addAlbum(musicLibDictionary):
    newKey = input("Enter artist:")
    value = input("Enter album:")
    notInLib = True

    for key in musicLibDictionary:
        if key.lower() == newKey.lower():
            musicLibDictionary[key].append(value)
            notInLib = False

    if notInLib == True:
        musicLibDictionary[newKey]= [value]



def deleteAlbum(musicLibDictionary):
    returnValue = False

    delete_artist = input("Enter artist:")
    delete_album = input("Enter album:")

    for key in musicLibDictionary:
        if key.lower() == delete_artist.lower():
            for i in musicLibDictionary[key]:
                if delete_album.lower() == i.lower():
                    musicLibDictionary[key].remove(i)
                    returnValue = True

    return returnValue



def deleteArtist(musicLibDictionary):
    returnValue = False

    delete_artist = input("Enter artist to delete:")

    for key in musicLibDictionary:
        if delete_artist.lower() == key.lower():
            returnValue = True
            delete_artist = key

    if returnValue == True:
        del musicLibDictionary[delete_artist]

    return returnValue


def searchLibrary(musicLibDictionary):
    term = input("Please enter a search term:")

    print("Artists containing '",term,"'")
    boo = False
    for key in musicLibDictionary:
        if term.lower() in key.lower():
            print("-",key)
            boo = True

    if boo == False:
        print("No result.")
    print("Albums containing '",term,"'")
    bool = False
    for key in musicLibDictionary:
        for i in musicLibDictionary[key]:
            if term.lower() in i.lower():
                print("-",i)
                bool = True
    if bool == False:
        print("No result.")


def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist:")
    for key in musicLibDictionary:
        print("-",random.choice(musicLibDictionary[key]),"by",key)



def generateCustomPlaylist(musicLibDictionary):
    value = True
    playlist = []
    while value == True:

        print("Your playlist so far:")
        for i in playlist:
            print("-",i)

        n = 0
        artists = []
        for i in musicLibDictionary:
            print(n,")",i)
            n += 1
            artists.append(i)

        num1 = int(input("Select an artist from the list by entering its number: "))
        while num1 not in range(0,len(artists)):
            print("*Error, please try again.")
            num1 = int(input("Select an artist from the list by entering its number: "))
        list = musicLibDictionary[artists[num1]]
        k = 0
        for i in list:
            print(k,")",i)
            k += 1

        num2 = int(input("Select an album from the list by entering its number: "))
        while num2 not in range(0,len(list)):
            print("*Error, please try again.")
            num2 = int(input("Select an album from the list by entering its number: "))
        playlist.append(list[num2])

        again = input("Would you like to continue building your playlist? (y/n)")
        if again.lower() == "y":
            value = True
        elif again.lower() == "n":
            value = False
    print("Your completed playlist:")
    for i in playlist:
        print("-",i)


def main():
    musicLibDictionary = MusicLibraryHelper.loadLibrary(libraryFileName)

    k = True
    while k == True:
        displayMenu()
        option = input(">")
        if option == "1":
            displayLibrary(musicLibDictionary)
        elif option == "2":
            displayArtists(musicLibDictionary)
        elif option == "3":
            addAlbum(musicLibDictionary)
        elif option == "4":
            var = deleteAlbum(musicLibDictionary)
            if var == True:
                print("Delete album success!")
            elif var == False:
                print("Delete album failed.")
        elif option == "5":
            vari = deleteArtist(musicLibDictionary)
            if vari == True:
                print("Delete artist success!")
            elif vari == False:
                print("Delete artist failed.")
        elif option == "6":
            searchLibrary(musicLibDictionary)
        elif option == "7":
            generateRandomPlaylist(musicLibDictionary)
        elif option == "8":
            generateCustomPlaylist(musicLibDictionary)
        elif option == "9":
            MusicLibraryHelper.saveLibrary(libraryFileName, musicLibDictionary)
            print("""Saving music library...
Goodbye!""")
            k = False


main()


