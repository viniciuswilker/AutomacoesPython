from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Automacao():
    def __init__(self):
        
        service = Service(executable_path=r'./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    def Iniciar(self):
        
        self.driver.get('https://cursoautomacao.netlify.app')
        
        btnDesafio = self.driver.find_element(By.LINK_TEXT, 'Desafios')
        sleep(1)
        btnDesafio.click()

        sleep(2)
        campo_texto = self.driver.find_element(By.ID, 'dadosusuario')
        campo_texto.click()

        sleep(2)
        campo_texto.send_keys('AAAAAAAAA')
        sleep(2)

        btnEnviar = self.driver.find_element(By.ID, 'desafio2')
        btnEnviar.click()

        sleep(6)

        inputEscondido = self.driver.find_element(By.ID,'escondido')
        inputEscondido.click()

        inputEscondido.send_keys('Vinicius')

        sleep(2)

        btnEscondido = self.driver.find_element(By.ID, 'validarDesafio2')
        btnEscondido.click()

        sleep(10)



auto = Automacao()
auto.Iniciar()