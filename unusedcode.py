import pyautogui as pg
import time
import random

time.sleep(4)
pg.hotkey("ctrl", "q")
pg.hotkey("ctrl", "alt","d")
pg.moveTo(1530, 1050, 1)
pg.click()
pg.moveTo(percentToPixelX(83.85), percentToPixelY(57.40), 2)
