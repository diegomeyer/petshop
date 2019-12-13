from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import datetime
import time
from urllib.request import urlopen
import xlsxwriter
import requests


class Produto():

    def __init__(self, nome, url):
        self._nome = nome
        self._url = url
        self._codigo = ""
        self._preco = ""
        self._detalhe = ""

    def get_nome(self):
        return self._nome

    def get_url(self):
        return self._url

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_preco(self, preco):
        self._preco = preco

    def get_preco(self):
        return self._preco

    def set_detalhe(self, detalhe):
        self._detalhe = detalhe

    def get_detalhe(self):
        return self._detalhe


class WebCrawler():

    def __init__(self):
        self._implicitly_time = 75
        self._options = webdriver.FirefoxOptions()
        self.set_options()
        self.set_webdriver()

    def set_options(self):
        print('Criando Options')
        self._options.add_argument('--headless')
        self._options.add_argument('--disable-extensions')
        # self._options.add_argument("--window-size=1920x1080")
        self._options.add_argument("--no-sandbox")
        self._options.add_argument("--disable-gpu")
        self._options.add_argument("--start-maximized")

    def set_webdriver(self):
        print('Criando WebDriver Firefox')
        try:
            self.drive = webdriver.Firefox(options=self._options)
            # self.drive = webdriver.Firefox()
            self.drive.set_page_load_timeout(self._implicitly_time)
            self.drive.implicitly_wait(self._implicitly_time)
            wait = WebDriverWait(self.drive, 60)
        except Exception as E:
            print(E)
            print("Erro ao iniciar drive")


class Crawler(WebCrawler):

    def __init__(self, url, num_paginas):
        super().__init__()
        self.url = url
        self.num_paginas = num_paginas
        self._tempo_espera = 10

    def buscar_pagina_categoria(self, categoria):
        self.drive.get(self.url)

        pesquisa = self.drive.find_element_by_xpath('//*[@id="strBusca"]')
        pesquisa.send_keys(categoria)

        buscar_btn = self.drive.find_element_by_xpath('//*[@id="btnOK"]')
        buscar_btn.click()

        url_categoria = self.drive.current_url
        print(url_categoria)

        mais_categorias = self.drive.find_element_by_xpath('//*[@id="neemu-search-filters"]/li[1]/a')
        mais_categorias.click()

        categoria_cachorro = self.drive.find_element_by_xpath('//*[@id="neemu-search-filters"]/li[1]/ul/li[1]/ul/li[1]/ul/li[6]/a')
        categoria_cachorro.click()
        time.sleep(self._tempo_espera)

        url_categoria_cachorro = self.drive.current_url
        print(url_categoria_cachorro)

        return url_categoria_cachorro

    def buscar_produtos(self, url):
        produtos = list()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_nome = soup.findAll("div",  {"class": "nm-product-name"})
        for nome in div_nome:
            urls = nome.find('a', href=True)
            produtos.append(Produto(urls.text, 'https:' + urls['href']))
        return produtos

    def buscar_detalhes(self, produto):
        print(produto.get_nome(), produto.get_url())
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(produto.get_url(), headers=user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

if __name__ == "__main__":
    produtos = list()

    crawler = Crawler('https://www.extra.com.br/',  5)
    print('Buscando URL categoria')
    url_categoria = crawler.buscar_pagina_categoria('Pet Shop')

    if url_categoria:
        for numeracao in range(1, crawler.num_paginas+1):
            url_produtos_pagina = url_categoria + '&page={}'.format(numeracao)
            print(url_produtos_pagina)
            produtos += crawler.buscar_produtos(url_produtos_pagina)

    for produto in produtos:
        crawler.buscar_detal9hes(produto)
