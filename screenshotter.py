#!/usr/bin/env python3
try:
    from PIL import ImageGrab as ScreenshotGrabber
except:
    import pyscreenshot as ScreenshotGrabber

import datetime
import time
import os
import traceback

rootDir = os.path.expanduser("~/Developer/Screenshots")
os.makedirs(rootDir, exist_ok=True)
os.chdir(rootDir)

while True:
  try:
    image = ScreenshotGrabber.grab()
    image = image.convert("RGB")
    now = datetime.datetime.now()
    folder = os.path.join(f"{now.year}", f"{now:%b}", f"{now:%d}-{now:%a}")
    os.makedirs(folder, exist_ok=True)
    filename = f'{now:%I}-{now:%M}{now:%p}.jpg'
    filepath = os.path.abspath(os.path.join(folder, filename))
    image.save(filepath, quality=25)
    print(f"[{str(datetime.datetime.now())}] Saved {filepath}")
  except:
    print(f"[{str(datetime.datetime.now())}] Exception: {traceback.format_exc()}")
  finally:
    time.sleep(60)
