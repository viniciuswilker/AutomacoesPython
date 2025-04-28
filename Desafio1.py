from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Automacao():
    def __init__(self):
        
        service = Service(executable_path=r'./chromedriver.exe')
        options = Options()
        options.add_argument('--lang=pt-BR')

        self.driver = webdriver.Chrome(service=service, options=options)

    def Inicia(self):
        
        self.driver.get('https://cursoautomacao.netlify.app')

        link = self.driver.find_element(By.LINK_TEXT, 'Desafios')
        link.click()


        btn1 = self.driver.find_element(By.ID, 'btn1')
        print('ACHEI BTN 1')if btn1 is not None else 'Não achei'
        print('BTN ATIVO') if btn1.is_enabled() else 'BTN DESATIVADO'


        btn2 = self.driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark')
        print('ACHEI BTN 2') if btn2 is not None else 'Não achei'
        print('BTN ATIVO') if btn2.is_enabled() else 'BTN DESATIVADO'

        btn3 = self.driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')
        print('ACHEI BTN 3') if btn3 is not None else 'Não achei'
        print('BTN ATIVO') if btn3.is_enabled() else 'BTN DESATIVADO'



auto = Automacao()
auto.Inicia()