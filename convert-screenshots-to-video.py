import sys, cv2, os, pathlib, time, tqdm

try:
	root = pathlib.Path(sys.argv[1])

except:
	print("Usage: python3 convert-screenshots-to-video.py <folder>")
	print("Example: python3 convert-screenshots-to-video.py /home/harshad/Developer/Screenshots/2022/Sep/19-Mon")
	sys.exit(0)

timeStart = time.time()

try:
	paths = sorted(filter(lambda p: p.suffix == ".jpg", root.iterdir()), key=os.path.getmtime)

	fps, width, height = (30.0, 1920, 1080)
	videoOutputPath = root.parent.joinpath(f"{root.name}.mp4")

	print(f"Writing video to {videoOutputPath}")

	writer = cv2.VideoWriter(str(videoOutputPath),
		cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

	for path in tqdm.tqdm(paths):
		# print(f"Processing {path}", end="\r")
		frame = cv2.resize(cv2.imread(str(path)), (width,height), interpolation=cv2.INTER_AREA)
		# cv2.imshow("output", frame)
		# keyPressed = cv2.waitKey(1)
		# if keyPressed > 0:
		# 	print("exiting")
		# 	break
		writer.write(frame)

except Exception as e:
	print(e)

finally:
	try:
		writer.release()
	except:
		pass

print(f"Video saved as {videoOutputPath}. Took {round((time.time()-timeStart)/60.0, 1)} minutes.")
