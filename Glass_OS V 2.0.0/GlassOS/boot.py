import shutil
import zipfile
from tkinter import *
import os

def chkState():
    f = open("state", "r")
    state = f.read().replace(" ", "")
    f.close()

    if state == "1":
        f = open("state", "w").write("0")
        os.system("python run.pyw")
    else:
        quit()

def chkUpdate():
    if os.path.exists("update.zip"):
        updateprogram = Tk()
        updateprogram.geometry("800x600")

        text = Label(updateprogram, text="Updating Glass OS Please wait...")

        text.pack()

        print("Extracting...")
        with zipfile.ZipFile('update.zip', "r") as z:
            z.extractall("../")
        print("Done!")

        f = open("state", "w")
        f.write("1")
        f.close()

        os.remove("updater.txt")
        os.remove("update.zip")

        updateprogram.destroy()

        chkState()

        updateprogram.mainloop()

def reset():
    if os.path.exists("reset"):
        os.remove("reset")

        newFile = open("GlassOS/System/newOS", "w")
        newFile.close()

        shutil.rmtree(user_dir)
        os.remove(users + username + ".profile")

        os.system("python run.pyw")
    else:
        pass

chkUpdate()

sys.path.insert(0, "System")
from GlassOS.System.glass import *

interface()

reset()
chkState()