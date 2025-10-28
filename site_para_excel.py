from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import openpyxl

url_site = 'https://cursoautomacao.netlify.app/'

class Automacao():

    def __init__(self):
        options = Options()
        options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(options=options)
        
    def Iniciar(self):
        driver = self.driver

        driver.get(url_site)
        driver.maximize_window()
        sleep(3)
        
        tabela = driver.find_element(By.CSS_SELECTOR, "table.table-striped")
        
        linhas = tabela.find_elements(By.TAG_NAME, "tr")
        
        dados = []
        
        for linha in linhas[1:]:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) == 3:
                nome = colunas[0].text
                abreviacao = colunas[1].text
                populacao = colunas[2].text
                dados.append([nome, abreviacao, populacao])
        
        df = pd.DataFrame(dados, columns=["Nome", "Abreviação", "População"])
        
        # Salvar no Excel
        df.to_excel("tabela_estados.xlsx", index=False)
        
        print("✅ Dados extraídos e salvos em 'tabela_estados.xlsx' com sucesso!")
        
        driver.quit()


if __name__ == "__main__":
    automacao = Automacao()
    automacao.Iniciar()
