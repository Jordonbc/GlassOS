from distutils.core import setup
import py2exe

from glob import *
#import os.path

# def directory_listing_recursive(path):
    # files = []
    # for item in glob.glob(path + '/*'):
        # if os.path.isdir(item):
            # files.append([item, directory_listing_recursive(item)])
        # else:
            # files.append(item)
    # return files

# print(directory_listing_recursive(os.path.realpath('Glass_OS')))]


# [[Folder, [File]],[Folder, [File]]]
dataFiles = [
            ["",["state"]],
            ["Users",["Users/Background.png"]],
            ["GlassOS", ["GlassOS/boot.py",
                         "GlassOS/file.png",
                         "GlassOS/Glass_OS_Logo.png",
                         "GlassOS/Recent",
                         "GlassOS/start.png"]],
            ["GlassOS/System", ["GlassOS/System/glass.py",
                         "GlassOS/file.png",
                         "GlassOS/System/settings.settings",
                         "GlassOS/System/version"]],
            ["GlassOS/Cache",[]]
        
            ]
# print(dataFiles)

setup(
    name='Glass OS',
    version='1.5.0',
    packages=['GlassOS.libaries.psutil', 'GlassOS.libaries.requests', 'GlassOS.libaries.requests.packages',
              'GlassOS.libaries.requests.packages.chardet', 'GlassOS.libaries.requests.packages.urllib3',
              'GlassOS.libaries.requests.packages.urllib3.util', 'GlassOS.libaries.requests.packages.urllib3.contrib',
              'GlassOS.libaries.requests.packages.urllib3.packages',
              'GlassOS.libaries.requests.packages.urllib3.packages.ssl_match_hostname'],
    options = {
        'py2exe': {
            'optimize': 2, 
            'bundle_files': 2,
            'includes' : ["tkinter", "urllib", "sys", "platform", "time",
                          "webbrowser", "winsound", "os", "tkinter.ttk", 
                          "tkinter.filedialog", "tkinter.colorchooser"
                          ],
        }
    }, 
    url='https://github.com/Jordonbc/GlassOS',
    license='Open Source',
    author='Jordon Brooks',
    author_email='jordonbc@hotmail.co.uk',
    description='A python Operating Environment',
    windows=['run.pyw'],
    data_files=dataFiles
)
