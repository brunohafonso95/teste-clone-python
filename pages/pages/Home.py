from Pyautomators.web_extensao import Tipos_de_elemento

class Home:
    MENU = 'no-food-menu_link js-toggle-sub-menu'
    ELETRONICOS = 'Tecnologia e Eletrônicos'
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def ir_home(self):
        self.driver.pagina(self.url)
        self.driver.maximiza()

    def selecionar_item_menu(self, tipo):
        self.driver.clica(MENU, Tipos_de_elemento.CLASS_NAME, 5)
        if(tipo=='ELETRONICOS'):
            self.driver.clica(ELETRONICOS, Tipos_de_elemento.LINK_TEXT, 5)
