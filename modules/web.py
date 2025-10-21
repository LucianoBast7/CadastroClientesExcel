from requirements.selenium.funcoes_selenium import SeleniumAutomator

timeout = 60

class ConfigWeb():
    def __init__(self):
        self.bot = SeleniumAutomator()
        

    def acessa_site(self, url):
        try:
            # Acessa Site
            self.bot.navegar_para(url)
            self.bot.aguardar_estado_documento()
            self.bot.maximizar_janela()
        except Exception as e:
            raise e

    def faz_login(self, user, password):
        try:
            # Aguarda Icone de Login
            self.bot.aguardar_elemento_por_xpath(f"/html/body/div/form/fieldset/legend/img", timeout)
            
            # Digita Usuário
            self.bot.aguardar_elemento_por_xpath(f"//*[@id='email']", timeout)
            self.bot.digitar_por_xpath(f"//*[@id='email']", user)
            self.bot.aguardar_estado_documento()

            # Digita Senha
            self.bot.aguardar_elemento_por_xpath(f"//*[@id='password']", timeout)
            self.bot.digitar_por_xpath(f"//*[@id='password']", password)
            self.bot.aguardar_estado_documento()

            # Clicar em Entrar
            self.bot.aguardar_elemento_por_xpath(f"//*[@id='submit']", timeout)
            self.bot.clicar_por_xpath(f"//*[@id='submit']")
            self.bot.aguardar_estado_documento()
        except Exception as e:
            raise e

    def acessa_tela_cadastro(self):
        try:
            # Aguarda e Clica no Icone de Cadastro
            self.bot.aguardar_elemento_por_xpath(f"/html/body/nav/div/ul/li[1]/a", timeout)
            self.bot.clicar_por_xpath(f"/html/body/nav/div/ul/li[1]/a")
            self.bot.aguardar_estado_documento()
        except Exception as e:
            raise e

    def realiza_cadastro(self, dados):
        try:
            for _, row in dados.iterrows():

                # Captura Dados de Cada Linha
                Nome = row["Nome"]
                Email = row["Email"]
                Telefone = row["Telefone"]
                Cidade = row["Cidade"]
                Estado = row["Estado"]

                # Valida Tela de Cadastro
                self.bot.aguardar_elemento_por_xpath(f"/html/body/div/form/fieldset/legend/img", timeout)
                self.bot.aguardar_elemento_por_xpath(f"/html/body/div/form/fieldset/h5", timeout)

                # Insere Nome
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='nome']", timeout)
                self.bot.digitar_por_xpath(f"//*[@id='nome']", Nome)
                self.bot.aguardar_estado_documento()

                # Insere Email
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='email']", timeout)
                self.bot.digitar_por_xpath(f"//*[@id='email']", Email)
                self.bot.aguardar_estado_documento()

                # Insere Telefone
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='telefone']", timeout)
                self.bot.digitar_por_xpath(f"//*[@id='telefone']", Telefone)
                self.bot.aguardar_estado_documento()

                # Insere Cidade
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='cidade']", timeout)
                self.bot.digitar_por_xpath(f"//*[@id='cidade']", Cidade)
                self.bot.aguardar_estado_documento()

                # Insere Estado
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='estado']", timeout)
                self.bot.digitar_por_xpath(f"//*[@id='estado']", Estado)
                self.bot.aguardar_estado_documento()

                # Clica em Cadastrar
                self.bot.aguardar_elemento_por_xpath(f"//*[@id='submit']", timeout)
                self.bot.clicar_por_xpath(f"//*[@id='submit']")
                self.bot.aguardar_estado_documento()

                # Valida Cadastro
                self.bot.aguardar_elemento_por_xpath(f"/html/body/div/form/fieldset/p")

                # Atualiza Status na Planilha
                row["Status"] = "Cadastrado Com Sucesso"
            return dados
        except Exception as e:
            raise e




