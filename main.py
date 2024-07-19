from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
MeuImovel = "https://appmeuimovel.com/?utm_source=google&utm_medium=cpc&utm_campaign=260994978&gad_source=1&gclid=EAIaIQobChMIltT8q4exhwMV8NbCBB0UIggCEAAYASAAEgJTHfD_BwE"
imovelk ="https://www.imovelk.com.br/sao-paulo/sao-paulo-sp/?"
vivareal = "https://www.vivareal.com.br/venda/sp/sao-paulo/apartamento_residencial/#onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Paulo,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%20Paulo,,,"
pesquisa = "sao paulo\n"
Distancia=6
SCROLL_PAUSE_TIME = 0.1
driver.get(MeuImovel)

#navegacao
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "/html/body/div[3]/header/div/div[2]/nav/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[1]/div[3]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[2]/div[3]/div/div[1]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[4]/div[3]/div/div[1]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[5]/div[3]/div/div[1]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[6]/div[4]/div[2]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[7]/div[3]/div/div[2]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[9]/div[4]/div[2]").click()


driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[10]/div[3]/div[1]/form/input").send_keys(pesquisa)


driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[2]/div").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[3]/div[10]/div[4]/div[2]").click()

driver.find_element(By.XPATH,"/html/body/div[3]/div[5]/div[2]/div[1]").click()
#




#scroll ate o fim da pagina para carregar todos os anuncios 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#
#pega todos os anuncios 
anuncios  = driver.find_elements(By.CLASS_NAME, "imovel-item")
#

#salva janela original 
original_window = driver.current_window_handle
# 
#pega informacoes de cada anuncio 
for web in anuncios:
    web.click()
    #muda de pagina para o do anuncio 
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    #
    driver.implicitly_wait(2)
    
    nome =driver.find_element(By.ID,"realtyName").text()
    endereco = driver.find_element(By.XPATH,"/html/body/div[3]/section/div[2]/div[2]/div[1]/div/p").text()
    pagina = window_handle
    print(nome)
    print(endereco)
    print(pagina)
    
    endereco = driver.find_element(By.XPATH,"/html/body/div[3]/header/div/div[2]/nav/a").click()
    driver.switch_to.window(original_window)

#
