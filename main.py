from src import create_draft_post
from src import create_post_content
from src import create_subject_query
from src import execute_query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyCFN8aJQI9fpQtR5o5Ls-XVw1B44rfpjxk"
headers = {
    "Content-Type": "application/json"
}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)

driver.get("https://oliveiraassessoriacontab.com.br/wp-login.php?loggedout=true&wp_lang=pt_BR")

username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="user_login"]'))
)
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="user_pass"]'))
)

username_input.send_keys("jota")
password_input.send_keys("Joao190896")

register_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="wp-submit"]'))
)

register_button.click()

subjects = [
    {"name": "ADERIÇÃO DO MIT E SUBSTITUIÇÃO DA DCTF, ENTENDA!"},
    {"name": "MANTER FUNCIONÁRIOS TOXICOS, QUANTO CUSTA PARA MANTÊ-LOS?"},
    {"name": "RETENÇÃO DE INSS, ENTENDA COMO FUNCIONA, QUEM DEVE PAGAR?"}
]

for subject in subjects:
    textos = create_draft_post(driver, url, headers, subject)

    try:
        post_content = create_post_content(textos)

        query = create_subject_query(subject["name"], post_content)

        execute_query(query)

    except (SyntaxError, ValueError) as e:
        print(f"Erro na conversão da string para dicionário: {e}")
