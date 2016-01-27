import shutil
import zipfile
from tkinter import *
import os

def chkState():
    f = open("state", "r")
    state = f.read().replace(" ", "")
    f.close()

    if state == "1":
        f = open("state", "w")
        f.write("0")
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
            for file in z.namelist():
                if not file.startswith('Glass_OS/'):
                    pass
                if file.startswith("GlassOS-master/GlassOS-master/") and os.path.isdir(file):
                    try:
                        os.makedirs("../"+str(file).replace("GlassOS-master/GlassOS-master/", ""))
                        print("Created: "+str(file).replace("GlassOS-master/GlassOS-master/", ""))
                    except:
                        pass
                if file.startswith("GlassOS-master/GlassOS-master/") and not os.path.isdir(file):
                    z.extract(file, path="../../../")
                    print("Extracted: "+file)
        print("Done!")

        f = open("state", "w")
        f.write("1")
        f.close()

        if os.path.exists("updater.txt"):
            os.remove("updater.txt")
        if os.path.exists("update.zip"):
            #os.rename("update.zip", "../update.zip") for testing purposes
            os.remove("update.zip")

        updateprogram.destroy()
        updateprogram.mainloop()

def reset():
    if os.path.exists("reset"):
        os.remove("reset")

        newFile = open("GlassOS/System/newOS", "w")
        newFile.close()

        #shutil.rmtree(user_dir)
        #os.remove(users + username + ".profile")

        os.system("python run.pyw")
    else:
        pass

chkUpdate()

sys.path.insert(0, "System")
from GlassOS.System.glass import *

interface()

reset()
chkState()