from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

arguments = ['--lang=pt-BR', '--incognito', '--disable-notifications']

for argument in arguments:
    chrome_options.add_argument(argument)


caminho_padrao_para_download = 'E:\\Storage\\Desktop'


service = Service(executable_path="./chromedriver.exe")


# Lista de opções experimentais (nem todas estão documentadas) https://chromium.googlesource.com
chrome_options.add_experimental_option("prefs", {
    'download.default_directory': caminho_padrao_para_download,
    # Atualiza diretório para diretório passado acima
    'download.directory_upgrade': True,
    # Seta se o navegador deve pedir ou não para fazer download
    'download.prompt_for_download': False,
    'profile.default_content_setting_values.notifications': 2,  # Desabilita notificações
    # Allow multiple downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

driver.get('https://www.youtube.com')
