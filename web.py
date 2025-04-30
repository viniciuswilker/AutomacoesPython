import webbrowser
import pyautogui as pg
from time import sleep
import pyperclip

webbrowser.open('https://cursoautomacao.netlify.app')
sleep(3)

pg.moveTo(1656,777, 1.5)
pg.click()
sleep(1)

pyperclip.copy('AAAAA TESTANDOOOOO0')
pg.hotkey('ctrl' , 'v')


