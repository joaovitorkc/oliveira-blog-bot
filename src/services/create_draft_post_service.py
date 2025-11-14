import ast
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from google import genai
from src.services.create_prompt_service import create_prompt
import os

def create_draft_post(driver, subject):
    client = genai.Client()
    print("Fazendo rascunho sobre o tema: " + subject["name"]) 
    driver.get("https://oliveiraassessoriacontab.com.br/wp-admin/post-new.php") 

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f'{create_prompt(subject["name"])}'
    )

    # data = {
    #     "contents": [{
    #         "parts": [
    #             {
    #                 "text": f'{create_prompt(subject["name"])}'
    #             }
    #         ]
    #     }]
    # }

    # response = requests.post(url, headers=headers, json=data)

    # print(f"Requisição para o tema {subject['name']} foi concluída com status {response.status_code}")
    response_data = response.text

    textos_str = response_data.replace("```python", "").replace("```", "").replace("textos = ", "").strip()

    try:
        textos = ast.literal_eval(textos_str)

        title_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Adicionar título"]'))
        )
        title_input.send_keys(subject["name"])
        print("Título adicionado")

        print("Adicionando categorias")
        for category in textos["categories"]:
            category_name = category["name"]
            category_input = WebDriverWait(driver, 200).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//label[@class='components-checkbox-control__label' and text()='{category_name}']")
                )
            )   
            category_input.click()
        print("Categorias adicionadas")

        divi_button = driver.find_element(
            By.CSS_SELECTOR, '[id="et-switch-to-divi"]'
        )
        divi_button.click()
        print("Botão de editar com DIVI clicado")

        time.sleep(2)
            
        layout_button_1 = WebDriverWait(driver, 200).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='et-fb-page-creation-card-button' and text()='Selecionar Layout']")
            )
        )

        driver.refresh()
        print("Atualizando a pagina")

        try:
            alert = Alert(driver)
            alert.accept() 
            print("Alerta de aceitar clicado")
        except:
            pass

        layout_button = WebDriverWait(driver, 200).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='et-fb-page-creation-card-button' and text()='Selecionar Layout']")
            )
        )    

        time.sleep(5)

        layout_button.click()
        print("Botão de escolher layout clicado")

        time.sleep(5)

        existing_pages_link = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.existing_pages'))
        )

        time.sleep(2)

        existing_pages_link.click()
        print("Botão de listar posts clicado")

        time.sleep(5)
            
        link_element = WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'IRPF 2025: PERÍODO DEVE COMEÇAR NO DIA 17 DE MARÇO.')]"))
        )

        link_element.click()
        print("Post base clicado")

        time.sleep(2)

        use_this_layout_button = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.et-common-button.et-common-button--primary'))
        )

        use_this_layout_button.click()
        print("Botão de usar layout clicado")

        print("Esperando a página ser carregada")
        WebDriverWait(driver, 100).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "et-fb-tooltip-modal--progress-label"))
        )

        print("Salvando rascunho")
        save_draft_button = driver.find_element(
            By.CSS_SELECTOR, '[data-tip="Salvar Rascunho"]'
        )
        save_draft_button.click() 

        time.sleep(2)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-tip='Salvar Rascunho' and not(@disabled)]"))
        ) 
        print("Rascunho salvo")

        return textos

    except (SyntaxError, ValueError) as e:
        print(f"Erro na criação do rascunho: {e}")
