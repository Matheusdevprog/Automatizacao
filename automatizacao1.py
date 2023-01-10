import time
import pyautogui as pt
import pyperclip as pc

pt.press("win")
time.sleep(1)
pt.write("chorme")
time.sleep(2)
pt.press("enter")

time.sleep(4)

print(pt.position())
pt.click(x=683, y=506)
time.sleep(3)
pt.click(x=172, y=311)
time.sleep(3)
pt.click(x=501, y=231)
time.sleep(1)
pt.click(x=436, y=248)
time.sleep(3)
pt.click(x=1027, y=279)
