#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import compile

PADRAO_DE_TITULO = compile(r'<meta property="og:title" content="(.*?)"')
PADRAO_DE_NOME = compile(r'<meta property="product:plural_title" content="(.*?)"')

PADRAO_DE_SUBDEPARTAMENTOS = compile(r'<ul class="sub_dept">(.*?)</ul>')
PADRAO_DE_LINK_PARA_SUBDEPARTAMENTOS = compile(r'<li><a href="(.*?)">(?:.*?)</a></li>')

PADRAO_DE_LINK_PARA_PRODUTO = compile(r'<a href="(http://www.epocacosmeticos.com.br/.*?/p)"(?:[ \n]*)class="comprar">COMPRAR</a>')

