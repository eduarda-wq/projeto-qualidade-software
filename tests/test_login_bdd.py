
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage

scenarios('features/login.feature')


@given('que eu acesso o sistema LocalEats')
def acessar_sistema(page):
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.wait_for_timeout(2000)

@when('sou redirecionado para a tela de login')
def verificar_tela_login(page):
    assert "login" in page.url

@when(parsers.parse('preencho o email "{email}" e a senha "{senha}"'))
def preencher_credenciais(page, email, senha):
    login = LoginPage(page)
   
    login.campo_email.fill(email)
    login.campo_senha.fill(senha)

@when('clico no botão Entrar')
def clicar_entrar(page):
    login = LoginPage(page)
    login.botao_entrar.click()
    page.wait_for_timeout(3000) 

@then('devo ser autenticado com sucesso e ver a barra de busca')
def verificar_autenticacao_sucesso(page):
   
    assert "login" not in page.url
    
    
    home = HomePage(page)
    assert home.campo_busca.is_visible()