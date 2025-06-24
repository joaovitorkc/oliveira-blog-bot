from dotenv import load_dotenv
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
import os

load_dotenv()

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

username_input.send_keys(os.getenv("USER_NAME"))
password_input.send_keys(os.getenv("USER_PASSWORD"))

register_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="wp-submit"]'))
)

register_button.click()

subjects = [
    {"name": "VOCÊ SABE QUAIS AS REGRAS DO AVISO PRÉVIO? FIQUE POR DENTRO DOS DETALHES E EVITE PROBLEMAS."},
    {"name": "CERTIDÃO DE REGULARIDADE FISCAL DE OBRA (CND DE OBRA), O QUE VOCÊ PRECISA SABER!"},
    {"name": "DEPRECIAÇÃO CONTÁBIL: IMPACTO DIRETO NA BASE DE CÁLCULO DE IRPJ E CSLL PARA EMPRESAS DO LUCRO REAL."},
    {"name": "7 ESTRATÉGIAS PRÁTICAS PARA MELHORAR SUA GESTÃO DE EMOÇÕES NO AMBIENTE PROFISSIONAL."},
    {"name": "ENTENDA A IMPORTÂNCIA DE CONTROLAR O SUBLIMITE DO SIMPLES NACIONAL."},
    {"name": "PENALIDADES DISCIPLINARES: REGRAS QUE O EMPREGADOR DEVE SEGUIR."},
    {"name": "ECD 2025: VEJA AS PRINCIPAIS DÚVIDAS E AS RESPOSTAS."},
    {"name": "DEPRECIAÇÃO CONTÁBIL: IMPACTO DIRETO NA BASE DE CÁLCULO DE IRPJ E CSLL PARA EMPRESAS DO LUCRO REAL."},
    {"name": "UMA ANÁLISE TÉCNICA DO CRUZAMENTO DE DADOS ENTRE DIRPF E E-FINANCEIRA PELA RECEITA FEDERAL."},
    {"name": "PRINCIPAIS DÚVIDAS DOS EMPREENDEDORES, O QUE VOCÊ PRECISA SABER ANTES DE ABRIR SUA EMPRESA."},
    {"name": "COMO A INTEGRAÇÃO COMERCIAL E OPERAÇÃO PODE DESTRAVAR O CRESCIMENTO DAS EMPRESAS?"},
    {"name": "EMPRESA INATIVA AINDA PRECISA DE UM PROFISSIONAL CONTÁBIL? ENTENDA."},
    {"name": "GESTÃO DE CRISE: COMO LIDAR COM SITUAÇÕES DESAFIADORAS NO SEU NEGÓCIO?"},
    {"name": "POR QUE O RH É ESSENCIAL PARA CRIAR MARCAS AUTÊNTICAS E RECONHECIDAS NO MERCADO."},
    {"name": "REFORMA TRIBUTÁRIA PARA MÉDICOS."},
    {"name": "IOF 2025: ENTENDA O QUE MUDA EM COMPRAS, CRÉDITO E VIAGENS."},
    {"name": "VENDA DE PARTICIPAÇÃO SOCIETÁRIA NÃO É CESSÃO."},
    {"name": "COMO PMES PODEM USAR AS REDES SOCIAIS PARA ATRAIR CLIENTES E AUMENTAR O FATURAMENTO."},
    {"name": "DIRPF 2025: CONFIRA DICAS PARA EVITAR ERROS NA RETA FINAL."},
]

for subject in subjects:
    textos = create_draft_post(driver, url, headers, subject)

    try:
        post_content = create_post_content(textos)

        query = create_subject_query(subject["name"], post_content)

        execute_query(query)

        # post_id_result = execute_query(f"""
        #     SELECT id
        #     FROM wp_posts 
        #     WHERE LOWER(post_title) LIKE '%{subject['name'].lower()}%' 
        #     AND post_type = 'post';
        # """)

        # post_id = post_id_result[0][0] if post_id_result else None

        # thumb_id_result = execute_query(f"""
        #     SELECT id
        #     FROM wp_posts 
        #     WHERE LOWER(post_title) LIKE '%{subject['name'].lower()}%'
        #     AND post_type = 'attachment';
        # """)

        # thumb_id = thumb_id_result[0][0] if thumb_id_result else None  
        
        # meta_id_result = execute_query(f"""
        #     SELECT COALESCE(MAX(meta_id), 0) + 1 AS next_meta_id 
        #     FROM wp_postmeta
        # """)

        # next_meta_id = meta_id_result[0][0] if meta_id_result else None      

        # execute_query(f"""
        #     INSERT INTO wp_postmeta (meta_id, post_id, meta_key, meta_value)
        #     VALUES (
        #         {next_meta_id}, 
        #         {post_id},
        #         '_thumbnail_id', 
        #         '{thumb_id}'
        #     );
        # """)

    except (SyntaxError, ValueError) as e:
        print(f"Erro na conversão da string para dicionário: {e}")
