from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class CursoAutomacao():
    def __init__(self):
        service = Service(executable_path='./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app')
        campo_idade = self.driver.find_element(By.ID,'campoIdade')
        if campo_idade.is_enabled():
            print('Campo habilitade')
        if  campo_idade.is_enabled() == False:
            print('nao habilitado')

curso = CursoAutomacao()
curso.Iniciar()
