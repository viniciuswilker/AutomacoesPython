from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CursoAutomacao:
    def __init__(self):
        service = Service(executable_path=r'./chromedriver.exe')
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    def Iniciar(self):
        self.driver.get('https://www.youtube.com')
        
        
curso = CursoAutomacao()
curso.Iniciar()