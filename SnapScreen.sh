#! /usr/bin/env bash

File_Path=/root/Desktop/Screenshots

echo $File_Path

#!/bin/bash
ans=$(zenity  --list  --text "Change Filepath?" --radiolist  --column "Pick" --column "" TRUE "Yes" FALSE "No"); 
if [ $ans == "Yes" ]; then
   New_File_Path=$(zenity --entry --text "Enter New Filepath" --entry-text ""); echo $New_File_Path
   File_Name=$(zenity --entry --text "Enter Filename" --entry-text "");  echo $File_Name
elif [ $ans == "No" ]; then
   File_Name=$(zenity --entry --text "Enter Filename" --entry-text "");
else
   zenity --error --text "Error"
fi

if [ -z ${New_File_Path+x} ]; then
   xfce4-screenshooter -r -s $File_Path/$File_Name;
else 
   xfce4-screenshooter -r -s $New_File_Path/$File_Name
fi

