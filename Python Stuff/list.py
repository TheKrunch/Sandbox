import os, time, datetime

#print("Using os.listdir() I get a list of strings of the files in the current directory.\n")
#time.sleep(1)
#dirlist = os.listdir()							# Creates a list of the files in the current directory as strings
#print(dirlist, end='\n\n')

print("Looping through current directory file names with os.scandir().\n")
time.sleep(1)

with os.scandir() as curDir:					# os.scandir() makes an iterator of the files in the current directory
	for entry in curDir:
		if entry.is_file():						# Checks if the current object is a file
			print(entry.name)					# If so it prints its file name

print("\nOkay, now this should print the file name and date & time of file creation...\n")

time.sleep(1)

with os.scandir() as curDir:					# Same as above creates the iterator
	for f in curDir:
		if f.is_file():							# Checks if its a file
			curF = os.stat(f)					# Saves the stat_result object into curF, this allows us to get file info
			print(f.name, end=': ')				# Prints the current file's name
			convTime = datetime.datetime.fromtimestamp(curF.st_ctime)		# This gets the ctime of the current file and formats it
			print(convTime.strftime("%m/%d/%Y, %H:%M:%S"))					# This formats it again, not really sure why it has to be done twice

print("\nUp until this point I was using default parameter for path, now trying 'E:\\Game Highlights\\OBS Recordings' as path.")

time.sleep(1)

with os.scandir('E:\\Game Highlights\\OBS Recordings') as pathDir:
	for f in pathDir:
		if f.is_file():
			curF = os.stat(f)
			print(f.name, end='\n')

# The following line should be run with subprocess.Popen() (or subprocess.run() not sure), it returns the duration of the clip in seconds.
# ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "FILENAMEHERE"
# FILENAMEHERE can also be a path to the file, or just the file name itself, depending on where script is executing.

# After the file probe get the output duration in seconds using subprocess.*() stuff,
# Using calculated elapsed time and duration of clip, (btw read "Clip audio script idea.txt")
# Encode selected time into audio file and save to soundboard folder
# :$

# The ffmpeg command to encode to audio will look something like this
# ffmpeg -ss (DURATION - ELAPSED) -t ELAPSED -i FILENAMEHERE OUTPUTFILENAME
# this took about .326s according to the Ubuntu time command, so the bottle neck now is the obs file save time...

# As for keyboard inturupt looks like there is a python module called "keyboard" by boppreh on github, that does exactly what I want.
