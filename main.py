from bs4 import BeautifulSoup
import requests
from tkinter import *
import pickle
import os

os.system("clear");


# TODO In comparePlayerStats Need to adjust the output
# TODO Clean up functions and attempt to reduce the amount of code used
# TODO Find a better way to display output
# TODO Save the player comparisons for later use

def submit():
    playersName = playerNameText.get()
    playerNameTwo = playerNameTwoText.get()

    if len(playerNameTwo) >= 3:
        comparePlayerStats(playersName, playerNameTwo)

    else:
        retrievePlayerInfo(playersName)
        print(len(playerNameTwo))
        print(playerNameTwo)


def retrievePlayerInfo(playerName):

    # Grabs the link using the player name
    link = 'https://r6stats.com/stats/uplay/' + playerName
    print(link)
    source = requests.get(link).text

    soup = BeautifulSoup(source, 'html.parser')

    # Sets all the variables
    kills = soup.find('div', {"class": "value"})
    deaths = kills.find_next('div', {"class": "value"})
    kdRatio = deaths.find_next('div', {"class": "value"})
    hoursPlayed = kdRatio.find_next('div', {"class": "value"})
    winLossRecord = hoursPlayed.find_next('div', {"class": "value"})

    # Adding the labels to the window
    Label(window, text="Kills: " + kills.text, font="none 12 bold").grid(row=3, column=0, sticky=W)
    Label(window, text="Deaths: " + deaths.text, font="none 12 bold").grid(row=4, column=0, sticky=W)
    Label(window, text="Kill Death Ratio: " + kdRatio.text, font="none 12 bold").grid(row=5, column=0, sticky=W)
    Label(window, text="Hours Played: " + hoursPlayed.text, font="none 12 bold").grid(row=6, column=0, sticky=W)
    Label(window, text="Win Loss Record: " + winLossRecord.text, font="none 12 bold").grid(row=7, column=0, sticky=W)


def comparePlayerStats(playerNameOne, playerNameTwo):

    # Shows the name using the label
    Label(window, text=playerNameOne, font="none 12 bold").grid(row=4, column=0, sticky=W)
    Label(window, text=playerNameTwo, font="none 12 bold").grid(row=4, column=1, sticky=W)
    # PLAYER ONE STATS
    link = 'https://r6stats.com/stats/uplay/' + playerNameOne
    print(link)
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')

    # Sets Player Ones Variables
    kills = soup.find('div', {"class": "value"})
    deaths = kills.find_next('div', {"class": "value"})
    kdRatio = deaths.find_next('div', {"class": "value"})
    hoursPlayed = kdRatio.find_next('div', {"class": "value"})
    winLossRecord = hoursPlayed.find_next('div', {"class": "value"})

    # Sets Player Ones Labels
    Label(window, text="Kills: " + kills.text, font="none 12 bold").grid(row=5, column=0, sticky=W)
    Label(window, text="Deaths: " + deaths.text, font="none 12 bold").grid(row=6, column=0, sticky=W)
    Label(window, text="Kill Death Ratio: " + kdRatio.text, font="none 12 bold").grid(row=7, column=0, sticky=W)
    Label(window, text="Hours Played: " + hoursPlayed.text, font="none 12 bold").grid(row=8, column=0, sticky=W)
    Label(window, text="Win Loss Record: " + winLossRecord.text, font="none 12 bold").grid(row=9, column=0, sticky=W)

    # PLAYER TWO STATS
    linkTwo = 'https://r6stats.com/stats/uplay/' + playerNameTwo
    print(linkTwo)
    source = requests.get(linkTwo).text

    soupTwo = BeautifulSoup(source, 'html.parser')

    # Sets Player Two Stats
    killsTwo = soupTwo.find('div', {"class": "value"})
    deathsTwo = killsTwo.find_next('div', {"class": "value"})
    kdRatioTwo = deathsTwo.find_next('div', {"class": "value"})
    hoursPlayedTwo = kdRatio.find_next('div', {"class": "value"})
    winLossRecordTwo = hoursPlayed.find_next('div', {"class": "value"})

    Label(window, text="Kills: " + killsTwo.text, font="none 12 bold").grid(row=5, column=1, sticky=W)
    Label(window, text="Deaths: " + deathsTwo.text, font="none 12 bold").grid(row=6, column=1, sticky=W)
    Label(window, text="Kill Death Ratio: " + kdRatioTwo.text, font="none 12 bold").grid(row=7, column=1, sticky=W)
    Label(window, text="Hours Played: " + hoursPlayedTwo.text, font="none 12 bold").grid(row=8, column=1, sticky=W)
    Label(window, text="Win Loss Record: " + winLossRecordTwo.text, font="none 12 bold").grid(row=9, column=1, sticky=W)

    submitButton=Button(window, text="Submit", width=6, command=submit, bg="black").grid(row=10, column=0, sticky=W)


# Control variable for the loop
controlVariable: str = "1"


# Main Window Creation
window = Tk()
window.title("Rainbow Six Stat Finder")
# window.configure(background="black")

# PlayerName Label and Text Entry
Label(window, text="Enter the players name you would like to look up: ", font="none 12 bold").grid(row=1, column=0,
                                                                                                   sticky=W)
playerNameText = Entry(window, width=15, bg="white")
playerNameText.grid(row=1, column=1, sticky=W)

# PlayerName2 Label and Text Entry
Label(window, text="If you would like to compare statistics enter the other players name:", font="none 12 bold").grid(
    row=2, column=0, sticky=W)
playerNameTwoText = Entry(window, width=15, bg="white")
playerNameTwoText.grid(row=2, column=1, sticky=W)

# Submit Button
submitButton = Button(window, text="Submit", width=6, command=submit, bg="black").grid(row=5, column=0, sticky=W)

# main loop
window.mainloop()
