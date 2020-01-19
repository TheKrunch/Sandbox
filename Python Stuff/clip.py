import os, time, subprocess
from datetime import datetime
from pathlib import Path


def getNewestFilePath(pathToDir):                               # This gets the news file in the path specified
    with os.scandir(pathToDir) as pathDir:
        newestFile = ''                                         # Where the newest file path will be stored
        tempTime = 0                                            # Where the current newests file's time since the epoch is stored

        for file in pathDir:
            if file.is_file():
                curFile = os.stat(file)                         # Gets stats about the file and stores it in curFile
                creatTime = curFile.st_ctime                    # Gets how much times since the epoch it was when the file was created and stores it in creatTime

                if creatTime > tempTime:
                    newestFile = file.path
                    tempTime = creatTime

    if newestFile == '' and pathToDir == Path.cwd():
        raise Exception("No files found in current working directory, please use specify a directory with media files.")
    elif newestFile == '':
        print("No files found in specified path, using curent working directory instead...\n")
        return getNewestFilePath(Path.cwd())
    else:
        return Path(newestFile)                                 # Turns the path string into a Path object


def getFileDuration(pathToFile):
    filePath = str(pathToFile)
    # This is the command to find the duration, it uses ffprobe which needs to be installed seperately
    args = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filePath]
    
    ffprobeProc = subprocess.run(args, stdout=subprocess.PIPE)  # This runs the command in args.
    
    if ffprobeProc.returncode > 0:
        raise Exception("File found is not recognized by ffprobe, please only use directories media files.")
    else:
        # This converts the output to a float instead of a string
        clipDur = float(ffprobeProc.stdout.decode('utf-8').strip())

        return clipDur


dirToScan = Path("E:/Game Highlights/OBS Recordings")           # This converts the string to the directory into a Path Object
 
dirToSave = Path("E:\Music\Soundboard Sounds\Python Clips")

print("Scanning \"{}\" for newest file...".format(dirToScan))

print("")
print("Path to newest file:")

newPath = getNewestFilePath(dirToScan)                          # Sets newPath = to the path object generated by getNewestFilePath()
print("\"{}\"".format(newPath), "\n")

clipSecs = getFileDuration(newPath)                             # Sets clipSecs = to the duration of the clip in seconds
# This prints the output from the above command.
print("The duration of \"{}{}\" is: {} seconds".format(newPath.stem, newPath.suffix, clipSecs))



# The ffmpeg command to encode to audio will look something like this
# ffmpeg -ss (DURATION - ELAPSED) -t ELAPSED -i FILENAMEHERE OUTPUTFILENAME
# this took about .326s according to the Ubuntu time command, so the bottle neck now is the obs file save time...(~1.8 seconds)

# After the file probe get the output duration in seconds,
# Using calculated elapsed time and duration of clip, (btw read "Clip audio script idea.txt")
# Encode selected time into audio file and save to soundboard folder
# As for keyboard inturupt looks like there is a python module called "keyboard" by boppreh on github, that does exactly what I want.
# :$
