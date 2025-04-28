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
        botao_dropdown = self.driver.find_element(By.ID, 'dropdownMenuButton')

        if botao_dropdown is not None:
            print('botao encontrado')
        if botao_dropdown is None:
            print('botao não encontrado')
            
curso = CursoAutomacao()
curso.Iniciar()
