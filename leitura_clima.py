from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import pandas as pd

#Acessa um site através de um navegador
navegador = webdriver.Chrome()

navegador.get('https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp')
completo = False
#Captura as informações através de um elemento identificado pelo XPATH
def consultar_clima():
    temperatura = str(navegador.find_element(By.XPATH, '//*[@id="mainContent"]/div[6]/div[3]/div[1]/div[3]/div[1]/div/div[2]/span').get_attribute("textContent")).strip()
    umidade = str(navegador.find_element(By.XPATH, '//*[@id="mainContent"]/div[6]/div[3]/div[1]/div[3]/div[1]/div/div[4]/ul/li[2]/div[2]/p').get_attribute("textContent")).strip()
    data_hora = datetime.datetime.now()
    agora = data_hora.strftime("%d/%m/%Y %H:%M")

    print(f'Temperatura em São Paulo agora: {temperatura}C')
    print(f'Umidade do Ar em São Paulo agora: {umidade}')
    print(f'Momento da leitura: {agora}')

    #Carrega o arquivo .xlsx
    arquivo = pd.read_excel('clima_sp.xlsx')

    #Cria um DataFrame com os dados obtidos
    dados = pd.DataFrame(
        {
        "temperatura": [temperatura],
        "umidade": [umidade],
        "leitura": [agora]
        },
    )
    
    #Concatena e salva os dados
    df = pd.concat([arquivo, dados], ignore_index=True)
    df.to_excel('clima_sp.xlsx', index=False)
    print('Informaçõs adicionadas ao arquivo ".xlsx"')
    


