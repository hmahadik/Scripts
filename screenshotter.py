#!/usr/bin/python3
try:
    from PIL import ImageGrab as ScreenshotGrabber
except:
    import pyscreenshot as ScreenshotGrabber
import datetime
import time
import os

os.chdir(os.path.expanduser("~/Developer/Screenshots"))

while True:
  try:
    image = ScreenshotGrabber.grab()
    filename = f'{str(datetime.datetime.now()).replace(":","-")}.jpg'
    image.save(filename, quality=25)
    print(f"[{str(datetime.datetime.now())}] Saved {filename}")
  except:
  	print(f"[{str(datetime.datetime.now())}] Exception")
  	import traceback
  	traceback.format_exc()
  finally:
  	time.sleep(60)
