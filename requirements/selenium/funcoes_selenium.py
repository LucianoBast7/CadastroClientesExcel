from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json
from datetime import datetime
from pathlib import Path
import re
import warnings
warnings.filterwarnings("ignore")

# Parâmetros de Data
hoje = datetime.today()
ano = hoje.strftime("%Y")
mes = hoje.strftime("%m")
dia = hoje.strftime("%d")

caminho_atual = Path(__file__).resolve()
raiz_projeto = caminho_atual.parents[3]

# Caminho arquivo
arquivo = os.path.abspath(f"{raiz_projeto}\\3. Finished\\{ano}\\{mes}\\{dia}")

# Garante que o diretório de salvamento existe
os.makedirs(arquivo, exist_ok=True)

class SeleniumAutomator:
    def __init__(self):
        """ Inicializa o navegador com opções configuradas para baixar PDF automaticamente """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Maximiza a janela
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--kiosk-printing")  # Ativa a impressão automática
        options.add_argument("--enable-print-browser")  # Garante a impressão em modo silencioso

        # Configuração para salvar automaticamente como PDF
        app_state = {
            "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
            "isHeaderFooterEnabled": False  # Remove cabeçalho e rodapé do PDF
        }

        prefs = {
            "printing.print_preview_sticky_settings.appState": json.dumps(app_state),  # Serializa corretamente
            "savefile.default_directory": arquivo,
            "download.prompt_for_download": False,  # Não exibir a caixa de diálogo de download
            "download.directory_upgrade": True
        }

        options.add_experimental_option("prefs", prefs)

        # Inicializa o driver do Chrome
        self.driver = webdriver.Chrome(options=options)

    def save_as_pdf(self):
        """ Executa o comando para salvar a página como PDF automaticamente """
        print("Salvando página como PDF...")
        self.driver.execute_script("window.print();")
        time.sleep(5)  # Tempo para salvar o arquivo

    def navegar_para(self, url):
        """ Abre uma URL """
        self.driver.get(url)

    def fechar_navegador(self):
        """ Fecha o navegador """
        self.driver.quit()

    def maximizar_janela(self):
        """ Maximiza a janela do navegador """
        self.driver.maximize_window()

    def obter_titulo(self):
        """ Retorna o título da página atual """
        return self.driver.title

    def obter_texto_por_id(self, elemento_id):
        """ Obtém o texto de um elemento pelo ID """
        return self.driver.find_element(By.ID, elemento_id).text

    def obter_texto_por_nome(self, nome):
        """ Obtém o texto de um elemento pelo Name """
        return self.driver.find_element(By.NAME, nome).text

    def obter_texto_por_xpath(self, xpath):
        """ Obtém o texto de um elemento pelo XPath """
        return self.driver.find_element(By.XPATH, xpath).text

    def digitar_por_xpath(self, xpath, texto):
        """ Digita um texto em um campo de entrada pelo XPath """
        self.driver.find_element(By.XPATH, xpath).send_keys(texto)

    def digitar_por_id(self, elemento_id, texto):
        """ Digita um texto em um campo de entrada pelo ID """
        self.driver.find_element(By.ID, elemento_id).send_keys(texto)

    def clicar_por_xpath(self, xpath):
        """ Clica em um elemento pelo XPath """
        self.driver.find_element(By.XPATH, xpath).click()

    def clicar_por_id(self, elemento_id):
        """ Clica em um elemento pelo ID """
        self.driver.find_element(By.ID, elemento_id).click()

    def clicar_por_nome(self, nome):
        """ Clica em um elemento pelo Name """
        self.driver.find_element(By.NAME, nome).click()

    def clicar_link_por_texto(self, texto):
        """ Clica em um link pelo texto visível """
        self.driver.find_element(By.LINK_TEXT, texto).click()

    def executar_javascript(self, script):
        """ Executa um script JavaScript na página """
        return self.driver.execute_script(script)

    def alterar_frame_por_texto(self, frame_name=""):
        """ Altera para um frame específico pelo nome """
        if frame_name:
            self.driver.switch_to.frame(frame_name)
        else:
            self.driver.switch_to.default_content()

    def alterar_frame_por_index(self, index):
        """ Altera para um frame pelo índice """
        self.driver.switch_to.frame(index)

    def aguardar_estado_documento(self):
        """ Aguarda a página carregar completamente """
        while self.executar_javascript("return document.readyState") != "complete":
            time.sleep(1)

    def selecionar_item_lista_por_nome(self, nome, texto):
        """ Seleciona um item em uma lista suspensa pelo Name """
        select = Select(self.driver.find_element(By.NAME, nome))
        select.select_by_visible_text(texto)

    def validar_checkbox_por_id(self, checkbox_id):
        """ Retorna True se um checkbox estiver marcado """
        return self.driver.find_element(By.ID, checkbox_id).is_selected()

    def aceitar_alerta(self):
        """ Aceita um alerta (popup) """
        Alert(self.driver).accept()

    def rejeitar_alerta(self):
        """ Rejeita um alerta (popup) """
        Alert(self.driver).dismiss()

    def obter_texto_alerta(self):
        """ Obtém o texto de um alerta (popup) """
        return Alert(self.driver).text

    def limpar_campo_por_xpath(self, xpath):
        """ Limpa um campo de entrada pelo XPath """
        self.driver.find_element(By.XPATH, xpath).clear()

    def selecionar_item_lista_por_id(self, elemento_id, texto):
        """ Seleciona um item em uma lista suspensa pelo ID """
        select = Select(self.driver.find_element(By.ID, elemento_id))
        select.select_by_visible_text(texto)

    def enviar_tab_por_id(self, elemento_id):
        """ Envia a tecla TAB para um campo de entrada pelo ID """
        self.driver.find_element(By.ID, elemento_id).send_keys(Keys.TAB)

    def enviar_arquivo_por_id(self, elemento_id, caminho_arquivo):
        """ Envia um arquivo para um input type='file' """
        self.driver.find_element(By.ID, elemento_id).send_keys(caminho_arquivo)

    def enviar_arquivo_por_xpath(self, elemento_xpath, caminho_arquivo):
        """ Envia um arquivo para um input type='file' """
        self.driver.find_element(By.XPATH, elemento_xpath).send_keys(caminho_arquivo)

    def trocar_para_nova_aba(self):
        """ Troca para a última aba aberta """
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Muda para a última aba aberta

    def tirar_print(self, caminho_arquivo):
        """ Tira um print da tela e salva no caminho especificado """
        self.driver.save_screenshot(caminho_arquivo)

    def voltar_para_aba_anterior(self):
        """ Volta para a aba anterior """
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[0])  # Volta para a primeira aba

    def fechar_nova_aba(self):
        """ Fecha a aba atual e retorna para a aba anterior """
        if len(self.driver.window_handles) > 1:
            self.driver.close()  # Fecha a aba ativa
            self.driver.switch_to.window(self.driver.window_handles[0])  # Volta para a primeira aba

    def limpar_campo_por_xpath(self, xpath, timeout=10):
        campo = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        campo.clear()

    def aguardar_elemento(self, by, valor, tempo=10):
        WebDriverWait(self.driver, tempo).until(
            EC.presence_of_element_located((by, valor))
        )

    def aguardar_elemento_por_xpath(self, valor, tempo=10):
        WebDriverWait(self.driver, tempo).until(
            EC.presence_of_element_located((By.XPATH, valor))
        )

    def refresh(self):
        self.driver.refresh()

    def clicar_por_xpath_sem_esperar(self, xpath, timeout=15):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].click();", el)

    def focar_e_enter(self, xpath, timeout=15):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        el.send_keys(Keys.ENTER)

    def aceitar_alerta(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(f"Mensagem do alerta: {alert.text}")  # Opcional
        alert.accept()  # Clica em "OK"

    def capturar_text_por_xpath(self, xpath, msg_re_search, timeout=10):
        mensagem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((
                By.XPATH, xpath
            ))
        ).text

        # Extrai apenas o número do arquivo (últimos dígitos da mensagem)
        match = re.search(msg_re_search, mensagem)
        if match:
            return match.group(1)
        else:
            return None

    def mudar_aba_navegador(self, indice_aba):
        self.driver.switch_to.window(self.driver.window_handles[indice_aba])

    def aguardar_pdf(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: (".pdf" in d.current_url) or ("consultar.jsf" in d.current_url)
        )
        # Opcional: ainda verificar que há <embed> ou <iframe>
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_elements(By.TAG_NAME, "embed") or d.find_elements(By.TAG_NAME, "iframe")
        )