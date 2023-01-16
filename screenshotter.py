#!/usr/bin/python3
try:
    from PIL import ImageGrab as ScreenshotGrabber
except:
    import pyscreenshot as ScreenshotGrabber

import datetime
import time
import os
import traceback
import cv2
import numpy as np

rootDir = os.path.expanduser("~/Developer/Screenshots")
os.makedirs(rootDir, exist_ok=True)
os.chdir(rootDir)

bgsub = cv2.createBackgroundSubtractorMOG2()

while True:
  try:
    image = ScreenshotGrabber.grab()
    fgmask = bgsub.apply(np.asarray(image), 2)
    image = image.convert("RGB")
    # % pixels that have remained the same is less than 90 i.e. at least 10% of all pixels have changed
    is_different_enough = ((100.0*np.count_nonzero(fgmask == 0)/fgmask.nbytes) < 90.0)
    print(f"{(100.0*np.count_nonzero(fgmask == 0)/fgmask.nbytes)}% similarity")
    if is_different_enough:
      now = datetime.datetime.now()
      folder = os.path.join(f"{now.year}", f"{now:%b}", f"{now:%d}-{now:%a}")
      os.makedirs(folder, exist_ok=True)
      filename = f'{now:%H}-{now:%M}-{now:%S}.jpg'
      filepath = os.path.abspath(os.path.join(folder, filename))
      image.save(filepath, quality=25)
      print(f"[{str(datetime.datetime.now())}] Saved {filepath}")
  except:
    print(f"[{str(datetime.datetime.now())}] Exception: {traceback.format_exc()}")
  finally:
    time.sleep(30)
