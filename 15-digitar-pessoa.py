from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import random

class CursoAutomacao():
    def __init__(self):
        service = Service(executable_path='./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)
        self.textao = 'aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaa '

    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app')
        campotexto = self.driver.find_element(By.XPATH, '//textarea[@placeholder="digite seu texto aqui"]')
        time.sleep(3)
        campotexto.click()
        time.sleep(2)

        


        self.digite_pessoa(self.textao, campotexto)


    def digite_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(random.randint(1,5) / 30)

curso = CursoAutomacao()
curso.Iniciar()
