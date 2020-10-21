#! /usr/bin/env bash

#written by fiolet and dauntless311
#a gui tool to help take screenshots faster and more organized
#this script should never require SUID or SUDO privileges.
#Please don't add them :)

#add this to your hotkeys (make sure the script is exceutable)
#Open your settings -> keyboard -> add
#Enter path to script -> assign hot key
#Enjoy!


#Change this to your Desired Filepath
File_Path=/root/Desktop/Screenshots

#!/bin/bash

#check if zenity is installed, and if not prompt to install
PURPLE='\033[1;35m'
NC='\033[0m'
if [ -z $(which zenity) ] ; then
   echo -e "     Zenity is Required for this script.
         Please ${PURPLE}sudo apt-get install zenity${NC}" 
   exit 1
fi

#Offer to change filepath. FALSE is default setting to reduce number of accidental changes
ans=$(zenity  --list  --text "Current Filepath:\n $File_Path \n\nDo you want to\nchange the Filepath?" --radiolist  --column "Pick" --column "" FALSE "Yes" TRUE "No"); 
if [ $ans == "No" ]; then
   File_Name=$(zenity --entry --text "Enter Filename" --entry-text "");

elif [ $ans == "Yes" ]; then
   New_File_Path=$(zenity --entry --text "Enter New Filepath" --entry-text ""); 
   File_Name=$(zenity --entry --text "Enter Filename" --entry-text "");  
else
   zenity --error --text "Error: Please Try Again"
fi

#run screenshooter area selection option and save
if [ -z ${New_File_Path+x} ]; then
   xfce4-screenshooter -r -s $File_Path/$File_Name;
else 
   xfce4-screenshooter -r -s $New_File_Path/$File_Name
fi
