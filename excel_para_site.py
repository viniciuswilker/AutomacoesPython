# mportação excel
import pandas as pd

# import web
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_argument('--lang=pt-BR')
url_site = 'https://cursoautomacao.netlify.app/login'
# 0 - Ler a planilha
arquivo = 'Panilha.xlsx'

data_frame = pd.read_excel(arquivo)

# print(data_frame)
# 1 - loop de cada arquivo EXCEL

try: 
    for index, row in data_frame.iterrows():
    # print('Index:' + str(index) + ' E o nome da pessoa é ' + row['NOME'])

        driver = webdriver.Chrome(options=options)
        driver.get(url_site)
        
        sleep(5)
        email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
        senha_input = driver.find_element(By.XPATH, '//*[@id="senha"]')
        email_input.send_keys(row['EMAIL'])
        sleep(1)
        senha_input.send_keys(row['SENHA'])
        sleep(2)
        botao_entrar = driver.find_element(By.XPATH, '/html/body/section/form/div/button')
        botao_entrar.click()
        sleep(1)
        
        print(f'Usuario cadastrado com sucesso')
        driver.quit()


except Exception as e:
    print(f'Erro: {e}')


 