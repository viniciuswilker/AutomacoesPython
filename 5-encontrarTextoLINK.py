from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class Automacao():
    def __init__(self):
        
        service = Service(executable_path=r'./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app')
        # link = self.driver.find_element(By.LINK_TEXT, 'Desafios')
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Desaf')


        if link is not None:
            print("ACHEI O LINK")
        else:
            print("NAO ACHEI")



auto = Automacao()
auto.Iniciar()