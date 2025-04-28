from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui as pa

class Automacao():
    def __init__(self):
        
        service = Service(executable_path=r'./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    
    def Iniciar(self):
        
        self.driver.get('https://youtube.com')
        sleep(2)

        inputTexto = self.driver.find_element(By.CLASS_NAME, 'ytSearchboxComponentInput.yt-searchbox-input.title')
        inputTexto.click()
        sleep(2)

        inputTexto.send_keys('Avenged Sevenfold - Nightmare')
        sleep(2)
        pa.press('enter')
        # inputTexto.send_keys(Keys.ENTER)
        sleep(5)

        tituloVideo = self.driver.find_element(By.LINK_TEXT, 'Avenged Sevenfold - Nightmare [Official Music Video]')
        tituloVideo.click()

        sleep(15)


auto = Automacao()
auto.Iniciar()