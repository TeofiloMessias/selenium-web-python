import time
import pytest

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.userfixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestCToo1:
    def test_ct001_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"

        # Fazendo Login
        login_page.fazer_login("standard_user", "secret_sauce")
        time.sleep(2)

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)
        time.sleep(2)

        # Verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_se_elemento_existe(produto_1)
        time.sleep(2)

        # Clicar para voltar a tela de produtos
        carrinho_page.clicar_continuar_comprando()
        time.sleep(2)

        # Adicionar mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)
        time.sleep(2)

        #Verificar que os 2 produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_se_elemento_existe(produto_1)
        carrinho_page.verificar_se_elemento_existe(produto_2)
        time.sleep(2)
