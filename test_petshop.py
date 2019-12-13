import unittest
from petshop import Produto, Crawler

class ProdutoTest(unittest.TestCase):

    def test_criar_produto(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url )
        self.assertEqual(produto.get_nome(), nome)
        self.assertEqual(produto.get_url(), url)

    def test_set_get_codigo(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url )
        self.assertEqual(produto.get_nome(), nome)
        self.assertEqual(produto.get_url(), url)

        codigo = 1111
        self.assertEqual(produto.get_codigo(),  "")
        produto.set_codigo(codigo)
        self.assertEqual(produto.get_codigo(), codigo)

    def test_set_get_preco(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url )
        self.assertEqual(produto.get_nome(), nome)
        self.assertEqual(produto.get_url(), url)

        preco = 100.00
        self.assertEqual(produto.get_preco(),  "")
        produto.set_preco(preco)
        self.assertEqual(produto.get_preco(), preco)

    def test_set_get_detalhe(self):
        nome = 'Ração'
        url = 'http://extra.com.br/ração'
        produto = Produto(nome, url )
        self.assertEqual(produto.get_nome(), nome)
        self.assertEqual(produto.get_url(), url)

        detalhe = 'mais detalhes'
        self.assertEqual(produto.get_detalhe(),  "")
        produto.set_detalhe(detalhe)
        self.assertEqual(produto.get_detalhe(), detalhe)



class CrawlerTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.crawler = Crawler('https://www.extra.com.br/')


    def test_buscar(self):
        self.crawler.buscar_pagina_produto()
        self.assertEqual(True,True)