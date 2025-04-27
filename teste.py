#  INSTALANDO MANUAL

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# service = Service(executable_path="./chromedriver.exe")

# driver = webdriver.Chrome(service=service)

# driver.get('https://www.youtube.com')


#  ==================================
#  INSTALAR O WEBDRIVER AUTO

#  pip install webdriver-manager


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Ele baixa e gerencia automaticamente o chromedriver correto
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.youtube.com')





# ============================

#  MAIS DIRETO AO PONTO ( MENOS PROF )

import webbrowser

# URL que você quer abrir
url = "https://cursoautomacao.netlify.app"

# Abrir o site no navegador padrão
webbrowser.open(url)
