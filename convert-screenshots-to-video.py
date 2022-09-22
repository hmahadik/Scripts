import sys, cv2, os, pathlib, time, tqdm

try:
	root = pathlib.Path(sys.argv[1])

except:
	print("Usage: python3 convert-screenshots-to-video.py <folder>")
	print("Example: python3 convert-screenshots-to-video.py /home/harshad/Developer/Screenshots/")
	sys.exit(0)

def process_folder(folder):

	print(f"Processing folder: {folder}")

	timeStart = time.time()

	try:
		paths = sorted(filter(lambda p: p.suffix == ".jpg", folder.iterdir()), key=os.path.getmtime)

		if not (len(paths) > 0):
			return

		fps, width, height = (30.0, 1920, 1080)
		videoOutputPath = folder.parent.joinpath(f"{folder.name}.mp4")

		if videoOutputPath.exists():
			print(f"Video '{videoOutputPath}' already exists, not overwriting.")
			return

		print(f"Writing video to {videoOutputPath}")

		writer = cv2.VideoWriter(str(videoOutputPath),
			cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

		for path in tqdm.tqdm(paths):
			frame = cv2.resize(cv2.imread(str(path)), (width,height), interpolation=cv2.INTER_AREA)
			writer.write(frame)

	except Exception as e:
		print(e)

	finally:
		try:
			writer.release()
		except:
			pass

	print(f"Video saved as {videoOutputPath}. Took {round((time.time()-timeStart)/60.0, 1)} minutes.")

def process_nested_folders(folder):
	nested_folders = sorted(filter(lambda p: p.is_dir(), folder.iterdir()), key=os.path.getmtime)
	if len(nested_folders) == 0:
		process_folder(folder)
		return

	print(f"Processing nested folder {folder}")
	for nested_folder in nested_folders:
		process_nested_folders(nested_folder)

process_nested_folders(root)