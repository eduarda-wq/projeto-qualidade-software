
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.campo_email = page.locator("#loginEmail")
        self.campo_senha = page.locator("#loginPassword")
        
       
        self.botao_entrar = page.locator("#loginForm").get_by_role("button", name="Entrar")

    def fazer_login(self, email: str, senha: str):
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()