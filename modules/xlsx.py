import pandas as pd
from pathlib import Path
import os
from datetime import datetime
import glob
import sys
import shutil

hoje = datetime.now()
dia = hoje.strftime("%d")
mes = hoje.strftime("%m")
ano = hoje.strftime("%Y")

caminho_atual = Path(__file__).resolve()
raiz_projeto = caminho_atual.parents[2]

caminho_input = f"{raiz_projeto}\\1. Input"
os.makedirs(caminho_input, exist_ok=True)

caminho_exportacao_excel = f"{raiz_projeto}\\2. Processed\\{ano}\\{mes}\\{dia}"
os.makedirs(caminho_exportacao_excel, exist_ok=True)

caminho_finalizado = f"{raiz_projeto}\\3. Finished\\{ano}\\{mes}\\{dia}"
os.makedirs(caminho_finalizado, exist_ok=True)

class ConfigXlsx():
    def __init__(self):
        self.arquivos = glob.glob(os.path.join(caminho_input, "*.xlsx"))
        self.colunas = ["Nome", "Email", "Telefone", "Cidade", "Estado", "Status"]

    def arquivo_existe(self):
        if not self.arquivos:
            return False
        return True

    def captura_arquivos_xlsx(self):
        try:
            if not self.arquivo_existe():
                print(f"{datetime.now()} - SEM ARQUIVOS. FINALIZANDO SCRIPT")
                sys.exit(0)
            else:
                arquivos_xlsx = self.arquivos
                return arquivos_xlsx
        except Exception as e:
            raise e

    def extrai_dados(self, arquivos):
        try:
            df = pd.read_excel(arquivos[0])
            df.columns = self.colunas
            shutil.move(arquivos[0], caminho_exportacao_excel)
            return df
        except Exception as e:
            raise e

    def salva_dados(self, dados):
        try:
            dados.to_excel(f"{caminho_finalizado}\\dados_cadastrados.xlsx", index=False)
        except Exception as e:
            raise e