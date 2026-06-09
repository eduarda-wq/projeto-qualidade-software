import pytest
from tests.pages.home_page import HomePage
from tests.pages.login_page import LoginPage

def test_busca_e2e_playwright(page):
    
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.wait_for_timeout(2000)
    
    
    if "login" in page.url:
        login = LoginPage(page)
        login.fazer_login("amanda@teste.com", "12345")
        page.wait_for_timeout(3000) 

   
    home = HomePage(page)
    home.realizar_busca("Italiana")
    page.wait_for_timeout(2000) 
    
   
    assert page.locator("text=Italiana").is_visible()