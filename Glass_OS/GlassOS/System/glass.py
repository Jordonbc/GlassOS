import platform  ## Imports platform
import time  ## import the time modules
import urllib  ## imports the main urllib files
import sys
import tkinter

# try:
    # import requests
# except:
    # from GlassOS.libaries import requests as requests

default_stdout = sys.__stdout__
default_stderr = sys.__stderr__
default_stdin = sys.__stdin__

__author__ = 'Jordon'  ## I am the author :)
__terminalVersion__ = "1.1.0"  ## This specifies the version of the terminal

log = open("GlassOS.log", "w")  ## this opens a file called "glassOS.log" and is used to debug modules
log.write(
    "Glass OS started at " + time.strftime("%H:%M:%S") + "\n")  ## Tells the log file what time the program started
log.write(
    "Python version: " + platform.python_version() + "\n")  ## Tells the logfile the version of python that it is using
log.write(
    "Operating System: " + platform.system() + " " + platform.release() + "\n")  ## Tells the log file what os it is on
log.write("Tkinter Version: "+ str(tkinter.TkVersion)+ "\n--------------------------------------------------------\n")
log.write("Importing Required files\n")  ## tells the log that it is importing the required files that is needed
log.write("Importing time module: ")  ## tells the log that it is importing the time module

##############################################################
#    Importing required files and logging it to glassOS.log
##############################################################
try:
    import time

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing importlib module: ")
try:
    import importlib

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing webbrowser module: ")
try:
    import webbrowser

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing winsound module: ")
try:
    import winsound

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing ttk module from tkinter: ")
try:
    from tkinter import ttk

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing filedialog module from tkinter: ")
try:
    from tkinter.filedialog import *

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing colourchooser module from tkinter: ")
try:
    from tkinter.colorchooser import *

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing everything from tkinter: ")
try:
    from tkinter import *

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("Importing os module: ")
try:
    import os

    log.write("Success\n")
except ImportError:
    log.write("Failed\n")
log.write("--------------------------------------------------------\n")

########################################################
#       This part of code defines what happens when it is starting for the first time
########################################################

minWidth = 640
minHeight = 360


def starter():
    log.write("--------------------------------------------------------\n")
    log.write("Running starter()\n")
    log.write("--------------------------------------------------------\n")
    global root  ## defines the main window globally accross the entire program

    ###############################
    # This is so the screen can become fullscreen or windowed
    ###############################
    def fullScreen(self):
        global max
        if max == 0:
            root.attributes('-fullscreen', True)
            max = 1
        else:
            root.attributes('-fullscreen', False)
            max = 0

    root = Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.title("GlassOS Setup")
    root.geometry(str(screenWidth) + "x" + str(screenHeight))
    root.minsize(minWidth, minHeight)  ## the minimum size the program will allow
    root.attributes('-fullscreen', True)  ## makes the program fullscreen
    max = 1  ## a variable used to keep track of window mode
    root.bind("<Escape>", fullScreen)  ## binds the exc key to the window type
    version = open("GlassOS/System/version", "r").read().replace("\n", "")

    userSetup = Frame(root)

    title = Label(root, text="Welcome to Glass OS V" + version, font=("arial", 20, "bold"))
    title.pack()

    description = Label(root, text="This Initial setup will guide you through the settings to configure Glass OS",
                        font=("arial", 15))
    description.pack()

    userSetup.pack()

    def callback(self):
        global file
        username = user.get()
        user_dir = "Users/" + username
        perm = permission.get()
        global username
        username = user.get()

        password = passw.get()
        password2 = passw1.get()

        if username != "":
            if password != "":
                if password == password2:
                    if perm == "0" or perm == "1" or perm == "2":
                        file = open("Users/" + username.lower() + ".profile", "w")
                        if not os.path.exists(user_dir):
                            os.makedirs(user_dir)
                            os.makedirs(user_dir + "/Desktop")
                            os.makedirs(user_dir + "/Documents")
                            os.makedirs(user_dir + "/Pictures")
                            os.makedirs(user_dir + "/Music")
                            os.makedirs(user_dir + "/Videos")
                        file.write("--==")
                        file.write(username)
                        file.write("==--")
                        file.write("\n")
                        file.write(username)
                        file.write("\n")
                        file.write(password)
                        file.write("\n")
                        file.write(perm)
                        file.write("\n")
                        file.write(user_dir)
                        file.close()

                        message.configure(text="Account Successfully Created!")
                        partTwo()
                    else:
                        message.configure(text="Err: Permission is not 0, 1 or 2!")
                else:
                    message.configure(text="Err: passwords do not match!")
            else:
                message.configure(text="Password cannot be blank!")
        else:
            message.configure(text="Username cannot be blank!")

            # Creates all visible text and objects

    blank = Label(userSetup, font=("arial", 16))
    usertitle = Label(userSetup, text="Please Type your name here:", font=("arial", 16))
    passtitle = Label(userSetup, text="Please type your password here:", font=("arial", 16))
    message = Label(userSetup, font=("arial", 16))
    user = Entry(userSetup, font=("arial", 16))
    passw = Entry(userSetup, show='*', font=("arial", 16))
    passw_title = Label(userSetup, text="Please retype your password here:", font=("arial", 16))
    passw1 = Entry(userSetup, show='*', font=("arial", 16))
    go = Button(userSetup, text="Next", font=("arial", 16))
    perm_title = Label(userSetup, text="Enter your permission rights (0 = guest, 1 = admin):", font=("arial", 16))
    permission = Entry(userSetup, font=("arial", 16))

    go.bind("<Button-1>", callback)

    blank.pack()
    blank = Label(userSetup, font=("arial", 16))
    blank.pack()

    usertitle.pack()
    user.pack()

    blank = Label(userSetup, font=("arial", 16))
    blank.pack()
    blank = Label(userSetup, font=("arial", 16))
    blank.pack()

    passtitle.pack()
    passw.pack()

    blank = Label(userSetup, font=("arial", 16))
    blank.pack()
    blank = Label(userSetup, font=("arial", 16))
    blank.pack()

    passw_title.pack()
    passw1.pack()

    blank = Label(userSetup, font=("arial", 16))
    blank.pack()
    blank = Label(userSetup, font=("arial", 16))
    blank.pack()

    perm_title.pack()
    permission.pack()

    blank = Label(userSetup, font=("arial", 16))
    blank.pack()
    blank = Label(userSetup, font=("arial", 16))
    blank.pack()

    permission.bind("<Return>", callback)

    go.pack()
    message.pack()

    def partTwo():  ## allows the user to change settings before starting up the program fully
        global root
        try:
            userSetup.destroy()
        except:
            pass
        settingsFrame = Frame(root)
        settingsFrame.pack()

        menuColour = "#a0fd44"

        def save():
            global root
            global menuColour
            file = open("GlassOS/System/settings.settings", "w")
            file.write(widthBox.get())
            file.write("\n")
            file.write(heightBox.get())
            file.write("\n")
            file.write(userSpaceBox.get())
            file.write("\n")
            file.write(backgroundBox.get())
            file.write("\n")
            file.write(colour)
            file.write("\n")
            file.write(startPictureBox.get())
            file.write("\n")
            file.write(str(start_fullSlider.get()))

            msg.configure(text="Saved Successfully")
            file.close()

            root.destroy()
            os.remove("GlassOS/System/newOS")

        def chooseColour():  ## allows the user to change the menu colours
            global colour
            menuColourBox.delete(0, END)
            colour = askcolor()
            colour = colour[1]
            menuColourBox.insert(index=0, string=colour)

        left = Frame(settingsFrame)
        left.pack(side=LEFT)

        right = Frame(settingsFrame)
        right.pack(side=RIGHT)

        settings_title = Label(settingsFrame, text="Settings")

        displayWidthTitle = Label(left, text="Display Width:", font=("arial", 16))
        widthBox = Entry(left, font=("arial", 16))
        widthBox.insert(index=0, string=screenWidth)

        displayHeightTitle = Label(left, text="Display Height:", font=("arial", 16))
        heightBox = Entry(left, font=("arial", 16))
        heightBox.insert(index=0, string=screenHeight)

        userSpaceTitle = Label(left, text="User Directory:", font=("arial", 16))
        userSpaceBox = Entry(left, font=("arial", 16))
        userSpaceBox.insert(index=0, string="Users/")

        backgroundTitle = Label(right, text="Background:", font=("arial", 16))
        backgroundBox = Entry(right, font=("arial", 16))
        backgroundBox.insert(index=0, string="Users/background.png")

        menuColourTitle = Label(right, text="Menu Colour:", font=("arial", 16))
        menuColourChooser = Button(right, text="Choose Colour", command=chooseColour, bg=menuColour,
                                   font=("arial", 16))
        menuColourBox = Entry(right, font=("arial", 16))
        menuColourBox.insert(index=0, string="#a0fd44")
        colour = menuColour

        startPictureTitle = Label(right, text="Start Menu Icon:", font=("arial", 16))
        startPictureBox = Entry(right, font=("arial", 16))
        startPictureBox.insert(index=0, string="GlassOS/start.png")

        startFullTitle = Label(right, text="Use fullScreen start:", font=("arial", 16))
        start_fullSlider = Scale(right, from_=0, to=1, orient=HORIZONTAL, font=("arial", 16))
        start_fullSlider.set(0)

        saveButton = Button(settingsFrame, text="Finish", command=save, font=("arial", 16))
        msg = Label(settingsFrame, font=("arial", 16))

        blank = Label(settingsFrame, font=("arial", 16))

        settingsTitle = Label(settingsFrame, text="Settings", font=("Arial", 20, "bold"))

        settingsTitle.pack(side=TOP)
        displayWidthTitle.pack()
        widthBox.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        displayHeightTitle.pack()
        heightBox.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        userSpaceTitle.pack()
        userSpaceBox.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        backgroundTitle.pack()
        backgroundBox.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        menuColourTitle.pack()
        menuColourBox.pack()
        menuColourChooser.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        startPictureTitle.pack()
        startPictureBox.pack()

        blank = Label(settingsFrame, font=("arial", 16))
        blank.pack()

        startFullTitle.pack()
        start_fullSlider.pack()

        blank.pack()
        saveButton.pack()
        msg.pack()

    root.mainloop()  ## this makes it so that the program doesn't just close

log.write("Checking for newOS in GlassOS/System\n")
if os.path.exists("GlassOS/System/newOS"):  ## checks for of the newOS file exists and if so start the user setup
    log.write("newOS Detected!\n")
    starter()
else:
    log.write("newOS NOT detected!\n")
    log.write("--------------------------------------------------------\n")

log.write("Getting Version information from GlassOS/System\n")
try:
    version = open("GlassOS/System/version", "r").read().replace("\n", "")  ## opens the program version
    log.write("Version detected: "+ str(version) +"\n")
    log.write("--------------------------------------------------------\n")
except:
    log.write("Version Not detected!\n")
    log.write("Fatal Error Detected: Unable to get version Information!\n")
    log.write("Shutting down")
    log.write("--------------------------------------------------------\n")
    sys.exit()

log.write("Making Dummy Window for screen width and height\n")
try:
    root = Tk()  ## Creates a dummy window to get the screen width and hight
    screenWidth = root.winfo_screenwidth()  ## Gets the screen width and hight
    screenHeight = root.winfo_screenheight()
    root.destroy()  ## destroys the dummy window
    log.write("Width: "+ str(screenWidth) +"\n")
    log.write("Height: "+ str(screenHeight) + "\n")
    log.write("--------------------------------------------------------\n")
except:
    log.write("Fatal Error Detected: Unable to get Screen Resolution!\n")
    log.write("Check your tkinter install\n")
    log.write("--------------------------------------------------------\n")
    sys.exit()

# (screenWidth)
# print(screenHeight)

log.write("Atempting to get settings from GlassOS/System\n")

try:
    settingsFileOpen = open("GlassOS/System/settings.settings", "r")
    settingsFile = settingsFileOpen.readlines()
    settingsFileOpen.close()
    log.write("System settings Detected!\n")
except:
    log.write("Fatal Error Detected: Unable to get settings from file!\n")
    log.write("--------------------------------------------------------\n")
    sys.exit()

width = settingsFile[0].replace("\n", "")
log.write("Width: " + str(width) + "\n")

height = settingsFile[1].replace("\n", "")
log.write("Height: "+ height + "\n")

menuColour = settingsFile[4].replace("\n", "")
log.write("Menu Colour: " + str(menuColour) + "\n")

startMenuPic = settingsFile[5].replace("\n", "")
log.write("Start Menu Picture: " + str(startMenuPic) + "\n")

start_full = settingsFile[6].replace("\n", "")
log.write("start Menu Fullscreen: "+ str(start_full) + "\n")
log.write("--------------------------------------------------------\n")

log.write("Checking if recent exists in GlassOS/\n")
try:
    recentListOpen = open("GlassOS/Recent", "r")
    recentList = recentListOpen.readlines()
    recentListOpen.close()
    log.write("recent Detected!\n")
    log.write("--------------------------------------------------------\n")
except:
    log.write("Warning: recent NOT detected in /!\n")
    log.write("--------------------------------------------------------\n")
    sys.exit()
    
log.write("Checking the setting width against screen\n")

if int(width) > int(screenWidth):
    log.write("Warning: width is larger than screen size!\n")
    width = str(screenWidth)
    log.write("Correction made!\n")
else:
    log.write("Width is ok\n")

log.write("Checking the setting height against screen\n")
    
if int(height) > int(screenHeight):
    log.write("Warning: height is larger than screen size!\n")
    height = str(screenHeight)
    log.write("Correction made!\n")
else:
    log.write("Height is ok\n")

log.write("--------------------------------------------------------\n")
settingsFileOpen.close()

widthHeight = width + "x" + height

centerWidth = int(int(width) / 2)
centerHeight = int(int(height) / 2)

screenCenter = str(centerWidth) + "x" + str(centerHeight)

users = settingsFile[2].replace("\n", "")
background = settingsFile[3].replace("\n", "")


def login(windowTitle, widthHeight="1920x1080", icon="", bgColour=None, bg=None, bgWidth="350", bgHeight="250",
          allUsersDir=""):
    log.write("Running lgoin()\n")
    global username
    global active
    try:
        log.write("Atempting to create window\n")
        window = Tk()
        window.title(windowTitle)
        window.geometry(widthHeight)
        canvas = Canvas(window, width=bgWidth, height=bgHeight)
        frame = Frame(canvas)
        frame.configure(bg=bgColour)
        log.write("Success, window created!\n")
    except:
        log.write("Fatal Error Detected: Unable to create window!\n")
        sys.exit()

    max = 0

    def fullScreen(self):
        global max
        if max == 0:
            window.attributes('-fullscreen', True)
            max = 1
        else:
            window.attributes('-fullscreen', False)
            max = 0

    window.attributes('-fullscreen', True)
    max = 1

    window.bind("<Escape>", fullScreen)

    try:
        log.write("Atempting to draw background on window\n")
        background_image = PhotoImage(file=bg)
        canvas.create_image(0, 0, image=background_image, anchor=NW)
        canvas.pack(expand=YES, fill=BOTH)
        log.write("Success, Background Created!\n")
    except:
        log.write("Warning: Unable to draw background! Skipping\n")
    try:
        log.write("Atempting to add icon to window\n")
        window.wm_iconbitmap(icon)
        log.write("Icon Successfully Created!\n")
    except:
        log.write("Warning: Unable to Create icon on window! Skipping\n")
    try:
        log.write("Atempting to draw background on window\n")
        window.configure(bg=bgColour)
        log.write("Background Successfully Created!\n")
    except:
        log.write("Warning: Unable to create Background Colour! Skipping\n")

    def callback(event):
        global username
        username = user.get()

        try:
            file = open(allUsersDir + username.lower() + ".profile", "r")
            file.close()
        except:
            message.configure(text="Err: Username or password is incorrect!")
        file = open(allUsersDir + username.lower() + ".profile", "r")
        global line
        line = file.readlines()

        global password
        password = passw.get()
        if username == line[1].strip() and password == line[2].strip():
            message.configure(text="Logged in.")
            active = username
            tmp = open("active", "w")
            tmp.write(active)
            window.destroy()
            # user_dir = line[4]
        else:
            message.configure(text="Err: Username and password don't match the profile")

    title1 = Label(frame, text="Login to " + windowTitle + "\n", bg=bgColour)
    usertitle = Label(frame, text="---Username---", bg=bgColour)
    passtitle = Label(frame, text="---Password---", bg=bgColour)
    message = Label(frame, bg=bgColour)
    user = Entry(frame)
    passw = Entry(frame, show="*")
    go = Button(frame, text="Log in!", bg="#00FF00")

    frame.place(x=int(window.winfo_width() / 3), y=window.winfo_height() / 3,
                width=int(int(window.winfo_width()) / 3),
                height=int(int(window.winfo_height()) / 3))
    title1.pack()
    usertitle.pack()
    user.pack()
    passtitle.pack()
    passw.pack()
    go.pack()
    message.pack()

    user.focus()

    def reposition(self):
        frame.place_configure(x=int(window.winfo_width() / 3), y=window.winfo_height() / 3,
                              width=int(int(window.winfo_width()) / 3),
                              height=int(int(window.winfo_height()) / 3))

    go.bind("<Button-1>", callback)
    go.bind("<Return>", callback)
    passw.bind("<Return>", callback)
    window.bind("<Configure>", reposition)
    
    log.write("--------------------------------------------------------\n")

    window.mainloop()


login("GlassOS", widthHeight=widthHeight, allUsersDir=users, bg=background, bgWidth=width, bgHeight=height)

try:
    active = open("active", "r").read()
except:
    sys.exit()
try:
    os.remove("active")
except:
    sys.exit()
username = active
user_dir = users + username


def box(event):
    global clicked
    if (clicked == False):
        searchvar.set("")
        search.config(fg="black")
        clicked = True


def search_internet(self):
    # TODO: Find a way to implement a browser
    webbrowser.open_new_tab("https://www.google.co.uk/#q=" + searchvar.get().replace(" ", "+"))


def terminal():
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("terminal")
    recentAdd.close()

    def askPermDialog(program):

        def yes():
            rootPermDialog.destroy()
            global rootTerminal

            try:
                os.remove("GlassOS/Cache/terminalCache.py")
            except:
                pass

            global a
            a = 0

            class TextRedirector(object):
                def __init__(self, widget, tag="stdout"):
                    self.widget = widget
                    self.tag = tag

                def write(self, str):
                    self.widget.configure(state="normal")
                    self.widget.insert("end", str, (self.tag,))
                    self.widget.configure(state="disabled")

            def terminal(command=None):
                def run(command=None):
                    temp = open("GlassOS/Cache/terminalCache.py", "w")
                    temp.close()
                    if input.get() == "cc":
                        if not os.path.exists("GlassOS/Cache"):
                            os.makedirs("GlassOS/Cache")
                        elif not os.path.exists("GlassOS/Cache/terminalCache.py"):
                            temp = open("GlassOS/Cache/terminalCache.py", "w")
                            temp.close()
                        elif os.path.exists("GlassOS/Cache/terminalCache.py"):
                            os.remove("GlassOS/Cache/terminalCache.py")
                            temp = open("GlassOS/Cache/terminalCache.py", "w")
                            temp.close()
                        input.delete(0, END)
                        print("\nCache Cleared")
                    elif "bg " in input.get():
                        input.delete(0, END)
                        try:
                            output.configure(bg=str(input.get).replace("bg ", "").replace("\n", ""))
                        except:
                            print("\n Colour must be hexadecimal!")
                    elif "fg " in input.get():
                        input.delete(0, END)
                        try:
                            output.configure(fg=str(input.get).replace("fg ", "").replace("\n", ""))
                        except:
                            print("\n Colour must be hexadecimal!")
                    elif input.get() == "clear":
                        input.delete(0, END)
                        print("\n" * 25)
                    else:
                        global a
                        a += 1
                        file = open("GlassOS/Cache/terminalCache.py", "a")
                        file.write(input.get() + "\n")
                        file.close()
                        input.delete(0, END)
                        cache = "GlassOS.Cache.terminalCache"

                        if a == 1:
                            importlib.import_module("GlassOS.Cache.terminalCache")
                            os.remove("GlassOS/Cache/terminalCache.py")
                        else:
                            import GlassOS
                            import GlassOS.Cache
                            import GlassOS.Cache.terminalCache
                            importlib.reload(GlassOS.Cache.terminalCache)
                    try:
                        os.remove("GlassOS/Cache/terminalCache.py")
                    except:
                        pass
                    temp = open("GlassOS/Cache/terminalCache.py", "w")
                    temp.close()
                    sys.stdout = default_stdout
                    sys.stderr = default_stderr
                    sys.stdin = default_stdin

                rootTerminal = Tk()
                rootTerminal.title("Terminal")
                rootTerminal.geometry("400x300")
                rootTerminal.minsize(200, 200)
                rootTerminal.configure(bg="#000000")

                output = Text(rootTerminal, state=DISABLED, height=10, bg="#000000", fg="#FFFFFF", wrap="word")
                output.configure(state=NORMAL)
                output.insert(END, "Glass OS Terminal V" + __terminalVersion__ + "\n")
                output.configure(state=DISABLED)
                output.pack(side=TOP, expand=YES, fill=BOTH)

                input = Entry(rootTerminal, width=400, bg="#000000", fg="#FFFFFF")
                input.focus()
                input.bind("<Return>", run)
                input.pack(side=BOTTOM)

                sys.stdout = TextRedirector(output, "stdout")
                sys.stderr = TextRedirector(output, "stderr")

                rootTerminal.mainloop()

            terminal()

            appFocus = 1

            global appFocus

            def minimize(self):
                global appFocus
                appFocus = 0

            def closeApp():
                appIcon.destroy()
                rootTerminal.destroy()
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                sys.stdin = sys.__stdin__

            def focusApp():
                global appFocus
                if appFocus == 0:
                    rootTerminal.focus_force()
                    appFocus = 1

                else:
                    appFocus = 0
                    rootTerminal.focus_set()

            appIcon = Button(toolbar, text="Terminal", command=focusApp)
            appIcon.pack(side=LEFT, fill=Y)
            rootTerminal.bind("<Unmap>", minimize)
            rootTerminal.protocol("WM_DELETE_WINDOW", closeApp)

        def no():
            rootPermDialog.destroy()

        bgColour = None
        rootPermDialog = Tk()
        rootPermDialog.title("Permission: " + program)
        rootPermDialog.geometry("310x155")
        rootPermDialog.configure(bg=bgColour)
        dialogFont = ("Apple Boy BTN Regular", 10, "bold")

        ptext = Label(rootPermDialog, text=program, font=dialogFont, bg=bgColour)
        dtext = Label(rootPermDialog, text="This program requires administrative access.\n\n" +
                                           "If you do not know what the program does\nthis could be an attempt to change the system,\n\n" +
                                           "Only press 'Yes' if you trust the program", font=dialogFont, bg=bgColour)

        yButton = Button(rootPermDialog, text="Yes", font=dialogFont, bg=bgColour, command=yes)
        nButton = Button(rootPermDialog, text="No", font=dialogFont, bg=bgColour, command=no)

        ptext.pack()
        dtext.pack()

        nButton.pack(side=RIGHT)
        yButton.pack(side=RIGHT)

        rootPermDialog.mainloop()

    askPermDialog("Terminal")


def musicPlayer():
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("musicPlayer")
    recentAdd.close()

    rootMusicPlayer = Tk()
    rootMusicPlayer.title("Music Player - Experimental")
    rootMusicPlayer.geometry("180x50" + "+" + str(centerWidth - 90) + "+" + str(centerHeight - 25))

    def openFile():
        file = askopenfilename(defaultextension=".wav",
                               filetypes=[("Windows Audio File", ".wav")])
        sound.delete(0, END)
        sound.insert(0, file)
        if file != None:

            winsound.PlaySound(file, winsound.SND_FILENAME)
        else:
            pass

    sound = Entry(rootMusicPlayer)
    openButton = Button(rootMusicPlayer, text="Open", command=openFile)

    sound.pack(side=LEFT)
    openButton.pack(side=LEFT)

    appFocus = 1

    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootMusicPlayer.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootMusicPlayer.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootMusicPlayer.focus_set()

    appIcon = Button(toolbar, text="Music Player", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)
    rootMusicPlayer.bind("<Unmap>", minimize)
    rootMusicPlayer.protocol("WM_DELETE_WINDOW", closeApp)

    rootMusicPlayer.mainloop()


def settings():
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("settings")
    recentAdd.close()

    global answer
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    def askPermDialog(program):
        bgColour = None
        rootPermDialog = Tk()
        rootPermDialog.title("Permission: " + program)
        rootPermDialog.geometry("310x155")
        rootPermDialog.configure(bg=bgColour)
        dialogFont = ("Apple Boy BTN Regular", 10, "bold")

        def yes():
            global menuColour
            global colour
            rootPermDialog.destroy()
            global rootSettings
            """

            Starts the settings program

            """

            def save():
                global menuColour
                file = open("GlassOS/System/settings.settings", "w")
                file.write(widthBox.get())
                file.write("\n")
                file.write(heightBox.get())
                file.write("\n")
                file.write(userSpaceBox.get())
                file.write("\n")
                file.write(backgroundBox.get())
                file.write("\n")
                file.write(colour)
                file.write("\n")
                file.write(startPictureBox.get())
                file.write("\n")
                file.write(str(start_fullSlider.get()))

                # background_image = PhotoImage(file=background)
                # canvas.create_image(0, 0, image=background_image, anchor=NW)

                msg.configure(text="Saved Successfully")
                file.close()

            def chooseColour():
                global colour
                menuColourBox.delete(0, END)
                colour = askcolor()
                colour = colour[1]
                menuColourBox.insert(index=0, string=colour)

            def createUser():
                def addUser(title="", widthHeight="250x350", icon=None, bgColour=None, allUsers=""):
                    window = Tk()
                    window.title("New User")
                    window.geometry(widthHeight)
                    try:
                        window.wm_iconbitmap(icon)
                    except:
                        pass
                    window.configure(bg=bgColour)

                    def callback():
                        global file
                        username = user.get()
                        user_dir = "Users/" + username
                        perm = permission.get()
                        global username
                        username = user.get()

                        password = passw.get()
                        password2 = passw1.get()
                        if username != "":
                            if password != "":
                                if password == password2:
                                    if perm == "0" or perm == "1" or perm == "2":
                                        file = open(allUsers + username.lower() + ".profile", "a")
                                        if not os.path.exists(user_dir):
                                            os.makedirs(user_dir)
                                        file.write("--==")
                                        file.write(username)
                                        file.write("==--")
                                        file.write("\n")
                                        file.write(username)
                                        file.write("\n")
                                        file.write(password)
                                        file.write("\n")
                                        file.write(perm)
                                        file.write("\n")
                                        file.write(user_dir)

                                        message.configure(text="Account Successfully Created!")
                                    else:
                                        message.configure(text="Err: Permission is not 0, 1 or 2!")
                                else:
                                    message.configure(text="Err: passwords do not match!")
                            else:
                                message.configure(text="Password cannot be blank!")
                        else:
                            message.configure(text="Username cannot be blank!")

                    title1 = Label(window, text="Add an account to " + title + "\n", bg=bgColour)
                    usertitle = Label(window, text="---Username---", bg=bgColour)
                    passtitle = Label(window, text="---Password---", bg=bgColour)
                    message = Label(window, bg=bgColour)
                    user = Entry(window)
                    passw = Entry(window, show='*')
                    passw_title = Label(window, text="---Retype-Password--", bg=bgColour)
                    passw1 = Entry(window, show='*')
                    go = Button(window, text="Add Account!", command=callback, bg="#00FF00")
                    perm_title = Label(window, text="---Permission Level--", bg=bgColour)
                    permission = Entry(window)

                    title1.pack()
                    usertitle.pack()
                    user.pack()
                    passtitle.pack()
                    passw.pack()
                    passw_title.pack()
                    passw1.pack()
                    perm_title.pack()
                    permission.pack()
                    go.pack()
                    message.pack()

                    window.mainloop()

                addUser(title="Glass OS", bgColour=menuColour, allUsers=users)

            def reset():
                sureDialog = Tk()
                sureDialog.title("Reset Glass OS")

                def y():
                    try:
                        sureDialog.destroy()
                    except:
                        pass
                    try:
                        rootSettings.destroy()
                    except:
                        pass
                    try:
                        rootJpad.destroy()
                    except:
                        pass
                    try:
                        start_menu.destroy()
                    except:
                        pass
                    try:
                        root_window.destroy()
                    except:
                        pass

                    w = open("reset", "w")
                    w.close()

                def n():
                    sureDialog.destroy()

                yesButton = Button(sureDialog, text="Yes, reset Glass OS!", command=y)
                noButton = Button(sureDialog, text="No, Don't reset Glass OS", command=n)
                description = Label(sureDialog, text="Are you sure you want to reset Glass OS?")

                description.pack()
                yesButton.pack()
                noButton.pack()

            rootSettings = Tk()
            screen_width = screenWidth
            screen_height = screenHeight
            rootSettings.title("Settings")
            rootSettings.geometry("400x500" + "+" + str(centerWidth - 200) + "+" + str(centerHeight - 250))

            settingsFileOpen = open("GlassOS/System/settings.settings", "r+")
            settingsFile = settingsFileOpen.readlines()
            settingsFileOpen.close()

            settings_title = Label(rootSettings, text="Settings")

            displayWidthTitle = Label(rootSettings, text="Display Width:")
            widthBox = Entry(rootSettings)
            widthBox.insert(index=0, string=settingsFile[0].replace("\n", ""))

            displayHeightTitle = Label(rootSettings, text="Display Height:")
            heightBox = Entry(rootSettings)
            heightBox.insert(index=0, string=settingsFile[1].replace("\n", ""))

            userSpaceTitle = Label(rootSettings, text="User Directory:")
            userSpaceBox = Entry(rootSettings)
            userSpaceBox.insert(index=0, string=settingsFile[2].replace("\n", ""))

            backgroundTitle = Label(rootSettings, text="Background:")
            backgroundBox = Entry(rootSettings)
            backgroundBox.insert(index=0, string=settingsFile[3].replace("\n", ""))

            menuColourTitle = Label(rootSettings, text="Menu Colour:")
            menuColourChooser = Button(rootSettings, text="Choose Colour", command=chooseColour, bg=menuColour)
            menuColourBox = Entry(rootSettings)
            menuColourBox.insert(index=0, string=menuColour)
            colour = menuColour

            startPictureTitle = Label(rootSettings, text="Start Menu Icon:")
            startPictureBox = Entry(rootSettings)
            startPictureBox.insert(index=0, string=settingsFile[5].replace("\n", ""))

            startFullTitle = Label(rootSettings, text="Use fullScreen start:")
            start_fullSlider = Scale(rootSettings, from_=0, to=1, orient=HORIZONTAL)
            start_fullSlider.set(int(start_full))

            resetButton = Button(rootSettings, text="Reset my System!", command=reset)

            saveButton = Button(rootSettings, text="Save", command=save)
            msg = Label(rootSettings)

            blank = Label(rootSettings)

            warn = Label(rootSettings, text="Warning! Changing these setting may damage the operating system!",
                         fg="#FF0000")

            settingsTitle = Label(rootSettings, text="Settings", font=("Arial", 20, "bold"))

            createUserButton = Button(rootSettings, text="Create New User", command=createUser)

            settingsTitle.pack(side=TOP)
            displayWidthTitle.pack()
            widthBox.pack()
            displayHeightTitle.pack()
            heightBox.pack()
            userSpaceTitle.pack()
            userSpaceBox.pack()
            backgroundTitle.pack()
            backgroundBox.pack()
            menuColourTitle.pack()
            menuColourBox.pack()
            menuColourChooser.pack()
            startPictureTitle.pack()
            startPictureBox.pack()
            createUserButton.pack()
            startFullTitle.pack()
            start_fullSlider.pack()
            resetButton.pack()

            blank.pack()
            saveButton.pack()
            msg.pack()
            warn.pack(side=BOTTOM)

            appFocus = 1

            global appFocus

            def minimize(self):
                global appFocus
                appFocus = 0

            def closeApp():
                appIcon.destroy()
                rootSettings.destroy()

            def focusApp():
                global appFocus
                if appFocus == 0:
                    rootSettings.focus_force()
                    appFocus = 1

                else:
                    appFocus = 0
                    rootSettings.focus_set()

            appIcon = Button(toolbar, text="Settings", command=focusApp)
            appIcon.pack(side=LEFT, fill=Y)
            rootSettings.bind("<Unmap>", minimize)
            rootSettings.protocol("WM_DELETE_WINDOW", closeApp)

            rootSettings.mainloop()

        def no():
            rootPermDialog.destroy()

        ptext = Label(rootPermDialog, text=program, font=dialogFont, bg=bgColour)
        dtext = Label(rootPermDialog, text="This program requires administrative access.\n\n" +
                                           "If you do not know what the program does\nthis could be an attempt to change the system,\n\n" +
                                           "Only press 'Yes' if you trust the program", font=dialogFont, bg=bgColour)

        yButton = Button(rootPermDialog, text="Yes", font=dialogFont, bg=bgColour, command=yes)
        nButton = Button(rootPermDialog, text="No", font=dialogFont, bg=bgColour, command=no)

        ptext.pack()
        dtext.pack()

        nButton.pack(side=RIGHT)
        yButton.pack(side=RIGHT)

        rootPermDialog.mainloop()

    askPermDialog("Settings")


start_open = 0
global start_menu
global toolbar


def hardwareMonitor():
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass
    try:
        import psutil
    except:
        from GlassOS.libaries import psutil as psutil
    import platform

    if "linux" in platform.system():
        print("LINUX MONITORING DON'T WORK YET")

    hardwareMon = Tk()
    hardwareMon.title("Hardware Monitor")
    hardwareMon.geometry("600x180")
    hardwareMon.minsize(width=600, height=180)

    diskFrame = Frame(hardwareMon)
    diskFrame.pack(side=LEFT, expand=YES)

    RAMFrame = Frame(hardwareMon)
    RAMFrame.pack(side=LEFT, expand=YES)

    cpuFrame = Frame(hardwareMon)
    cpuFrame.pack(side=LEFT, expand=YES)

    def tick():
        global current
        current = ""
        if psutil.cpu_percent() != current:

            def size(num, suffix='B'):
                num = int(num)
                for unit in ['B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                    if abs(num) < 1024:
                        return "%3.1f%s%s" % (num, unit, suffix)
                    num /= 1024
                return "%.1f%s%s" % (num, 'Y', suffix)

            RAM = psutil.virtual_memory()
            ramTotal = size(str(RAM[0]).replace("svmem(total=", ""))
            ramAvailableFree = size(
                str(RAM[1]).replace("available=", ""))
            ramUsedPercent = str(RAM[2]).replace("percent=", "")
            ramUsed = size(str(RAM[3]).replace("used=", ""))

            DISK = psutil.disk_usage("/")
            diskTotal = size(str(DISK[0]).replace("sdiskusage(total=", ""))
            diskUsed = size(str(DISK[1]).replace("used=", ""))
            diskFree = size(str(DISK[2]).replace("free=", ""))
            diskUsedPercent = str(DISK[3]).replace("percent=", "")

            cpuUsedPercent = psutil.cpu_percent(1)
            cpuLogicalCores = psutil.cpu_count(logical=True)
            cpuCores = psutil.cpu_count(logical=False)

            current = psutil.cpu_percent()

            cpuPercentLabel.configure(text="CPU Percent: " + str(cpuUsedPercent) + "%")
            cpuCoresLabel.configure(text="CPU Cores: " + str(cpuCores))
            cpuLogicalCoresLabel.configure(text="CPU Logical Cores: " + str(cpuLogicalCores))

            RAMPercentLabel.configure(
                text="RAM used as Percentage: " + str(ramUsedPercent) + "%")
            RAMTotalLabel.configure(
                text="Total RAM: " + str(ramTotal))
            RAMAvailableFreeLabel.configure(
                text="RAM Available/Free: " + str(ramAvailableFree))
            RAMUsedLabel.configure(
                text="RAM used: " + str(ramUsed))

            diskPercentLabel.configure(
                text="Disk space used as percentage: " + str(diskUsedPercent) + "%")
            diskTotalLabel.configure(
                text="Total disk space: " + str(diskTotal))
            diskUsedLabel.configure(
                text="Disk space used: " + str(diskUsed))
            diskFreeLabel.configure(
                text="Disk space free: " + str(diskFree))

            cpuPercentLabel.after(5000, tick)
        else:
            cpuPercentLabel.after(5000, tick)

    cpuLabel = Label(cpuFrame, text="CPU Status", font=("Arial", 20, "bold"))

    cpuNameLabel = Label(cpuFrame, text="Processor Name: " + platform.processor())
    cpuPercentLabel = Label(cpuFrame, text="CPU Percent: ")
    cpuCoresLabel = Label(cpuFrame, text="CPU Cores: ")
    cpuLogicalCoresLabel = Label(cpuFrame, text="CPU Logical Cores: ")
    cpuLabel.pack()
    cpuNameLabel.pack()
    cpuPercentLabel.pack()
    cpuCoresLabel.pack()
    cpuLogicalCoresLabel.pack()

    diskLabel = Label(diskFrame, text="Disk Status", font=("Arial", 20, "bold"))

    diskPercentLabel = Label(diskFrame, text='Disk space used as percentage: ')
    diskTotalLabel = Label(diskFrame, text='Total disk space: ')
    diskUsedLabel = Label(diskFrame, text='Disk space used: ')
    diskFreeLabel = Label(diskFrame, text='Disk space free: ')
    diskLabel.pack()
    diskPercentLabel.pack()
    diskTotalLabel.pack()
    diskUsedLabel.pack()
    diskFreeLabel.pack()

    RAMLabel = Label(RAMFrame, text="RAM Status", font=("Arial", 20, "bold"))

    RAMPercentLabel = Label(RAMFrame, text="RAM used as Percentage: ")
    RAMTotalLabel = Label(RAMFrame, text="Total RAM: ")
    RAMAvailableFreeLabel = Label(RAMFrame, text="RAM Available/Free: ")
    RAMUsedLabel = Label(RAMFrame, text="RAM used: ")
    RAMLabel.pack()
    RAMPercentLabel.pack()
    RAMTotalLabel.pack()
    RAMAvailableFreeLabel.pack()
    RAMUsedLabel.pack()

    tick()

    appFocus = 1

    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        hardwareMon.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            hardwareMon.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            hardwareMon.focus_set()

    appIcon = Button(toolbar, text="Task Monitor", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)
    hardwareMon.bind("<Unmap>", minimize)
    hardwareMon.protocol("WM_DELETE_WINDOW", closeApp)

    hardwareMon.mainloop()


def restart():
    try:
        rootUpdate.destroy()
    except:
        pass
    try:
        rootSettings.destroy()
    except:
        pass
    try:
        rootJpad.destroy()
    except:
        pass
    try:
        start_menu.destroy()
    except:
        pass
    try:
        root_window.destroy()
    except:
        pass
    f = open("state", "w")
    f.write("1")
    f.close()


def jpadEditor(file=None):
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("jpad")
    recentAdd.close()

    jpadFile = file

    """
    Starts Jpad
    """
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass
    global rootJpad
    global jpadEditor
    width = "500"
    height = "400"

    widthHeight = width + "x" + height

    rootJpad = Tk()

    sWidth = rootJpad.winfo_screenwidth()
    sHeight = rootJpad.winfo_screenheight()

    rootJpad.title("Jpad")
    rootJpad.geometry(widthHeight + "+" + str(centerWidth - 250) + "+" + str(centerHeight - 200))
    rootJpad.maxsize(sWidth, sHeight)
    rootJpad.minsize("200", "200")

    textPad = Text(rootJpad)
    textPad.configure(bg=menuColour)
    textPad.focus()

    textPad.pack(expand=YES, fill=BOTH)

    font = ["Arial", "11", "normal"]

    textPad.configure(font=(font[0], int(font[1]), font[2]))

    def chfont():
        def apply():
            try:
                textPad.configure(font=(font1.get(), int(font2.get()), font3.get()))
                font[0] = font1.get()
                font[1] = font2.get()
                font[2] = font3.get()

                rootFont.destroy()
            except:
                msg.configure(text="Whoops, something went wrong while applying your font!")

        rootFont = Tk()
        rootFont.title("Font")
        rootFont.geometry("320x110")

        font1 = Entry(rootFont)
        font2 = Entry(rootFont)
        font3 = Entry(rootFont)

        font1.insert(0, font[0])
        font2.insert(0, font[1])
        font3.insert(0, font[2])

        applyButton = Button(rootFont, text="Apply Font", command=apply)
        msg = Label(rootFont)

        font1.pack()
        font2.pack()
        font3.pack()
        applyButton.pack()
        msg.pack()

        rootFont.mainloop()

    def open_command():
        nonlocal jpadFile
        jpadFile = askopenfilename(defaultextension=".txt",
                                   filetypes=[("Text Files", ".txt"), ("Python .py", ".py"), ("Python .pyw", ".pyw"),
                                              ("All Files", ".*")],
                                   initialdir=user_dir)

        rootJpad.title("Jpad Text Editor" + "     File: " + jpadFile)
        jpadFile = open(jpadFile, "r")
        if jpadFile != None:
            contents = jpadFile.read()
            textPad.delete(0.0, END)
            textPad.insert(0.0, contents)
            jpadFile.close()

    def save_command():
        nonlocal jpadFile
        jpadFile = open(file, "w")
        if jpadFile != None:
            # slice off the last character from get, as an extra return is added
            data = textPad.get(0.0, END)
            jpadFile.write(data)
            jpadFile.close()

    def saveAs_command():
        nonlocal jpadFile
        jpadFile = asksaveasfilename(defaultextension=".txt",
                                     filetypes=[("Text Files", ".txt"), ("Python .py", ".py"), ("Python .pyw", ".pyw"),
                                                ("All Files", ".*")],
                                     initialdir=user_dir)
        rootJpad.title("Jpad Text Editor" + "     File: " + jpadFile)
        jpadFile = open(jpadFile, "w")
        if jpadFile != None:
            # slice off the last character from get, as an extra return is added
            data = textPad.get(0.0, END)
            jpadFile.write(data)
            jpadFile.close()

    def exit_command():
        closeApp()

    def new():
        rootJpad.title("Jpad Text Editor" + "     File: New File")
        textPad.delete(0.0, END)

    if jpadFile != None:
        rootJpad.title("Jpad Text Editor" + "     File: " + str(jpadFile))
        jpadFile = open(file, "r")
        contents = jpadFile.read()
        textPad.delete(0.0, END)
        textPad.insert(0.0, contents)
        jpadFile.close()

    menu = Menu(rootJpad)
    rootJpad.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Open...", command=open_command)
    filemenu.add_command(label="Save", command=save_command)
    filemenu.add_command(label="Save As", command=saveAs_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_command)

    fontMenu = Menu(menu)
    menu.add_cascade(label="Font", menu=fontMenu)
    fontMenu.add_command(label="font", command=chfont)

    appFocus = 1

    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootJpad.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootJpad.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootJpad.focus_set()

    appIcon = Button(toolbar, text="Jpad", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)
    rootJpad.bind("<Unmap>", minimize)
    rootJpad.protocol("WM_DELETE_WINDOW", closeApp)

    rootJpad.mainloop()


def appUnavailable(app):
    global start_menu
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    appFocus = 1
    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootApp.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootApp.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootApp.focus_set()

    app = str(app)

    rootApp = Tk()
    rootApp.configure(bg=menuColour)
    rootApp.title(app + " Unavailable")
    rootApp.geometry("400x300" + "+" + str(centerWidth - 200) + "+" + str(centerHeight - 150))

    appIcon = Button(toolbar, text=app + " Unavailable", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)

    rootApp.bind("<Unmap>", minimize)

    text = Label(rootApp, text=app + " coming soon!", bg=menuColour)

    text.place(x=200, y=150, anchor=CENTER)

    rootApp.protocol("WM_DELETE_WINDOW", closeApp)

    rootApp.mainloop()


def info():
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("info")
    recentAdd.close()

    global start_menu
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    appFocus = 1
    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootInfo.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootInfo.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootInfo.focus_set()

    rootInfo = Tk()
    rootInfo.configure(bg=menuColour)
    rootInfo.title("Glass OS Information Panel")
    rootInfo.geometry("400x300" + "+" + str(centerWidth - 200) + "+" + str(centerHeight - 150))

    # glassOSLogo = PhotoImage(file="GlassOS/Glass_OS_Logo.png")
    # glassOSPicture = Button(rootInfo, image=glassOSLogo)

    glassOSPicture = Label(rootInfo, text="Glass OS " + version,
                           font=("Space Bd BT Bold", 32, ""), fg="#FF0000", bg=menuColour)
    glassOSPicture.pack()

    appIcon = Button(toolbar, text="Glass OS Information Panel", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)

    rootInfo.bind("<Unmap>", minimize)

    text = Label(rootInfo, text="You are currently running Glass OS version " + version + ".", bg=menuColour)

    text.place(x=200, y=150, anchor=CENTER)

    rootInfo.protocol("WM_DELETE_WINDOW", closeApp)

    rootInfo.mainloop()


def glass_quit():
    """
    Quits the Program
    """
    try:
        start_open = 0
        start_menu.destroy()
        root_window.destroy()
        sys.exit()
    except:
        pass


def file_Explorer(folder=""):
    if folder != "":
        pass
    else:
        folder = user_dir
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("fe")
    recentAdd.close()

    """
    Starts File Explorer
    """

    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    def dir_see(posX, posY, title="Title", directory="C:/", width_and_height="300x200"):
        global rootFV

        def fill_tree(treeview, node):
            if treeview.set(node, "type") != 'directory':
                return

            path = treeview.set(node, "fullpath")
            # Delete the possibly 'dummy' node present.
            treeview.delete(*treeview.get_children(node))

            parent = treeview.parent(node)
            for p in os.listdir(path):
                p = os.path.join(path, p)
                ptype = None
                if os.path.isdir(p):
                    ptype = 'directory'

                fname = os.path.split(p)[1]
                oid = treeview.insert(node, 'end', text=fname, values=[p, ptype])
                if ptype == 'directory':
                    treeview.insert(oid, 0, text='dummy')

        def update_tree(event):
            treeview = event.widget
            fill_tree(treeview, treeview.focus())

        def create_root(treeview, startpath):
            dfpath = os.path.abspath(startpath)
            node = treeview.insert('', 'end', text=dfpath,
                                   values=[dfpath, "directory"], open=True)
            fill_tree(treeview, node)

        rootFV = Tk()
        treeview = ttk.Treeview(rootFV, columns=("fullpath", "type"))

        rootFV.geometry(str(width_and_height) + "+" + str(str(posX) + "+" + str(posY)))
        rootFV.title(title)

        treeview.pack(fill='both', expand=True)
        create_root(treeview, directory)
        treeview.bind('<<TreeviewOpen>>', update_tree)

        appFocus = 1
        global appFocus

        def minimize(self):
            global appFocus
            appFocus = 0

        def closeApp():
            appIcon.destroy()
            rootFV.destroy()

        def focusApp():
            global appFocus
            if appFocus == 0:
                rootFV.focus_force()
                appFocus = 1

            else:
                appFocus = 0
                rootFV.focus_set()

        appIcon = Button(toolbar, text=user_dir + " - File Explorer", command=focusApp)
        appIcon.pack(side=LEFT, fill=Y)

        rootFV.bind("<Unmap>", minimize)
        rootFV.protocol("WM_DELETE_WINDOW", closeApp)

        rootFV.mainloop()

    dir_see(posX=centerWidth - 150, posY=centerHeight - 100, title=user_dir + " -File Explorer",
            directory=folder)


def update_check(checked=0):
    global rootUpdate
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("chkUpdate")
    recentAdd.close()
    # TODO: Allow users to some how update the program
    """
    Updates the program
    """

    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("info")
    recentAdd.close()

    global start_menu
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    appFocus = 1
    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootUpdate.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootUpdate.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootUpdate.focus_set()

    rootUpdate = Tk()
    rootUpdate.configure(bg=menuColour)
    rootUpdate.title("Glass OS Updating Tool")
    rootUpdate.geometry("400x300" + "+" + str(centerWidth - 200) + "+" + str(centerHeight - 150))

    statusText = Label(rootUpdate, bg=menuColour)

    def update():
        statusText.configure(text="Status: Updating...")
        testfile = urllib.request.urlretrieve(
            "https://github.com/Jordonbc/GlassOS/archive/master.zip", "update.zip")
        # zipFile = requests.get("https://github.com/Jordonbc/GlassOS/archive/master.zip")

        statusText.configure(text="Status: done, restart Glass OS to continue.")
        checkButton.configure(text="Restart", command=restart)

    def check():
        try:
            statusText.configure(text="Status: checking")
            # updateFile = urllib.request.urlretrieve(
            # "https://raw.githubusercontent.com/Jordonbc/GlassOS/master/updater.txt, updater.txt")
            updateFile = requests.get("https://raw.githubusercontent.com/Jordonbc/GlassOS/master/updater.txt")
            file = open("updater.txt", "w")
            file.write(updateFile.text)
            file.close()
        except:
            statusText.configure(text="Status: Could not contact server")

        try:
            updateVerFile = open("updater.txt", "r")
            updateVer = updateVerFile.read()
            updateVerFile.close()

            if int(updateVer) > int(version):
                statusText.configure(text="Status: There is a new update available!", fg="#0000ff")
                checkButton.configure(text="Update!", command=update)
            elif int(updateVer) == int(version):
                statusText.configure(text="Status: You are using the latest version.")
                checkButton.configure(text="You are up to date!", state=DISABLED)
            elif int(updateVer) < int(version):
                statusText.configure(text="Status: You are using the latest Dev Version of Glass OS.")
        except:
            if os.path.exists("updater.txt"):
                statusText.configure(text="status: Failed to read file", fg="#ff0000")
            else:
                statusText.configure(text="Status: Could not contact server")

                # glassOSLogo = PhotoImage(file="GlassOS/Glass_OS_Logo.png")
                # glassOSPicture = Button(rootInfo, image=glassOSLogo)

                # glassOSPicture = Label(rootUpdate, text="Glass OS " + version,
                # font=("Space Bd BT Bold", 32, ""), fg="#FF0000", bg=menuColour)

    # glassOSPicture.pack()

    appIcon = Button(toolbar, text="Glass OS Updating Tool", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)

    rootUpdate.bind("<Unmap>", minimize)

    # text = Label(rootUpdate, text="You are currently running Glass OS version " + version + ".", bg=menuColour)

    # text.place(x=200, y=150, anchor=CENTER)

    statusText.pack()
    checkButton = Button(rootUpdate, text="Check for updates", command=check)
    checkButton.pack()

    rootUpdate.protocol("WM_DELETE_WINDOW", closeApp)

    rootUpdate.mainloop()


# def store():
#     global rootUpdate
#     recentAdd = open("GlassOS/Recent", "a")
#     recentAdd.write("\n")
#     recentAdd.write("store")
#     recentAdd.close()
#
#     global start_menu
#     try:
#         start_open = 0
#         start_menu.destroy()
#     except:
#         pass
#
#     appFocus = 1
#     global appFocus
#
#     def minimize(self):
#         global appFocus
#         appFocus = 0
#
#     def closeApp():
#         appIcon.destroy()
#         rootStore.destroy()
#
#     def focusApp():
#         global appFocus
#         if appFocus == 0:
#             rootStore.focus_force()
#             appFocus = 1
#
#         else:
#             appFocus = 0
#             root.focus_set()
#
#     rootStore = Tk()
#     rootStore.configure(bg=menuColour)
#     rootStore.title("Glass OS Updating Tool")
#     rootStore.geometry("600x400" + "+" + str(centerWidth - 300) + "+" + str(centerHeight - 200))
#     rootStore.minsize(width="600", height="400")
#     rootStore.maxsize(width="600", height="400")
#     titleFrame = Frame(rootStore)
#     titleFrame.configure(bg=menuColour)
#     titleFrame.place(x=0, y=5, width=600, height=30)
#
#     title = Label(titleFrame, text="Glass OS Store", font=("OCR A Std", 24), bg=menuColour)
#     title.pack(side=LEFT)
#
#     userEntry = Entry(titleFrame, text="Username")
#     userPassEntry = Entry(titleFrame, text="Password")
#     goButon = Button(titleFrame, text="Login")
#
#     goButon.pack(side=RIGHT)
#     userEntry.pack(side=RIGHT)
#     userPassEntry.pack(side=RIGHT)
#
#     menu = Frame(rootStore)
#     menu.configure(bg="#ffffff")
#     menu.place(x=10, y=40, width=580, height=350)
#
#     jpadFrame = Frame(menu)
#     jpadFrame.configure(bg="#aaaaaa", width="570")
#     jpadFrame.pack()
#     jpadApp = Button(jpadFrame, text="APP_01", font=("OCR A Std",))
#     jpadApp.pack(side=LEFT)
#
#     if os.path.exists("Programs/jpadApp.py"):
#         jpadApp.configure(text="Uninstall Jpad")
#     else:
#         jpadApp.configure(text="Install Jpad")
#
#
#     appIcon = Button(toolbar, text="Store", command=focusApp)
#     appIcon.pack(side=LEFT, fill=Y)
#     rootStore.bind("<Unmap>", minimize)
#     rootStore.protocol("WM_DELETE_WINDOW", closeApp)
#
#     rootStore.mainloop()


# def pyInterpreter():
#     global rootInterpreter
#     global start_menu
#     try:
#         start_open = 0
#         start_menu.destroy()
#     except:
#         pass
#
#     appFocus = 1
#     global appFocus
#     global rootInterpreter
#
#     def minimize(self):
#         global appFocus
#         appFocus = 0
#
#     def closeApp():
#         global rootInterpreter
#         appIcon.destroy()
#         rootInterpreter.destroy()
#
#     def focusApp():
#         global rootInterpreter
#         global appFocus
#         if appFocus == 0:
#             rootInterpreter.focus_force()
#             appFocus = 1
#
#         else:
#             appFocus = 0
#             rootInterpreter.focus_set()
#
#     global a
#     a = 0
#
#
#     class TextRedirector(object):
#         def __init__(self, widget, tag="stdout"):
#             self.widget = widget
#             self.tag = tag
#
#         def write(self, str):
#             self.widget.configure(state="normal")
#             self.widget.insert("end", str, (self.tag,))
#             self.widget.configure(state="disabled")
#
#     def Interpreter():
#         global rootInterpreter
#         def run(command=None):
#             global rootInterpreter
#             global a
#             a += 1
#             file = open("cache.py", "w")
#             file.write(input.get(0.0, END))
#             file.close()
#             cache = "cache"
#             if a == 1:
#                 importlib.import_module(cache)
#             else:
#                 import cache
#                 importlib.reload(cache)
#
#         rootInterpreter = Tk()
#         rootInterpreter.title("Terminal")
#         rootInterpreter.geometry("200x200")
#         rootInterpreter.minsize(200, 200)
#         rootInterpreter.configure(bg="#000000")
#
#         executeButton = Button(rootInterpreter, text="Execute", command=run)
#
#         output = Text(rootInterpreter, state=DISABLED, height=10, bg="#000000", fg="#FFFFFF", wrap="word")
#         output.configure(state=NORMAL)
#         output.configure(state=DISABLED)
#         output.pack(side=TOP, expand=YES, fill=BOTH)
#
#         input = Text(rootInterpreter, width=400, bg="#000000", fg="#FFFFFF")
#         input.focus()
#         input.pack(side=BOTTOM)
#         executeButton.pack()
#
#         sys.stdout = TextRedirector(output, "stdout")
#
#         rootInterpreter.mainloop()
#
#     appIcon = Button(toolbar, text="PyInterpreter", command=focusApp)
#     appIcon.pack(side=LEFT, fill=Y)
#
#     global rootInterpreter
#     rootInterpreter.bind("<Unmap>", minimize)
#     rootInterpreter.protocol("WM_DELETE_WINDOW", closeApp)
#
#     Interpreter()


def cal():
    recentAdd = open("GlassOS/Recent", "a")
    recentAdd.write("\n")
    recentAdd.write("cal")
    recentAdd.close()

    # TODO: Implement Custom app launcher into Glass OS
    sys.path.insert(0, "Programs")

    global start_menu
    try:
        start_open = 0
        start_menu.destroy()
    except:
        pass

    appFocus = 1
    global appFocus

    def minimize(self):
        global appFocus
        appFocus = 0

    def closeApp():
        appIcon.destroy()
        rootCal.destroy()

    def focusApp():
        global appFocus
        if appFocus == 0:
            rootCal.focus_force()
            appFocus = 1

        else:
            appFocus = 0
            rootCal.focus_set()

    def execute():
        program = askopenfilename(defaultextension=".py",
                                  filetypes=[("Executable File", ".py"),("Executable", ".exe")],
                                  initialdir="Programs")
        viewName.configure(state=NORMAL)
        viewName.delete(0, END)
        viewName.insert(0, program)
        viewName.configure(state=DISABLED)
        try:
            importlib.import_module(program)
            status.configure(text="Program Running!", fg="#00FF00")
        except NameError:
            status.configure(text="Error: No Module called " + "'" + program + "'" + " was found in 'programs'.",
                             fg="#FF0000")
            # print()

    rootCal = Tk()
    rootCal.configure(bg=menuColour)
    rootCal.title("Custom App Launcher")
    rootCal.geometry("400x300" + "+" + str(centerWidth - 200) + "+" + str(centerHeight - 150))
    appIcon = Button(toolbar, text="Custom App Launcher", command=focusApp)
    appIcon.pack(side=LEFT, fill=Y)
    rootCal.bind("<Unmap>", minimize)
    rootCal.protocol("WM_DELETE_WINDOW", closeApp)

    title = Label(rootCal, text="Custom App Launcher", bg=menuColour)
    viewName = Entry(rootCal, bg=menuColour)
    viewName.configure(state=DISABLED)
    execFile = Button(rootCal, text="Open and Execute file", command=execute, bg=menuColour)
    status = Label(rootCal, bg=menuColour)
    ver = Label(rootCal, text="Version: ALPHA", bg=menuColour)

    title.pack()
    viewName.pack()
    execFile.pack()
    status.pack()
    ver.pack(side=BOTTOM, anchor=CENTER)

    rootCal.mainloop()


def start():
    """

    Makes the start Menu appear and disappear

    """
    global menuColour
    global canvas
    global restart
    global settings
    global start_menu
    global start_open
    global allPrograms
    global showAllOpen
    global recentFrame
    global root_windowX
    global root_windowY

    if start_open == 0:
        global jpad
        start_menu = Tk()
        start_menu.configure(bg=menuColour)
        start_menu.focus()

        settingsFileOpen = open("GlassOS/System/settings.settings", "r")
        settingsFile = settingsFileOpen.readlines()
        settingsFileOpen.close()

        start_full = settingsFile[6].replace("\n", "")

        start_menu.title("Start")

        recentFrame = Frame(start_menu)
        recentFrame.pack()
        recentFrame.configure(bg=menuColour)

        if start_full == "1":
            row0 = Frame(recentFrame)
            row1 = Frame(recentFrame)
            row2 = Frame(recentFrame)
            row3 = Frame(recentFrame)
            recentLabel = Label(row0, text="Recent", bg=menuColour)
            recentLabel.pack()
            row0.configure(height=200, bg=menuColour)

            buttonWidth = 20
            buttonHeight = 10

            start_menu.geometry(
                str(width) + "x" + str(int(height) - 85) + "+" + "0" + "+" + "0")

            hardwareMonitorButton = Button(row1, text="TaskHardware Monitor", command=hardwareMonitor,
                                           width=buttonWidth,
                                           height=buttonHeight,
                                           bg=menuColour)
            musicPlayerButton = Button(row1, text="Music Player - Experimental", command=musicPlayer, width=buttonWidth,
                                       height=buttonHeight,
                                       bg=menuColour)
            infoButton = Button(row1, text="Glass OS Info Panel", command=info, width=buttonWidth,
                                height=buttonHeight, bg=menuColour)
            CustomAppLauncherButton = Button(row1, text="Custom App Launcher", command=cal, width=buttonWidth,
                                             height=buttonHeight,
                                             bg=menuColour)
            terminalButton = Button(row1, text="Terminal", command=terminal, width=buttonWidth,
                                    height=buttonHeight, bg=menuColour)
            restartButton = Button(row1, text="Restart", command=restart, width=buttonWidth,
                                   height=buttonHeight, bg=menuColour)
            jpadButton = Button(row2, text="Jpad", command=jpadEditor, width=100, bg=menuColour)
            chkUpdates = Button(row3, text="Check for Updates", command=update_check, width=buttonWidth,
                                height=buttonHeight, bg=menuColour)
            settingsButton = Button(row2, text="Settings", command=settings, width=buttonWidth,
                                    height=buttonHeight, bg=menuColour)
            fileExplorer = Button(row2, text="File Explorer", command=file_Explorer, width=buttonWidth,
                                  height=buttonHeight, bg=menuColour)
            shutdown = Button(row2, text="Shutdown", command=glass_quit, width=buttonWidth,
                              height=buttonHeight, bg=menuColour)

            row0.pack()
            row1.pack()
            row2.pack()
            row3.pack()
        else:
            recentLabel = Label(recentFrame, text="Recent", bg=menuColour)
            recentLabel.pack()

            print("Start Menu X = " + str(root_windowX) + " Start Menu Y = " + str(root_windowY))

            start_menu.geometry("242x260" + "+" + str(root_windowX) + "+" + str(root_windowY - 315))

            hardwareMonitorButton = Button(recentFrame, text="TaskHardware Monitor", command=hardwareMonitor, width=100,
                                           bg=menuColour)
            musicPlayerButton = Button(recentFrame, text="Music Player - Experimental", command=musicPlayer, width=100,
                                       bg=menuColour)
            infoButton = Button(recentFrame, text="Glass OS Info Panel", command=info, width=100, bg=menuColour)
            CustomAppLauncherButton = Button(recentFrame, text="Custom App Launcher", command=cal, width=100,
                                             bg=menuColour)
            terminalButton = Button(recentFrame, text="Terminal", command=terminal, width=100, bg=menuColour)
            restartButton = Button(recentFrame, text="Restart", command=restart, width=100, bg=menuColour)
            jpadButton = Button(recentFrame, text="Jpad", command=jpadEditor, width=100, bg=menuColour)
            chkUpdates = Button(recentFrame, text="Check for Updates", command=update_check, width=100, bg=menuColour)
            settingsButton = Button(recentFrame, text="Settings", command=settings, width=100, bg=menuColour)
            fileExplorer = Button(recentFrame, text="File Explorer", command=file_Explorer, width=100, bg=menuColour)
            shutdown = Button(recentFrame, text="Shutdown", command=glass_quit, width=100, bg=menuColour)
        try:
            allPrograms.destroy()
        except:
            pass

        recentListOpen = open("GlassOS/Recent", "r")
        recentList = recentListOpen.readlines()
        del recentList[0]
        recentListOpen.close()

        # print(recentList)

        a = -1
        try:
            for x in recentList:
                recentList[a] = recentList[a].replace("\n", "")
                a += 1
        except:
            pass
        try:
            if len(recentList) >= 6:
                del recentList[0]
                recentListOpen = open("GlassOS/Recent", "w")

                a = -1
                for x in recentList:
                    recentListOpen.write("\n")
                    recentListOpen.write(recentList[a])
                    a += 1
                recentListOpen.close()
        except:
            pass
        if "taskMonitor" in recentList:
            hardwareMonitorButton.pack()
        if "musicPlayer" in recentList:
            musicPlayerButton.pack()
        if "jpad" in recentList:
            jpadButton.pack()
        if "chkUpdate" in recentList:
            chkUpdates.pack()
        if "cal" in recentList:
            CustomAppLauncherButton.pack()
        if "fe" in recentList:
            fileExplorer.pack()
        if "info" in recentList:
            infoButton.pack()
        if "settings" in recentList:
            settingsButton.pack()
        if "terminal" in recentList:
            terminalButton.pack()
        if "restart" in recentList:
            restartButton.pack()
        if "shutdown" in recentList:
            shutdown.pack()

        showAllOpen = 0

        def showAll():
            global showAllOpen
            allPrograms = Frame(start_menu)
            allPrograms.configure(bg=menuColour)
            row0 = Frame(allPrograms)
            row1 = Frame(allPrograms)
            row2 = Frame(allPrograms)
            row3 = Frame(allPrograms)
            row0.configure(height=200, bg=menuColour)

            if showAllOpen == 0:
                recentFrame.destroy()
                allPrograms.pack()
                allProgramsListButton.configure(text="Recent Programs")
                if start_full == "1":
                    start_menu.geometry(str(width) + "x" + str(int(height) - 85) + "+" + "0" + "+" + "0")

                    hardwareMonitorButton = Button(row1, text="Hardware Monitor", command=hardwareMonitor, width=20,
                                                   height=10,
                                                   bg=menuColour)
                    musicPlayerButton = Button(row1, text="Music Player - Experimental", command=musicPlayer,
                                               width=20,
                                               height=10, bg=menuColour)
                    infoButton = Button(row1, text="Glass OS Info Panel", command=info, width=20,
                                        height=10, bg=menuColour)
                    CustomAppLauncherButton = Button(row1, text="Custom App Launcher", command=cal, width=20,
                                                     height=10,
                                                     bg=menuColour)
                    terminalButton = Button(row1, text="Terminal", command=terminal, width=20,
                                            height=10, bg=menuColour)
                    restartButton = Button(row1, text="Restart", command=restart, width=20,
                                           height=10, bg=menuColour)
                    jpadButton = Button(row2, text="Jpad", command=jpadEditor, width=20,
                                        height=10, bg=menuColour)
                    chkUpdates = Button(row2, text="Check for Updates", command=update_check, width=20,
                                        height=10,
                                        bg=menuColour)
                    settingsButton = Button(row2, text="Settings", command=settings, width=20,
                                            height=10, bg=menuColour)
                    fileExplorer = Button(row2, text="File Explorer", command=file_Explorer, width=20,
                                          height=10,
                                          bg=menuColour)
                    shutdown = Button(row2, text="Shutdown", command=glass_quit, width=20,
                                      height=10, bg=menuColour)

                    row0.pack()
                    row1.pack()
                    row2.pack()
                    row3.pack()
                    musicPlayerButton.pack(side=LEFT)
                    jpadButton.pack(side=LEFT)
                    chkUpdates.pack(side=LEFT)
                    CustomAppLauncherButton.pack(side=LEFT)
                    fileExplorer.pack(side=LEFT)
                    infoButton.pack(side=LEFT)
                    hardwareMonitorButton.pack(side=LEFT)
                    settingsButton.pack(side=LEFT)
                    terminalButton.pack(side=LEFT)
                    restartButton.pack(side=LEFT)
                    shutdown.pack(side=LEFT)
                else:
                    start_menu.geometry("242x400" + "+" + str(root_windowX) + "+" + str(root_windowY - 455))

                    hardwareMonitorButton = Button(allPrograms, text="Hardware Monitor", command=hardwareMonitor,
                                                   width=100,
                                                   bg=menuColour)
                    musicPlayerButton = Button(allPrograms, text="Music Player - Experimental", command=musicPlayer,
                                               width=100, bg=menuColour)
                    infoButton = Button(allPrograms, text="Glass OS Info Panel", command=info, width=100, bg=menuColour)
                    CustomAppLauncherButton = Button(allPrograms, text="Custom App Launcher", command=cal, width=100,
                                                     bg=menuColour)
                    terminalButton = Button(allPrograms, text="Terminal", command=terminal, width=100, bg=menuColour)
                    restartButton = Button(allPrograms, text="Restart", command=restart, width=100, bg=menuColour)
                    jpadButton = Button(allPrograms, text="Jpad", command=jpadEditor, width=100, bg=menuColour)
                    chkUpdates = Button(allPrograms, text="Check for Updates", command=update_check, width=100,
                                        bg=menuColour)
                    settingsButton = Button(allPrograms, text="Settings", command=settings, width=100, bg=menuColour)
                    fileExplorer = Button(allPrograms, text="File Explorer", command=file_Explorer, width=100,
                                          bg=menuColour)
                    shutdown = Button(allPrograms, text="Shutdown", command=glass_quit, width=100, bg=menuColour)

                    musicPlayerButton.pack()
                    jpadButton.pack()
                    chkUpdates.pack()
                    CustomAppLauncherButton.pack()
                    fileExplorer.pack()
                    infoButton.pack()
                    hardwareMonitorButton.pack()
                    settingsButton.pack()
                    terminalButton.pack()
                    restartButton.pack()
                    shutdown.pack()

                showAllOpen = 1
            else:
                global start_open
                showAllOpen = 0
                start_open = 0
                start_menu.destroy()
                start()

        shutdown = Button(start_menu, text="Shutdown", command=glass_quit, width=100, bg=menuColour)
        shutdown.pack(side=BOTTOM)

        allProgramsListButton = Button(start_menu, text="All Programs", command=showAll, width=100, bg=menuColour)
        allProgramsListButton.pack(side=BOTTOM)

        # musicPlayerButton.pack()
        # jpadButton.pack()
        # chkUpdates.pack()
        # CustomAppLauncherButton.pack()
        # fileExplorer.pack()
        # infoButton.pack()
        # settingsButton.pack()
        # terminalButton.pack()
        # restartButton.pack()
        # shutdown.pack()
        start_open = 1

        start_menu.mainloop()
    if start_open == 1:
        try:
            start_menu.destroy()
            start_open = 0
        except:
            start_open = 0


clicked = 0


def reposition(self):
    global centerWidth
    global centerHeight
    global screenCenter
    global root_windowX
    global root_windowY
    global notifcationBar
    global start_menu
    global cTime

    cHeight = root_window.winfo_height()
    cWidth = root_window.winfo_width()
    
    centerWidth = root_window.winfo_x() + int(int(cWidth) / 2)
    centerHeight = root_window.winfo_y() + int(int(cHeight) / 2)

    screenCenter = str(centerWidth) + "+" + str(centerHeight)

    startPic.place_configure(x=int(0), y=int(cHeight) - 55)

    search.place_configure(x=57, y=int(cHeight) - 55, height=55, width=200)

    # versionText.place(x=int(cWidth) - 300, y=int(cHeight) - 120)

    toolbar.place_configure(x=258, y=int(cHeight) - 55, height=55, width=int(cWidth))

    notifcationBar.place_configure(x=int(cWidth) - 500, y=int(cHeight) - 55, height=55, width=500)

    root_windowX = root_window.winfo_x()
    root_windowY = (root_window.winfo_y() + root_window.winfo_height())

    try:
        start_menu.geometry("242x260" + "+" + str(root_windowX) + "+" + str(root_windowY - 315))
        start_menu.focus()
    except:
        pass

        # displayTime.pack_configure(side=RIGHT)


max = 0


def fullScreen(self):
    global max
    if max == 0:
        root_window.attributes('-fullscreen', True)
        max = 1
    else:
        root_window.attributes('-fullscreen', False)
        max = 0


def interface():
    global notifcationBar
    global time1
    global cTime
    global displayTime
    global menuColour
    global max
    global toolbar
    global versionText
    global startPic
    global root_window
    global canvas
    try:
        root_window.destroy()
    except:
        pass
    global search
    global start
    global searchvar
    global root_window
    global root_windowX
    global root_windowY
    global fileImage
    global background_image
    root_window = Tk()
    root_window.title("GlassOS      " + "Version: " + version + "      Username: " + active)
    root_window.geometry(widthHeight)
    root_window.minsize(minWidth, minHeight)

    root_windowX = root_window.winfo_x()
    root_windowY = root_window.winfo_y()

    # root_window.wm_iconbitmap("System/JordonOS Logo.ico")


    # TODO: Find a way to resize the desktop background
    canvas = Canvas(root_window, width=width, height=height)
    background_image = PhotoImage(file=background)
    canvas.create_image(0, 0, image=background_image, anchor=NW)
    canvas.pack(expand=YES, fill=BOTH)
    
    start_image = PhotoImage(file=startMenuPic)

    startPic = Button(root_window, image=start_image, command=start, bg=menuColour)
    startPic.place(x=int(0), y=int(height))

    root_window.attributes('-fullscreen', True)
    max = 1

    # root_window.configure(bg="#39d972")

    fileImage = PhotoImage(file="GlassOS/file.png")

    def desktopRefresh():
        f = []
        l = []
        fName = []
        place = []
        files = -1
        space = 80

        prefix = user_dir

        # prefix = os.path.expanduser("~")
        def openFile(self):
            # print(fName)
            fileURL = prefix + "/Desktop/" + str(fName[files])
            # print(fileURL)
            jpadEditor(fileURL)

        def openFolder(self):
            folderURL = prefix + "/Desktop/" + str(fName[files])
            file_Explorer(folderURL)

        # for file in fName:
        #     if os.path.exists(prefix + "/Desktop/" + file):
        #         pass
        #     else:
        #         try:
        #             l[files].destroy()
        #             f = []
        #             l = []
        #             fName = []
        #             place = []
        #             files = -1
        #
        #         except:
        #             pass

        try:
            for file in os.listdir(prefix + "/Desktop"):
                if file not in fName:
                    l.append(Label(root_window, text=file, font=("Arial", 11, "bold")))

                    files += 1

                    fName.append(file)
                    place.append(files)

                    space += 80

                    f.append(Button(root_window, image=fileImage))

                    f[files].place(x=int(80), y=int(20) + space, width=40, height=40)

                    if ".txt" in file:
                        f[files].bind("<Double-Button-1>", openFile)
                    elif ".py" in file:
                        f[files].bind("<Double-Button-1>", openFile)
                    elif ".pyw" in file:
                        f[files].bind("<Double-Button-1>", openFile)
                    elif os.path.isdir(prefix + "/Desktop/" + file):
                        f[files].bind("<Double-Button-1>", openFolder)
                    else:
                        pass
                    l[files].place(x=int(100), y=int(70) + space, anchor=CENTER)
        except:
            pass

    def refresh(self):
        desktopRefresh()

    desktopRefresh()

    root_window.bind("<F5>", refresh)

    root_window.bind("<Escape>", fullScreen)
    root_window.bind("<Configure>", reposition)
	
    contextMenu = Menu(root_window, tearoff=0)
	
    contextMenu.add_command(label="Refresh", command=desktopRefresh)
    contextMenu.add_command(label="Jpad", command=jpadEditor)
    contextMenu.add_command(label="Terminal", command=terminal)
    contextMenu.add_command(label="Settings", command=settings)
	
    def contextMenuPopup(event):
        contextMenu.post(event.x_root, event.y_root)

    root_window.bind("<Button-3>", contextMenuPopup)

    searchText = Label(root_window, text="Search for: ")
    searchvar = StringVar()
    search = Entry(root_window, textvariable=searchvar, font=(14), bg=menuColour)
    search.bind("<Button-1>", box)
    search.bind("<Return>", search_internet)
    search.place(x=57, y=350, height=50, width=100)
    search.insert(0, "Search")

    def updChk():
        def run():
            update_check(1)

        def done():
            update_check(0)

        updIcon = Button(notifcationBar, text="!")
        updIcon.pack(side=RIGHT)
        try:
            testfile = requests.get("https://raw.githubusercontent.com/Jordonbc/GlassOS/master/updater.txt")
        except:
            pass
        try:
            updateVerFile = open("updater.txt", "r")
            updateVer = updateVerFile.read()

            if int(updateVer) >= int(version) + 2:
                updIcon.configure(bg="#ff0000", command=run)
            elif int(updateVer) == int(version) + 1:
                updIcon.configure(bg="#FF6600", command=run)
            elif int(updateVer) <= int(version):
                updIcon.configure(bg="#00ff00", command=done)
        except:
            pass

    # versionText = Label(root_window, text="Glass OS build " + version,
    # font=("Arial", 20))
    # versionText.place(x=int(width) - 300, y=int(height) - 120)
    def clockTick():
        desktopRefresh()
        global time1
        # cTime = time.strftime("%H:%M:%S")
        # print(cTime)
        cTime = time.strftime("%H:%M")
        if cTime != time1:
            time1 = cTime
            displayTime.configure(text=cTime)
            displayTime.after(1000, clockTick)
        else:
            displayTime.after(1000, clockTick)

    toolbar = Frame(root_window, bg=menuColour)
    toolbar.place(x=0, y=int(height) - 55)

    notifcationBar = Frame(root_window, bg=menuColour)
    notifcationBar.place(x=int(width) - 100, y=int(height) - 55)

    cTime = time.strftime("%H:%M")

    displayTime = Label(notifcationBar, text=cTime, bg=menuColour, font=("System", 20))

    displayTime.pack(side=RIGHT)

    updChk()

    time1 = ""

    clockTick()

    root_window.mainloop()