from automa.api import *
from os.path import expanduser, exists, join, pardir, getsize
import unittest
import time
 
class TestAutomaWebsite(unittest.TestCase):
    def testAddUser(self):
        switch_to("Internet Explorer")
        for i in range(1000,1010):
            scroll_up(steps=10)
            click(Point(2200,550))
            time.sleep(2)
            scroll_up(steps=10)
            click(Point(1000,720))
            write(i)
            press(TAB)
            write(i)
            press(TAB)
            press(TAB)
            press(TAB)
            write(i)
            press(TAB)
            press(TAB)
            press(TAB)
            press(TAB)
            write("{}{}".format(i,i))
            press(TAB)
            write("{}{}".format(i,i))
            press(TAB)
            write(i)
            press(TAB)
            write(i)
            press(TAB)
            press(TAB)
            write(i)
            scroll_down(steps=10)
            click(Point(650,1300))
            time.sleep(4)

if __name__ == '__main__':
    unittest.main()