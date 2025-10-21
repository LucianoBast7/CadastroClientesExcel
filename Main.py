from modules.xlsx import ConfigXlsx
from modules.web import ConfigWeb
from datetime import datetime
from requirements.variables.variables import ConfigVariaveis
hoje = datetime.now()
dia = hoje.strftime("%d")
mes = hoje.strftime("%m")
ano = hoje.strftime("%Y")

# Carregando Objetos
xlsx = ConfigXlsx()
bot  = ConfigWeb()
variables = ConfigVariaveis()

def main():
    print(f"{datetime.now()} - CAPTURANDO ARQUIVOS")
    arquivos_xlsx = xlsx.captura_arquivos_xlsx()
    print(f"{datetime.now()} - ARQUIVOS CAPTURADOS")

    print(f"{datetime.now()} - INICIANDO EXTRAÇÃO")
    dados_extraidos = xlsx.extrai_dados(arquivos_xlsx)
    print(f"{datetime.now()} - EXTRAÇÃO FINALIZADA")

    print(f"{datetime.now()} - ACESSANDO SITE")
    bot.acessa_site(variables.url_site)
    print(f"{datetime.now()} - SITE ACESSADO")

    print(f"{datetime.now()} - FAZENDO LOGIN")
    bot.faz_login(variables.usuario, variables.senha)
    print(f"{datetime.now()} - LOGIN REALIZADO")

    print(f"{datetime.now()} - ACESSANDO TELA DE CADASTRO")
    bot.acessa_tela_cadastro()
    print(f"{datetime.now()} - TELA DE CADASTRO ACESSADA")

    print(f"{datetime.now()} - REALIZANDO CADASTRO")
    dados_cadastrados = bot.realiza_cadastro(dados_extraidos)
    print(f"{datetime.now()} - CADASTRO FINALIZADO")

    print(f"{datetime.now()} - SALVANDO PLANILHA")
    xlsx.salva_dados(dados_cadastrados)
    print(f"{datetime.now()} - PLANILHA SALVA")

    
if __name__ == "__main__":
    main()