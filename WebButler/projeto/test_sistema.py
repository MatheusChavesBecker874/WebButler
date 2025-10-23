from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Função para configurar o driver do Chrome
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service, options=chrome_options)  
    driver.maximize_window()  
    return driver

# Função para realizar o login
def login(driver):
    driver.get("https://webbutler.onrender.com/") 
    time.sleep(2)
    
    driver.find_element("name", "username").send_keys("admin")  
    driver.find_element("name", "password").send_keys("admin123")
    driver.find_element("xpath", "//button[text()='Entrar']").click()  
    time.sleep(3)
    
    assert "Início" in driver.title
    print("Login bem-sucedido!")

# Função para testar a criação de aluno
def test_create_student(driver):
    driver.get("https://webbutler.onrender.com/alunos/criar/")  # URL de criação de aluno
    time.sleep(2)
    
    driver.find_element("name", "nome").send_keys("Aluno Teste")
    turma_select = driver.find_element("name", "turma")
    turma_select.click()
    turma_select.find_element("xpath", "//option[text()='eu e tu']").click()
    driver.find_element("xpath", "//button[contains(text(),'Salvar')]").click() 
    time.sleep(3)
    
    assert "Aluno Teste" in driver.page_source
    print("Aluno criado com sucesso!")

# Função para testar a criação de turma
def test_create_class(driver):
    driver.get("https://webbutler.onrender.com/turmas/nova/") 
    time.sleep(2)
    
    driver.find_element("name", "nome").send_keys("Turma Teste")
    
    # Espera até que o botão "Salvar" esteja presente e visível
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'💾 Salvar')]"))
    )
    save_button.click() 
    time.sleep(3)
    
    assert "Turma Teste" in driver.page_source 
    print("Turma criada com sucesso!")

# Função para testar a criação de atividade
def test_create_activity(driver):
    driver.get("https://webbutler.onrender.com/atividades/nova/")  # URL de criação de atividade
    time.sleep(2)
    
    driver.find_element("name", "titulo").send_keys("Atividade Teste") 
    driver.find_element("name", "descricao").send_keys("Descrição da atividade.") 
    turma_select = driver.find_element("name", "turma")
    turma_select.click()
    turma_select.find_element("xpath", "//option[text()='eu e tu']").click() 
    driver.find_element("xpath", "//button[contains(text(),'Salvar')]").click()  # Clica no botão de salvar
    time.sleep(3)
    
    assert "Atividade Teste" in driver.page_source 
    print("Atividade criada com sucesso!")

# Função para testar a edição de atividade
def test_edit_activity(driver):
    driver.get("https://webbutler.onrender.com/atividades/4/editar/")  # URL de editar atividade
    time.sleep(2)
    
    driver.find_element("name", "titulo").clear()
    driver.find_element("name", "titulo").send_keys("Atividade Editada")
    driver.find_element("name", "descricao").clear()
    driver.find_element("name", "descricao").send_keys("Descrição editada da atividade.")
    
    # Espera até que o botão "Salvar Progresso" esteja presente e visível
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Salvar Progresso')]"))
    )
    save_button.click()  # Clica no botão de salvar
    time.sleep(3)
    
    assert "Atividade Editada" in driver.page_source
    print("Atividade editada com sucesso!")

# Função para testar a edição de horário
def test_edit_schedule(driver):
    driver.get("https://webbutler.onrender.com/atividades/4/editar-horarios/")  # URL de editar horário
    time.sleep(2)
    
    driver.find_element("name", "horario_inicio").clear()
    driver.find_element("name", "horario_inicio").send_keys("10:00")
    driver.find_element("name", "horario_fim").clear()
    driver.find_element("name", "horario_fim").send_keys("12:00")
    
    # Espera até que o botão de salvar esteja presente e visível
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Salvar')]"))
    )
    save_button.click()
    time.sleep(3)
    
    assert "10:00" in driver.page_source and "12:00" in driver.page_source  # Verifica se o horário foi editado
    print("Horário editado com sucesso!")

# Função principal que executa os testes
def run_tests():
    print("Iniciando testes do sistema...")
    
    # Configura o driver
    driver = setup_driver()
    
    try:
        login(driver)  # Realiza o login uma vez antes de executar os testes
        
        test_create_student(driver)  # Teste de criação de aluno
        test_create_class(driver)  # Teste de criação de turma
        test_create_activity(driver)  # Teste de criação de atividade
        test_edit_activity(driver)  # Teste de edição de atividade
        test_edit_schedule(driver)  # Teste de edição de horário
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
