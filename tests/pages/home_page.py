class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://local-eats-unisenac.vercel.app/"
     
        self.campo_busca = page.get_by_role("textbox")
        self.botao_buscar = page.get_by_role("button", name="Buscar")

    def navegar(self):
        self.page.goto(self.url)

    def realizar_busca(self, termo: str):
        self.campo_busca.fill(termo)
        self.botao_buscar.click()