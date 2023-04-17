import time
import pytest
from pages.login_page import LoginPage


@pytest.mark.userfixtures("setup_teardown")
@pytest.mark.login
class TestCT003:
    def test_ct003_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        # Instacia os objetos a serem usados no teste
        login_page = LoginPage()

        # Faz o logn
        login_page.fazer_login("standaerd_user", "senha_incorreta")

        # Verificar se o lign não foi realizado e a mensagem de erro apareceu
        login_page.verificar_mensagem_erro_login_existe()
        time.sleep(2)

        # Verifica o texto da mensagem de erro
        login_page.verificar_mensagem_erro_login()

