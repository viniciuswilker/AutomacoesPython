from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class CursoAutomacao():
    def __init__(self):
        service = Service(executable_path='./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(service=service, options=options)

        self.site = input('Em qual site deseja ir?')

    def Iniciar(self):
        self.driver.get(self.site)
        

curso = CursoAutomacao()
curso.Iniciar()
