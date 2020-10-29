#! /usr/bin/env python3

# written by fiolet and dauntless311
# a gui tool to help take screenshots faster and more organized
# this script should never require SUID or SUDO privileges.
# Please don't add them :)

# add this to your hotkeys (make sure the script is exceutable)
# Open your settings -> keyboard -> add
# Enter path to script -> assign hot key
# Enjoy!

import os
import subprocess


# Change this to your Desired Filepath
file_path = "/root/Desktop/Screenshots"


class color:
    MAG = '\033[35m'
    BOLD = '\033[1m'
    END = '\033[0m'


zen = color.BOLD + color.MAG + "Please sudo apt-get install zenity" + color.END


def zenity():
    zen_check = subprocess.check_output(['which', 'zenity'], stderr=subprocess.STDOUT)
    if zen_check != 0:
        pass
    else:
        print("Error: " + "Zenity is Required for this script.")
        print(zen)

def call_zenity():
    ans=subprocess.call(["zenity", "--question", "--text=Current Filepath: " + "\n" + "\n" +  file_path + "\n" + "\n" +"Do you want to change the Filepath?", "--width=250"])
    file_name = ""
    new_file_path = ""
    if ans == 1:
        file_name = subprocess.call(["zenity", "--entry", "--text=Enter Filename", "--entry-text="""])
    elif ans == 0:
        new_file_path = subprocess.call(["zenity", "--entry", "--text=Enter New Filepath", "--entry-text="""])
        file_name = subprocess.call(["zenity", "--entry", "--text=Enter Filename", "--entry-text="""])
    else:
        subprocess.call(["zenity", "--error", "--text='Error'"])


def snap():

     
def main():
    zenity()
    call_zenity()


main()
