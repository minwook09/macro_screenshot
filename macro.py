import pyautogui
import time

time.sleep(20)
for i in range(581):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'blockchain_boook/'+ str(i) +'.png') #path to save
    pyautogui.press('right')