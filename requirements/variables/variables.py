from dotenv import load_dotenv
import os

load_dotenv()

class ConfigVariaveis():
    def __init__(self):
        self.url_site = os.getenv("URL")
        self.usuario = os.getenv("USER")
        self.senha = os.getenv("PASSWORD")