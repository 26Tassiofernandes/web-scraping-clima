# ## Coletando dados de um site de clima

# Link do site: https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected

# Criando navegador virtual

from selenium import webdriver
navegador = webdriver.Chrome()
from selenium.webdriver.common.by import By
navegador.get(r"https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected")

# Raspando dados do site:

from selenium.webdriver.common.keys import Keys
from time import sleep

while True:
    
    try:
    
        # Campo para o usuário inserir o nome da cidade desejada:
        nome_cidade = input('\033[1;34mDigite o nome da cidade [0 p/ parar]: \033[m').strip()
        
        if nome_cidade == '0':
            print('\033[1;31mVocê saiu do programa!\033[m')
            break
            
        if not nome_cidade.replace(' ', '').isalpha():
            raise ValueError('\033[1;31mInsira o nome de uma cidade válida!\033[m')
        
        if nome_cidade != '0':
            
            print('\033[1;32mRequisitando dados...\n\033[m')
            
            # O nome da cidade vai para dentro do campo de pesquisa do site:
            campo_pesquisa = navegador.find_element(By.XPATH, '//*[@id="LocationSearch_input"]')

            # Limpar o campo de pesquisa e inserir o nome da cidade:
            campo_pesquisa.send_keys(nome_cidade)
            sleep(0.8)

            # Apertar tecla para baixo para selecionar a primeira sugestão:
            campo_pesquisa.send_keys(Keys.ARROW_DOWN)
            sleep(1)

            # Apertar Enter para confirmar a primeira sugestão de cidade:
            opcao_cidade = navegador.find_element(By.CSS_SELECTOR, 'button[data-testid="ctaButton"]').send_keys(Keys.ENTER)

            conteudo_site = navegador.find_elements(By.CLASS_NAME, 'TodayDetailsCard--detailsContainer--2yLtL')
            
            clima_principal = navegador.find_element(By.CLASS_NAME, 'CurrentConditions--primary--2DOqs')
            
            titulo_cidade = navegador.find_element(By.XPATH, '//*[@id="todayDetails"]/section/header/h2')

            # Saída:
            sleep(1)
            print(f'\033[1;35m{titulo_cidade.text}:\n\033[m')
            print('\033[1mTemperatura:', clima_principal.text)

            for dado in conteudo_site:
                print(f'\033[1m{dado.text}\n\033[m')
        
    except ValueError as e:
        print(e)

# Limpar o campo de pesquisa quando necessário:

campo_pesquisa = navegador.find_element(By.XPATH, '//*[@id="LocationSearch_input"]')
campo_pesquisa.clear()
