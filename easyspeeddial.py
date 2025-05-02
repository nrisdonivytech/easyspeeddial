# Final Project - Easy Speed Dial
# author: ntr
# IDE: VSCode
# created: 2025-04-28 updated: 2025-04-28 (ntr)
# program that lets a user set 4 contacts and call them with the press of a button
# NO CODING ASSISTANCE was used in this program

# import packages
from tkinter import *
from PIL import ImageTk, Image
import os

# set local path to current folder
modulePath = os.path.dirname(os.path.realpath(__file__))

# get config file path and open it for reading
configFileName = "config.txt"
configPath = os.path.join(modulePath, configFileName)
configFile = open(configPath, 'r')

# get a list of lines in the file
configLines = configFile.readlines()

# iterate through the lines, stripping them of the newline and skipping to after the first space in the file (leaving only the data)
i = 0
for line in configLines:
    newLine = line.split(" ",1)
    newLine = newLine[1].strip()
    configLines[i] = newLine
    i += 1

# set contact names based on the first set of 4 lines in the config
contact1Name = configLines[0]
contact2Name = configLines[1]
contact3Name = configLines[2]
contact4Name = configLines[3]

# set contact images based on the second set of 4 lines in the config
image1Name = configLines[4]
image2Name = configLines[5]
image3Name = configLines[6]
image4Name = configLines[7]

# set phone numbers based on the third set of 4 lines in the config
contact1Number = configLines[8]
contact2Number = configLines[9]
contact3Number = configLines[10]
contact4Number = configLines[11]

# get the full image path of the images using their name and the module path
image1Path = os.path.join(modulePath, image1Name)
image2Path = os.path.join(modulePath, image2Name)
image3Path = os.path.join(modulePath, image3Name)
image4Path = os.path.join(modulePath, image4Name)

# open the images for use later
image1 = Image.open(image1Path)
image2 = Image.open(image2Path)
image3 = Image.open(image3Path)
image4 = Image.open(image4Path)

# function that prints the welcome message
# params: n/a   returns: n/a
def greetingMessage():

    # display welcome message
    print("Easy Speed Dial (by ntr)")
    print()

# function that opens a window corresponding to a phone call, using the photo, name, and phone number associated with the contact 
# params: the photo, name, and phone number associated with the contact
# returns: no variables, but opens a phone call window
def openCallMenu(photo, name, phoneNumber):
    callWindow = Tk()

    # configure window visuals
    callWindow.title("Phone Call")
    callWindow.configure(background="white")
    callWindow.geometry('600x550') 

    # initialize the image associated with the contact and create image label 
    callerPhotoImage = ImageTk.PhotoImage(master=callWindow, file=photo)
    callerPhotoLabel = Label(callWindow, image=callerPhotoImage, background="white", height=400, width=590)
    callerPhotoLabel.grid(row=0, column=0, padx=5, pady=5)

    # create caller name label which includes their name and phone number
    callerDetails = f'{name} ({phoneNumber})'
    callerNameLabel = Label(callWindow, text=callerDetails, font='Roboto 24', background="White")
    callerNameLabel.grid(row=1, column=0)

    # create hang up button that closes the window when pressed
    hangUpButton = Button(callWindow, text="Hang Up", font='Roboto 24', background="Light Gray", command=callWindow.destroy)
    hangUpButton.grid(row=2, column=0)

    # open call window
    callWindow.mainloop()

# function that initializes the GUI window and its elements, including creating the window configuring its title, color, and geometry, creating and initializing all GUI elements, and placing them on a grid
# params: n/a
# returns: the window initialized from the function 
def initializeMainWindow():
   
    # create window
    window = Tk()

    # configure window visuals
    window.title("Easy Speed Dial")
    window.configure(background="white")
    window.geometry('725x825')

    # initialize all the contact photos
    contact1Photo = ImageTk.PhotoImage(file=image1Path)
    contact2Photo = ImageTk.PhotoImage(file=image2Path)
    contact3Photo = ImageTk.PhotoImage(file=image3Path)
    contact4Photo = ImageTk.PhotoImage(file=image4Path)

    # initialize buttons
    contact1Button = Button(window, text=contact1Name, background="light gray", height=350, width=350, image=contact1Photo, command=lambda : openCallMenu(image1Path, contact1Name, contact1Number))
    contact1Button.image = contact1Photo

    contact2Button = Button(window, text=contact2Name, background="light gray", height=350, width=350, image=contact2Photo, command=lambda : openCallMenu(image2Path, contact2Name, contact2Number))
    contact2Button.image = contact2Photo

    contact3Button = Button(window, text=contact3Name, background="light gray", height=350, width=350, image=contact3Photo, command=lambda : openCallMenu(image3Path, contact3Name, contact3Number))
    contact3Button.image = contact3Photo

    contact4Button = Button(window, text=contact4Name, background="light gray", height=350, width=350, image=contact4Photo, command=lambda : openCallMenu(image4Path, contact4Name, contact4Number))
    contact4Button.image = contact4Photo

    # initialize labels
    contact1Label = Label(window, text=contact1Name, font='Roboto 24', background="white")
    contact2Label = Label(window, text=contact2Name, font='Roboto 24', background="white")
    contact3Label = Label(window, text=contact3Name, font='Roboto 24', background="white")
    contact4Label = Label(window, text=contact4Name, font='Roboto 24', background="white")

    # place contact 1's GUI elements
    contact1Label.grid(row=0, column=0, padx=5, pady=5)
    contact1Button.grid(row=1, column=0, padx=5)

    # place contact 2's GUI elements
    contact2Label.grid(row=0,column=1)
    contact2Button.grid(row=1,column=1)

    # place contact 3's GUI elements
    contact3Button.grid(row=2, column=0, padx=5, pady=5)
    contact3Label.grid(row=3, column=0)

    # place contact 4's GUI elements
    contact4Button.grid(row=2,column=1)
    contact4Label.grid(row=3,column=1)

    # return the window
    return window

# program start
greetingMessage()

# initialize and display the program window 
mainWindow = initializeMainWindow()
mainWindow.mainloop()