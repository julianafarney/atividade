from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabInfo\\Downloads\\chromedriver-win32(2)\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://github.com/")
    print('-2')
    botao_login = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a")
    botao_login.click()
    print('-1')
    def enviarDados(usuario, senha):
        print('0')
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login_field'))
        )
        print('1')
        senha_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        print('2')
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]'))
        )
        email_login.clear
        senha_login.clear
        print('3')
        email_login.send_keys(usuario)
        print('4')
        senha_login.send_keys(senha)
        print('5')
        btn_login.click()
        driver.implicitly_wait(5)  
        print('6')

        return alert
    
    alert = enviarDados('victoriamariana759@gmail.com','CuR$o7002')
    if 'Your username is invalid' in alert :
        print("Teste de usuário inválido bem sucedido")
    else:
        print("Usuário incorreto não reconhecido, teste falhou")
    
    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()