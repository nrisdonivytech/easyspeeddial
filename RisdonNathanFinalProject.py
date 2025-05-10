# Final Project - Easy Speed Dial
# author: ntr
# IDE: VSCode
# created: 2025-04-28 updated: 2025-05-10 (ntr)
# program that lets a user set and configure 4 contacts and call them with the press of a button
# NO CODING ASSISTANCE was used in this program

# pseudo code
# read from a file named config.txt to get the names, image filenames, and phone numbers of 4 contacts
# initialize and open a window that displays a menu with 4 contacts, their names, their photos as buttons, and a config and exit button
# pressing any contact's photo buttons opens a call window where the user can see the contact's name, photo, and phone number, and can press a button to hang up (closing the window)
# pressing the config button opens a window where the user can edit any of the 4 contact's names, image filenames, or phone numbers, automatically changing the GUI in the contact menu and saving the new configuration to the config.txt file when they press the corresponding save button
# pressing the exit button closes the program

# import packages
from tkinter import *
from PIL import ImageTk
import os

# set constants
MODULE_PATH = os.path.dirname(os.path.realpath(__file__)) # the path of the folder that the program is in
CONFIG_FILE_NAME = "config.txt" # the name of the config file
CONFIG_PATH = os.path.join(MODULE_PATH, CONFIG_FILE_NAME) # the full path of the config file

# function that takes an array of strings and strips the newlines from each string
# params: an array of only strings with newlines to be stripped
# returns: n/a, but alters the original array that was passed to it by turning it into an array of strings with no newlines 
def stripLines(linesArray):
    # iterate through the lines, stripping them of the newline
    i = 0 # iterative variable to get the index of the array
    for line in linesArray:
        # strip the newline from the current line
        newLine = line.strip() # the line passed to the loop with the newline stripped
        # replace the line in the array with the stripped line
        linesArray[i] = newLine
        # increment the i variable so it can go to next index in the array on the next iteration
        i += 1

# function that reads the config.txt file and initializes the original configuration the program uses based on the information in that file
# params: n/a
# returns: n/a, but sets 6 global variables (configFile, configLines, contactNames, imageNames, contactNumbers, and imagePaths) which are used by the rest of the program
def initializeConfiguration():

    # initialize the global variables used in other sections of the program
    global configFile # the config.txt file which will be read for configuration and written to when new configurations are saved
    global configLines # an array that contains each individual line in the config.txt file
    global contactNames # an array that contains each of the names of the 4 contacts
    global imageNames # an array that contains the filename for each image of the 4 contacts
    global contactNumbers # an array that contains the phone numbers for each of the 4 contacts
    global imagePaths # an array that contains the full image path for each image of the 4 contacts

    # open config file for reading
    configFile = open(CONFIG_PATH, 'r') # the config.txt file which will be read for configuration and written to when new configurations are saved

    # get a list of lines in the file
    configLines = configFile.readlines() # an array that contains each individual line in the config.txt file

    # strip each line in the file of its newline character so that only the config information is left
    stripLines(configLines)

    # close the file for later writing
    configFile.close()

    # set contact names based on the first set of 4 lines in the config and put them in an array
    contactNames = [configLines[0], configLines[1], configLines[2], configLines[3]] # an array that contains each of the names of the 4 contacts

    # set contact images based on the second set of 4 lines in the config and put them in an array
    imageNames = [configLines[4], configLines[5], configLines[6], configLines[7]] # an array that contains the filename for each image of the 4 contacts

    # set phone numbers based on the third set of 4 lines in the config and put them in an array
    contactNumbers = [configLines[8], configLines[9], configLines[10], configLines[11]] # an array that contains the phone numbers for each of the 4 contacts

    # get the full image paths of the images using their name and the module path and put them in an array
    imagePaths = [os.path.join(MODULE_PATH, imageNames[0]), os.path.join(MODULE_PATH, imageNames[1]), os.path.join(MODULE_PATH, imageNames[2]), os.path.join(MODULE_PATH, imageNames[3])] # an array that contains the full image path for each image of the 4 contacts

# function that closes the window assigned to it as a parameter
def closeWindow(window):
    # destroy the window passed to this function as a parameter
    window.destroy()

# function that opens the config.txt file for writing and updates it with the current program configuration
# params: n/a, but uses the configLines global array as it represents the current configuration
# returns: n/a, but writes to the config.txt file with the new configuration outlined in the configLines array
def updateConfigFile():
    # open config file for writing
    configFile = open(CONFIG_PATH, 'w')

    # add the newlines back to each line in the config data to preserve formatting by looping though each and adding the newline at the end
    i = 0 # iterative variable to get the index of the array
    for line in configLines:
        # add the newline by appending a newline string to the end of the string
        configLines[i] = line + '\n'
        # increment the i variable so it can go to next index in the array on the next iteration
        i += 1
    
    # save the config to the config file
    configFile.writelines(configLines)

    # strip the newlines again so that they dont stack up
    stripLines(configLines)

    # close the config file
    configFile.close()

# function that opens a window that displays a status message
# params: the message the status window will display
# returns: n/a, but opens a window that displays a message
def openStatusWindow(statusMessage):
    # initialize a new window
    statusWindow = Tk() # window object containing a status message
   
    # configure window visuals
    statusWindow.title("Status Message")
    statusWindow.configure(background="white")
    statusWindow.geometry('500x75') 
    # center window elements
    statusWindow.columnconfigure(0, weight=1)

    # initialize and place the status message label at the top of the window, using the statusMessage parameter for the label text
    statusLabel = Label(statusWindow, text=statusMessage, font='Roboto 16', background="white") # the status message label
    statusLabel.grid(row=0,column=0)

    # initialize and place the button that closes the window at the bottom of the window
    closeButton = Button(statusWindow, text="Close", background="light gray", height=2, width=10, command=lambda : closeWindow(statusWindow)) # button that closes the window when pressed
    closeButton.grid(row=1,column=0)

    # display the status message window
    statusWindow.mainloop()

# function that saves a new name for a contact, updating the associated contact's name label and saving it to the config.txt file
# params: the index number associated with the contact to change, the new name for the contact
# returns: n/a, but updates the GUI and writes to the config.txt file with the new name
def saveName(indexNum, name):
    
    # if the text box is empty then open a status message and abort without saving
    if len(name) < 1:
        openStatusWindow("Please enter a name into the name box!")
        return
    
    # change the config line associated with the name to the new name
    configLines[indexNum] = name

    # update the contact's name to match the new name
    contactNames[indexNum] = name
    contactLabels[indexNum].config(text=name)

    # save the new name to the config.txt file
    updateConfigFile()

    # send a saved status message
    openStatusWindow("Saved successfully!")

# function that saves a new image for a contact, updating the associated contact's image label and saving it to the config.txt file
# params: the index number associated with the contact to change, the filename for the new image for the contact
# returns: n/a, but updates the GUI with the new image and writes to the config.txt file with the new filename
def saveImage(indexNum, imageName):
    # if the text box is empty then open a status message and abort without saving
    if len(imageName) < 1:
        openStatusWindow("Please enter a filename into the text box!")
        return
    
    # ensure the new image filename is a valid image by using a try-except clause
    try:
        # get the full path for the new image 
        newImagePath = os.path.join(MODULE_PATH, imageName) # the full path for the new image file
        # attempt to initialize the new image
        contactPhoto = ImageTk.PhotoImage(file=newImagePath) # the image object for the new image
   
    # if image isn't found then send a warning status message and abort without saving
    except:
        openStatusWindow("Image not found! Please try again.")
        return

    # update the associated contact's image with the new image 
    contactButtons[indexNum].configure(image=contactPhoto) 
    contactButtons[indexNum].image = contactPhoto
    imagePaths[indexNum] = newImagePath

    # update the configuration with the new image name
    contactIndex = indexNum + 4 # index that adds 4 to the indexNum so that it accurately reflects the indexes in the contactNumbers array
    configLines[contactIndex] = imageName

    # save the new image filename to the config.txt file
    updateConfigFile()

    # send a saved status message
    openStatusWindow("Saved successfully!")

# function that saves a new phone number for a contact, updating the associated contact's phone number label and saving it to the config.txt file
# params: the index number associated with the contact to change, the new phone number for the contact
# returns: n/a, but updates the GUI and writes to the config.txt file with the new phone number
def savePhoneNumber(indexNum, phoneNumber):
    # ensure the new phone number is a string of 10 characters and abort with an error window if not
    if len(phoneNumber) != 10:
        openStatusWindow("Please enter a 10 character phone number!")
        return
    
    # try to convert the new phone number to an int
    try:
        int(phoneNumber)
    
    # if we can't, it must have non-numbers, so abort and open the error window
    except:
        openStatusWindow("Please remove any special characters and try again.")
        return
    
    # change the config line associated with the phone number and the associated phone number in the phone numbers array to the new number
    configLines[indexNum] = phoneNumber
    contactIndex = indexNum-8 # index that subtracts 8 from the indexNum so that it accurately reflects the indexes in the contactNumbers array
    contactNumbers[contactIndex] = phoneNumber

    # update the configuration file
    updateConfigFile()

    # send a saved status message
    openStatusWindow("Saved successfully!")

# function that opens a window corresponding to a phone call, using the photo, name, and phone number associated with the contact 
# params: the photo, name, and phone number associated with the contact
# returns: n/a, but opens a phone call window
def openCallMenu(photo, name, phoneNumber):
    # initialize a new window
    callWindow = Tk() # window object that contains a phone call
    
    # configure window visuals
    callWindow.title("Phone Call")
    callWindow.configure(background="white")
    callWindow.geometry('600x550') 

    # initialize the image associated with the contact and create image label 
    callerPhotoImage = ImageTk.PhotoImage(master=callWindow, file=photo) # image object associated with the person being called
    callerPhotoLabel = Label(callWindow, image=callerPhotoImage, background="white", height=400, width=590) # image label associated with the person being called

    # create caller name label which includes their name and phone number
    callerDetails = f'{name} ({phoneNumber})' # string that displays the caller's name and phone number
    callerNameLabel = Label(callWindow, text=callerDetails, font='Roboto 24', background="White") # text label associated with the person being called, displaying the person's name and phone number

    # create hang up button that closes the window when pressed
    hangUpButton = Button(callWindow, text="Hang Up", font='Roboto 24', background="Light Gray", command=lambda : closeWindow(callWindow)) # button that closes the window when pressed

    # place all the GUI elements in their associated spot in the grid
    callerPhotoLabel.grid(row=0, column=0, padx=5, pady=5)
    callerNameLabel.grid(row=1, column=0)
    hangUpButton.grid(row=2, column=0)

    # open call window
    callWindow.mainloop()

# function that opens the config window, allowing the user to change their contact's names, images, and phone numbers
# params: n/a
# returns: n/a, but opens a window that lets the user change settings in the config.txt file
def openConfigWindow():
    
    # create config window object
    configWindow = Tk() # window object that contains the config menu

    # configure window visuals
    configWindow.title("Configure Easy Speed Dial")
    configWindow.configure(background="white")
    configWindow.geometry('700x550')

    # configure contact name config labels
    c1NameConfigLabel = Label(configWindow, text="Contact 1 Name: ", background="white", width=20, font='Roboto 20') # text label that says "Contact 1 Name: "
    c2NameConfigLabel = Label(configWindow, text="Contact 2 Name: ", background="white", width=20, font='Roboto 20') # text label that says "Contact 2 Name: "
    c3NameConfigLabel = Label(configWindow, text="Contact 3 Name: ", background="white", width=20, font='Roboto 20') # text label that says "Contact 3 Name: "
    c4NameConfigLabel = Label(configWindow, text="Contact 4 Name: ", background="white", width=20, font='Roboto 20') # text label that says "Contact 4 Name: "

    # configure contact image contact labels
    c1ImageConfigLabel = Label(configWindow, text="Contact 1 Image Filename: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 1 Image Filename: "
    c2ImageConfigLabel = Label(configWindow, text="Contact 2 Image Filename: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 2 Image Filename: "
    c3ImageConfigLabel = Label(configWindow, text="Contact 3 Image Filename: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 3 Image Filename: "
    c4ImageConfigLabel = Label(configWindow, text="Contact 4 Image Filename: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 4 Image Filename: "

    # configure contact phone number labels
    c1NumberConfigLabel = Label(configWindow, text="Contact 1 Phone Number: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 1 Phone Number: "
    c2NumberConfigLabel = Label(configWindow, text="Contact 2 Phone Number: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 2 Phone Number: "
    c3NumberConfigLabel = Label(configWindow, text="Contact 3 Phone Number: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 3 Phone Number: "
    c4NumberConfigLabel = Label(configWindow, text="Contact 4 Phone Number: ", background="white", width=25, font='Roboto 20') # text label that says "Contact 4 Phone Number: "

    # configure contact 1 config entry boxes
    c1NameConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 1's name
    c1ImageConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 1's image using a file name
    c1NumberConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 1's phone number

    # configure contact 2 config entry boxes
    c2NameConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 2's name
    c2ImageConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 2's image using a file name
    c2NumberConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 2's phone number

    # configure contact 3 config entry boxes
    c3NameConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 3's name
    c3ImageConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 3's image using a file name
    c3NumberConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 3's phone number

    # configure contact 4 config entry boxes
    c4NameConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 4's name
    c4ImageConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 4's image using a file name
    c4NumberConfigEntry = Entry(configWindow, background="light gray", width=30) # entry box that lets the user configure contact 4's phone number

    # configure contact 1 save buttons
    c1NameSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveName(0, c1NameConfigEntry.get())) # button that saves contact 1's new name when pressed
    c1ImageSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveImage(0, c1ImageConfigEntry.get())) # button that saves contact 1's new image when pressed
    c1NumberSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : savePhoneNumber(8, c1NumberConfigEntry.get())) # button that saves contact 1's new phone number when pressed

    # configure contact 2 save buttons
    c2NameSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveName(1, c2NameConfigEntry.get())) # button that saves contact 2's new name when pressed
    c2ImageSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveImage(1, c2ImageConfigEntry.get())) # button that saves contact 2's new image when pressed
    c2NumberSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : savePhoneNumber(9, c2NumberConfigEntry.get())) # button that saves contact 2's new phone number when pressed

    # configure contact 3 save buttons
    c3NameSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveName(2, c3NameConfigEntry.get())) # button that saves contact 3's new name when pressed
    c3ImageSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveImage(2, c3ImageConfigEntry.get())) # button that saves contact 3's new image when pressed
    c3NumberSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : savePhoneNumber(10, c3NumberConfigEntry.get())) # button that saves contact 3's new phone number when pressed

    # configure contact 4 save buttons
    c4NameSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveName(3, c4NameConfigEntry.get())) # button that saves contact 4's new name when pressed
    c4ImageSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : saveImage(3, c4ImageConfigEntry.get())) # button that saves contact 4's new image when pressed
    c4NumberSaveButton = Button(configWindow, text="Save", background="light gray", height=2, width=10, command=lambda : savePhoneNumber(11, c4NumberConfigEntry.get())) # button that saves contact 4's new phone number when pressed
    
    # configure close button
    closeButton = Button(configWindow, text="Close Config", background="light gray", height=2, width=30, command=lambda : closeWindow(configWindow)) # button that closes the window when pressed

    # put all the config labels and entries into lists
    configLabels = [c1NameConfigLabel, c1ImageConfigLabel, c1NumberConfigLabel, c2NameConfigLabel, c2ImageConfigLabel, c2NumberConfigLabel, c3NameConfigLabel, c3ImageConfigLabel, c3NumberConfigLabel, c4NameConfigLabel, c4ImageConfigLabel, c4NumberConfigLabel] # array that contains all of the config window's text labels
    configEntries = [c1NameConfigEntry, c1ImageConfigEntry, c1NumberConfigEntry, c2NameConfigEntry, c2ImageConfigEntry, c2NumberConfigEntry, c3NameConfigEntry, c3ImageConfigEntry, c3NumberConfigEntry, c4NameConfigEntry, c4ImageConfigEntry, c4NumberConfigEntry] # array that contains all of the config window's entry boxes
    configSaveButtons = [c1NameSaveButton, c1ImageSaveButton, c1NumberSaveButton, c2NameSaveButton, c2ImageSaveButton, c2NumberSaveButton, c3NameSaveButton, c3ImageSaveButton, c3NumberSaveButton, c4NameSaveButton, c4ImageSaveButton, c4NumberSaveButton] # array that contains all of the config window's save buttons

    # loop through placing all of the config labels in their spot, going down by 1 each time
    i=0 # iterative variable to go down the rows each iteration
    for label in configLabels:
        # place the label in the next row
        label.grid(row=i, column=0)
        # increment i by 1 to go down a row
        i += 1

    # loop through placing all the entry labels in their spot, going down a spot by 1 each time
    i=0 # iterative variable to go down the rows each iteration
    for entry in configEntries:
        # place the entry box in the next row
        entry.grid(row=i, column=1)
        # increment i by 1 to go down a row
        i += 1

     # loop through placing all the save buttons in their spot, going down a spot by 1 each time
    i=0 # iterative variable to go down the rows each iteration
    for button in configSaveButtons:
        # place the button in the next row
        button.grid(row=i, column=2)
        # increment i by 1 to go down a row
        i += 1

    # place the close button at the end, using the i from the end of the last loop to know where the end is
    closeButton.grid(row=i,column=0)

    # display the config window to the screen
    configWindow.mainloop()

# function that initializes the GUI window that contains the contact menu and its elements, including creating the window, configuring its title, color, and geometry, creating and initializing all GUI elements, and placing them on a grid
# params: n/a
# returns: the window initialized from the function that contains the contact menu 
def initializeMainWindow():
   
    # initialize the config variables
    initializeConfiguration()

    # create window
    window = Tk() # window object that contains the main contact menu

    # configure window visuals
    window.title("Easy Speed Dial")
    window.configure(background="white")
    window.geometry('725x900')

    # initialize all the contact photos
    contact1Photo = ImageTk.PhotoImage(file=imagePaths[0]) # photo object that corresponds to contact 1's image
    contact2Photo = ImageTk.PhotoImage(file=imagePaths[1]) # photo object that corresponds to contact 2's image
    contact3Photo = ImageTk.PhotoImage(file=imagePaths[2]) # photo object that corresponds to contact 3's image
    contact4Photo = ImageTk.PhotoImage(file=imagePaths[3]) # photo object that corresponds to contact 4's image

    # initialize contact buttons and their images
    contact1Button = Button(window, text=contactNames[0], background="light gray", height=350, width=350, image=contact1Photo, command=lambda : openCallMenu(imagePaths[0], contactNames[0], contactNumbers[0])) # button that corresponds to contact 1 and calls them when pressed
    contact1Button.image = contact1Photo

    contact2Button = Button(window, text=contactNames[1], background="light gray", height=350, width=350, image=contact2Photo, command=lambda : openCallMenu(imagePaths[1], contactNames[1], contactNumbers[1])) # button that corresponds to contact 2 and calls them when pressed
    contact2Button.image = contact2Photo

    contact3Button = Button(window, text=contactNames[2], background="light gray", height=350, width=350, image=contact3Photo, command=lambda : openCallMenu(imagePaths[2], contactNames[2], contactNumbers[2])) # button that corresponds to contact 3 and calls them when pressed
    contact3Button.image = contact3Photo

    contact4Button = Button(window, text=contactNames[3], background="light gray", height=350, width=350, image=contact4Photo, command=lambda : openCallMenu(imagePaths[3], contactNames[3], contactNumbers[3])) # button that corresponds to contact 4 and calls them when pressed
    contact4Button.image = contact4Photo

    # create a global array that contains each of the contact buttons
    global contactButtons # array that has each contact button contained in it
    contactButtons = [contact1Button, contact2Button, contact3Button, contact4Button] # array that has each contact button contained in it

    # initialize config button
    configButton = Button(window, text="Config", background="light gray", height=2, width=40, command=openConfigWindow) # button that opens the config menu when pressed

    # initialize exit button
    exitButton = Button(window, text="Exit", background="light gray", height=2, width=40, command=lambda : closeWindow(window)) # button that closes the contact menu when pressed

    # initialize labels
    contact1Label = Label(window, text=contactNames[0], font='Roboto 24', background="white") # label that identifies contact 1 with their name
    contact2Label = Label(window, text=contactNames[1], font='Roboto 24', background="white") # label that identifies contact 2 with their name
    contact3Label = Label(window, text=contactNames[2], font='Roboto 24', background="white") # label that identifies contact 3 with their name
    contact4Label = Label(window, text=contactNames[3], font='Roboto 24', background="white") # label that identifies contact 4 with their name

    # create a global array that contains each of the contact labels
    global contactLabels # array that has each contact label contained in it
    contactLabels = [contact1Label, contact2Label, contact3Label, contact4Label] # array that has each contact label contained in it

    # place contact 1's GUI elements in the top left
    contact1Label.grid(row=0, column=0, padx=5, pady=5)
    contact1Button.grid(row=1, column=0, padx=5)

    # place contact 2's GUI elements in the top right
    contact2Label.grid(row=0,column=1)
    contact2Button.grid(row=1,column=1)

    # place contact 3's GUI elements in the bottom left
    contact3Button.grid(row=2, column=0, padx=5, pady=5)
    contact3Label.grid(row=3, column=0)

    # place contact 4's GUI elements in the bottom right
    contact4Button.grid(row=2,column=1)
    contact4Label.grid(row=3,column=1)

    # place the config and exit button under everything else
    configButton.grid(row=5,column=0,pady=20)
    exitButton.grid(row=5,column=1,pady=20)

    # display the main program window
    window.mainloop()

# program start
# initialize and display the program window 
initializeMainWindow()
