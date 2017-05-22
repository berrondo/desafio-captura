#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from crowler import subdepartamentos, produtos, detalhes


class TestExtracaoDeDadosDoProduto(unittest.TestCase):

    cwd = os.getcwd()
    home = r'file:///%s/fixtures/home.html' % cwd
    pagina_do_produto = 'file:///%s/fixtures/um_perfume.html' % cwd

    def test_obtem_links_para_os_sub_departamentos_na_home(self):

        links_para_subdepartamentos = subdepartamentos(self.home)
        
        self.assertEqual([
            'http://www.epocacosmeticos.com.br/perfumes',
            'http://www.epocacosmeticos.com.br/maquiagem',
            'http://www.epocacosmeticos.com.br/cabelos',
            'http://www.epocacosmeticos.com.br/dermocosmeticos',
            'http://www.epocacosmeticos.com.br/tratamentos',
            'http://www.epocacosmeticos.com.br/corpo-e-banho',
            'http://www.epocacosmeticos.com.br/unhas',
            'http://www.epocacosmeticos.com.br/selecao/ofertas'
        ], links_para_subdepartamentos)
        
    def test_obtem_links_para_produtos_de_cada_subdepartamento(self):
    
        subdepartamento = r'file:///%s/fixtures/perfumes.html' % self.cwd
        links_para_produtos = produtos(subdepartamento)
        
        self.assertEqual(20, len(links_para_produtos))
        self.assertEqual([
            'http://www.epocacosmeticos.com.br/good-girl-eau-de-parfum-carolina-herrera-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/sexy-woman-night-eau-de-toilette-paris-elysees-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/nuit-rose-limited-edition-deo-colonia-fiorucci-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/l-eau-par-kenzo-mirror-edition-pour-femme-eau-de-toilette-kenzo-perfume-feminino-/p',
            'http://www.epocacosmeticos.com.br/very-irresistible-l-eau-en-rose-eau-de-toilette-givenchy-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/la-vie-est-belle-eau-de-parfum-lancome-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/amor-amor-eau-de-toilette-cacharel-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/billion-woman-eau-de-toilette-paris-elysees-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/1-million-eau-de-toilette-paco-rabanne-perfume-masculino/p',
            'http://www.epocacosmeticos.com.br/sexy-woman-eau-de-toilette-paris-elysees-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/lady-gaga-fame-eau-de-parfum-lady-gaga-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/jus-de-fleurs-eau-de-toilette-blumarine-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/paris-deo-colonia-fiorucci-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/majestic-pour-femme-deo-colonia-fiorucci-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/legend-angel-eau-de-parfum-lonkoom-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/demeanor-eau-de-toilette-lonkoom-perfume-masculino/p',
            'http://www.epocacosmeticos.com.br/intense-for-woman-eau-de-parfum-animale-perfume-feminino-100ml/p',
            'http://www.epocacosmeticos.com.br/bebe-desire-eau-de-parfum-bebe-perfume-feminino/p',
            'http://www.epocacosmeticos.com.br/vodka-brasil-yellow-eau-de-toilette-paris-elysees-perfume-masculino/p',
            'http://www.epocacosmeticos.com.br/212-vip-rose-eau-de-parfum-carolina-herrera-perfume-feminino/p',
        ], links_para_produtos)

    def test_extracao_dos_detalhes_do_produto_para_a_linha_do_arquivo_csv(self):

        linha_csv = detalhes(self.pagina_do_produto)

        self.assertEqual(
            [u'Hypn\xf4se Lanc\xf4me - Perfume Feminino - Eau de Toilette - 30ml',
             u'Hypn\xf4se Lanc\xf4me - Perfume Feminino - Eau de Toilette - 30ml',
            r'file:///%s/fixtures/um_perfume.html' % self.cwd]
            , linha_csv)


if __name__ == '__main__':
    unittest.main()