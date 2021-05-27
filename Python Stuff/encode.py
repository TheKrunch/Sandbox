import os, subprocess
from pathlib import Path

 # Converts string to a path object
inputDir = Path("E:/Game Highlights/OBSRaw")
outputDir = Path("E:/Game Highlights/OBSEncoded")

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



with os.scandir(inputDir) as direc:
	for file in direc:
		if file.is_file():
			inPath = Path(file.path)
			print("Encoding: \"{}\"".format(inPath))

			args = ['ffmpeg', '-n', '-i', str(inPath), '-vcodec' , 'libx265', '-crf', '26', (str(outputDir) + "\\" + inPath.stem + 'ENCODED.mp4')]
			ffmpegProc = subprocess.run(args, capture_output=True)
			print("Finished encoding \"{}\", continuing...".format(inPath))

print("Finished.")
			
