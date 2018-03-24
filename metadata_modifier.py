import taglib
import os
import sys

string_to_replace = sys.argv[1]
replace_with = sys.argv[2]

print "Files that may have changed:"
for filename in os.listdir('.'):
    if filename.endswith(".wav"):
        try:
            print "{filename}".format(filename=filename)
            wavFile = taglib.File(filename)
            if 'TITLE' not in wavFile.tags.keys():
                title = filename.replace(string_to_replace, replace_with).replace(".wav", "")
            else:
                title = wavFile.tags['TITLE'][0]
            wavFile.tags['TITLE'] = title.replace(string_to_replace, replace_with)
            wavFile.save()
        except Exception as e:
            print "Exception: {}".format(e)
            pass

