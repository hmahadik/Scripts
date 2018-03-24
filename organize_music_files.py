import os
import eyed3
import shutil

for filename in os.listdir(os.curdir):

	# make sure it's a file
	if os.path.isfile(filename):

		print "Loading file {}".format(filename)
		id3File = eyed3.load(filename)
		if id3File is None:
			print "Unable to load file: {}".format(filename)
		else:
			genre = id3File.tag.genre.name

			if not os.path.exists(genre):
				print "Creating folder {}".format(genre)
				os.makedirs(genre)

			shutil.move(filename, os.path.join(genre, filename))
			print "{} moved into {}".format(filename, genre)