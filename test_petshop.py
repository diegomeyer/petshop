import unittest
from petshop import Produto, Crawler


class ProdutoTest(unittest.TestCase):

    def test_criar_produto(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url)
        self.assertEqual(produto.get_nome(),  'racao')
        self.assertEqual(produto.get_url(), url)

    def test_set_get_codigo(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url)
        self.assertEqual(produto.get_nome(), 'racao')
        self.assertEqual(produto.get_url(), url)

        codigo = 1111
        self.assertEqual(produto.get_codigo(),  "")
        produto.set_codigo(codigo)
        self.assertEqual(produto.get_codigo(), codigo)

    def test_set_get_preco(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url)
        self.assertEqual(produto.get_nome(), 'racao')
        self.assertEqual(produto.get_url(), url)

        preco = 100.00
        self.assertEqual(produto.get_preco(),  "")
        produto.set_preco(preco)
        self.assertEqual(produto.get_preco(), preco)

    def test_set_get_detalhe(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url)
        self.assertEqual(produto.get_nome(), 'racao')
        self.assertEqual(produto.get_url(), url)
   
        detalhe = 'mais detalhes'
        self.assertEqual(produto.get_detalhe(),  "")
        produto.set_detalhe(detalhe)
        self.assertEqual(produto.get_detalhe(), detalhe)

        preco = float(1000.123)
        produto.set_preco(preco)
        self.assertEqual(produto.get_preco(), 1000.12)

        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto2 = Produto(nome, url)
        self.assertEqual(produto.get_nome(), 'racao')
 

        detalhe = 'ração special dog, para o seu cachorro'
        self.assertEqual(produto2.get_detalhe(),  "")
        produto2.set_detalhe(detalhe)
        self.assertEqual(produto2.get_detalhe(), 'racao special dog para o seu cachorro')

        preco = '1000,123'
        produto2.set_preco(preco)
        self.assertEqual(produto.get_preco(), 1000.12)


class CrawlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.crawler = Crawler('https://www.extra.com.br/', 5)

    def test_buscar(self):
        gabarito = 'https://buscando2.extra.com.br/busca?q=Pet%20Shop&common_filter%5B1%5D=146093'
        url_categoria = self.crawler.buscar_pagina_categoria('Pet Shop')
        self.assertEqual(url_categoria, gabarito)
