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

print(os.getenv("GEMINI_API_KEY"))

load_dotenv()

# url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
# headers = {
#     "Content-Type": "application/json",
#     "x-goog-api-key": os.getenv("GOOGLE_API_KEY"),
# }

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
    {"name": "SITUAÇÕES QUE COLOCAM O FLUXO DE CAIXA EM PERIGO."},
    {"name": "O ATIVO INVISÍVEL DA LIDERANÇA: POR QUE A CONFIANÇA É O MAIOR BENEFÍCIO QUE UMA EMPRESA PODE OFERECER."},
    {"name": "REFORMA TRIBUTÁRIA: TOP 5 DICAS PARA INCLUIR NO CHECKLIST DA EMPRESA."},
    {"name": "COMPRADOR DO IMÓVEL DEVE PAGAR CONDOMÍNIO MESMO QUE AINDA NÃO TENHA CHAVES."},
    {"name": "DESCONTO DO DSR: O QUE DIZ A LEI, COMO CALCULAR E INCLUIR NA FOLHA DE PAGAMENTO."},
    {"name": "CARTÃO, PIX E NOTA FISCAL: TUDO O QUE O FISCO JÁ ESTÁ CRUZANDO E OS CUIDADOS PARA A SUA EMPRESA NÃO CAIR EM MALHA FISCAL."},
    {"name": "MEI E PREVIDÊNCIA SOCIAL: 5 DÚVIDAS COMUNS DE MICROEMPREENDEDORES INDIVIDUAIS."},
    {"name": "CONTRIBUIÇÃO ASSISTENCIAL: O QUE DIZ A CLT APÓS A REFORMA."},
    {"name": "SUSPENSÃO DISCIPLINAR NO TRABALHO INTERMITENTE: QUANDO E COMO APLICAR CORRETAMENTE."},
    {"name": "GRATIFICAÇÃO POR FUNÇÃO: O QUE SUA EMPRESA PRECISA SABER PARA NÃO TER PROBLEMAS LEGAIS."},
    {"name": "PRINCIPAIS TERMOS NA GESTÃO DE CUSTOS: UMA ABORDAGEM CONCEITUAL."},
    {"name": "PESSOAS FÍSICAS E A TRIBUTAÇÃO DAS OPERAÇÕES COM BENS IMÓVEIS – CONFORME A LC 214/2025."},
    {"name": "CONTABILIDADE E FLUXO DE CAIXA: UMA DUPLA ESSENCIAL PARA O SEU NEGÓCIO."}
]

for subject in subjects:
    textos = create_draft_post(driver, subject)

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
