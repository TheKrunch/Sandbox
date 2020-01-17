import os, time, subprocess
from datetime import datetime
from pathlib import Path


dirToScan = "E:/Game Highlights/OBS Recordings" # This is the directory I want to scan
p = Path(dirToScan)                             # This converts the string to the directory into a Path Object

print("This should print the file name and the date & time of creation for all the files in:", p, end='\n\n')

with os.scandir(p) as curDir:                   # Creates an iterator for the specified directory in p
    for f in curDir:
        if f.is_file():                         # Checks if its a file
            curF = os.stat(f)                   # Saves the stat_result object into curF, this allows us to get file info
            print(f.name, end=': ')             # Prints the current file's name
            convTime = datetime.fromtimestamp(curF.st_ctime)       # This gets the ctime of the current file and formats it
            print(convTime.strftime("%m/%d/%Y, %H:%M:%S"))         # This formats it again, not really sure why it has to be done twice


def getNewestFilePath():
    with os.scandir(p) as pathDir:
        newestFile = ''     # Where the newest file path will be stored
        tempTime = 0        # Where the current newests file's time since the epoch is stored

        for file in pathDir:
            if file.is_file():
                curFile = os.stat(file)             # Gets stats about the file and stores it in curFile
                creatTime = curFile.st_ctime        # Gets how much times since the epoch it was when the file was created and stores it in creatTime

                if creatTime > tempTime:
                    newestFile = file.path
                    tempTime = creatTime
        
    return newestFile

print("")
print("This should print the path to the newest file.\n")
newPath = Path(getNewestFilePath())
print(newPath)

# The following line should be run with subprocess.Popen() (or subprocess.run() not sure), it returns the duration of the clip in seconds.
# ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "FILENAMEHERE"
# FILENAMEHERE can also be a path to the file, or just the file name itself, depending on where script is executing.

#args = ['ffprobe', '-v', 'error' , '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '"FILENAMEHERE"']
#ffprobeProc = subprocess.run(args, stdout=subprocess.PIPE)

# After the file probe get the output duration in seconds using subprocess.*() stuff,
# Using calculated elapsed time and duration of clip, (btw read "Clip audio script idea.txt")
# Encode selected time into audio file and save to soundboard folder
# :$

# The ffmpeg command to encode to audio will look something like this
# ffmpeg -ss (DURATION - ELAPSED) -t ELAPSED -i FILENAMEHERE OUTPUTFILENAME
# this took about .326s according to the Ubuntu time command, so the bottle neck now is the obs file save time...

# As for keyboard inturupt looks like there is a python module called "keyboard" by boppreh on github, that does exactly what I want.
