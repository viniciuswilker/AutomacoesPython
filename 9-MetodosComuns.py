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

    def iniciar(self):
        self.driver.get("https://cursoautomatcao.netlify.com/") # navegar até um site
        self.driver.maximize_window() # maximizar a janela
        self.driver.refresh() # recarrega página atual
        self.driver.get(self.driver.current_url) # recarrega página atual
        self.driver.back() # volta à página anterior
        self.driver.forward() # navega 1 vez para frente
        print(self.driver.title) # Obtém título da página
        print(self.driver.current_url) # Obtém URL (endereço) da página atual
        print(self.driver.page_source) # Obtém o código fonte da página atual
        self.driver.close() # Fecha janela atual
        self.driver.quit() # Fecha a sessão do driver e todas as abas
        print(self.driver.find_element_by_xpath('//a[@class="navbar-brand"]').text) # obtém o texto dentro de um elemento
        print(self.driver.find_element_by_xpath('//a[@class="navbar-brand"]').get_attribute("href"))


curso = CursoAutomacao()
curso.Iniciar()
