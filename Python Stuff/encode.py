import os, subprocess, time
from pathlib import Path
from datetime import datetime, timedelta

 # Converts string to a path object
inputDir = Path("\\\\Gimli\\g\\Game Highlights\\CSGO Highlights\\To Encode")
outputDir = Path("\\\\Gimli\\g\\Game Highlights\\CSGO Highlights\\To Encode\\Encoded")

if not inputDir.is_dir():
    print("Input directory can't be found, will try current working directory...")
    inputDir = os.getcdw()

if not outputDir.is_dir():
    print("Output directory can't be found, will be created in \"{}\".".format(inputDir))
    outputDir = os.path.join(inputDir, "OBSEncoded")
    try:
        os.mkdir(outputDir)
    except FileExistsError:
        print("Output directory already exists in \"{}\", continuing...".format(inputDir))


startTime = 0

with os.scandir(inputDir) as direc:
    for file in direc:
        if file.is_file():
            inPath = Path(file.path)
            print("Encoding: \"{}\"".format(inPath))
            print("Start time is: " , datetime.now().strftime("%H:%M:%S"))
            
            #args = ['ffmpeg', '-n', '-i', str(inPath), '-vcodec' , 'libx265', '-crf', '26', '-preset', 'fast' (str(outputDir) + "\\" + inPath.stem + 'ENCODED.mp4')]
            args = ['ffmpeg', '-n', '-i', str(inPath), '-c:v' , 'libx264', '-crf', '21', '-c:a', 'aac', (str(outputDir) + "\\" + inPath.stem + 'ENCODED.mp4')]
            startTime = time.time()
            ffmpegProc = subprocess.run(args, capture_output=True)
            print("Finished encoding \"{}\", continuing...".format(inPath))
            print("Encode took: " , timedelta(seconds=(time.time() - startTime)))

print("Finished.")
print("Finish time is: " + datetime.now().strftime("%H:%M:%S"))
