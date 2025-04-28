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
        btnLogin = self.driver.find_element(By.LINK_TEXT, "Login")
        btnLogin.click()
        sleep(2)        

        campo_email = self.driver.find_element(By.ID, "email")
        print('clicado no email') if campo_email.click() else 'naoooo '
        sleep(2) 

        campo_email.send_keys('joao@joao.com')
        sleep(1)

        campo_senha = self.driver.find_element(By.ID, "senha")
        campo_senha.click()
        sleep(1)
        campo_senha.send_keys('******')

        btnEnviar = self.driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
        sleep(2)
        btnEnviar.click()
        sleep(3)




curso = CursoAutomacao()
curso.Iniciar()
