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
        navbar = self.driver.find_element(By.CLASS_NAME, 'navbar.navbar-expand-md.navbar-light')
        if navbar is not None:
            print('Nav bar encontrado')
        else:
            print('NAV BAR não encontrado')

curso = CursoAutomacao()
curso.Iniciar()
