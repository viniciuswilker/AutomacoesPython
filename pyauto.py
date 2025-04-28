import pyautogui as pa
from time import sleep


pa.press('win')
pa.write('cmd')
sleep(2)

pa.press('enter')
sleep(2)
pa.write('ipconfig')
sleep(2)
pa.press('enter')