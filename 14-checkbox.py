from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class CursoAutomacao():
    def __init__(self):
        service = Service(executable_path='./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app')
        btn1 = self.driver.find_element(By.ID, 'acessoNivel1Checkbox')
        btn2 = self.driver.find_element(By.ID, 'acessoNivel2Checkbox')

        btn1.click()
        btn2.click()


        sleep(5)
curso = CursoAutomacao()
curso.Iniciar()
