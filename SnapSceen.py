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


# Change this to your Desired Filepath or you can change it on the fly
file_path = "/root/Desktop/Screenshots"
new_file_path = ""
file_name = ""


class color:
    MAG = '\033[35m'
    BOLD = '\033[1m'
    END = '\033[0m'


# check for GUI program
def zenity():
    zen_check = subprocess.check_output(['which', 'zenity'], stderr=subprocess.STDOUT)
    zen = color.BOLD + color.MAG + "Please sudo apt-get install zenity" + color.END
    if zen_check != 0:
        pass
    else:
        print("Error: " + "Zenity is Required for this script.")
        print(zen)

# Offers a chance to change the filepath
def check_path():
    ans=subprocess.call(["zenity", "--question", "--text=Current Filepath: " + "\n" + "\n" +  file_path + "\n" + "\n" +"Do you want to change the Filepath?", "--width=250"])
    if ans == 0:
        global new_file_path
        new_path = subprocess.Popen(["zenity", "--entry", "--text=Enter New Filepath", "--entry-text="""], stdout=subprocess.PIPE, universal_newlines=True)
        new_file_path = new_path.stdout.read().strip()
    elif ans == 1:
        pass
    else:
        subprocess.call(["zenity", "--error", "--text='Error'"])


# Enter the filename
def enter_name():
    global file_name
    get_file_name = subprocess.Popen(["zenity", "--entry", "--text=Enter Filename", "--entry-text="""], stdout=subprocess.PIPE, universal_newlines=True)
    file_name = get_file_name.stdout.read().strip()


# take the screenshot and save
def snap():
    final_nochange = str(file_path) + "/" + str(file_name)
    final_newpath = str(new_file_path) + "/" + str(file_name)
    if new_file_path == "":
        subprocess.call(["xfce4-screenshooter", "-r", "-s", final_nochange], stderr=subprocess.STDOUT)
    else:
        subprocess.call(["xfce4-screenshooter", "-r", "-s", final_newpath], stderr=subprocess.STDOUT)

     
def main():
    zenity()
    check_path()
    enter_name()
    snap()
    

main()
