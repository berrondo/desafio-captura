#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import findall
from sqlite3 import IntegrityError

import requests
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, WebDriverException

from navegador.navegador import Navegador
from padroes import *


def downloader_alternativo(caminho):
    if caminho.startswith(r'file:///'):
        caminho = caminho.replace(r'file:///', '')
        with open(caminho, 'r') as arq:
            conteudo = arq.read()
            return unicode(conteudo, 'utf-8')
    return requests.get(caminho).text


def downloader(url, mostrar_mais=False):
    if not mostrar_mais:
        return downloader_alternativo(url)

    browser = Navegador.get_browser()
    browser.get(url)
    while True:
        try:
            elem = browser.find_element_by_xpath('//span[contains(text(), "MOSTRAR MAIS PRODUTOS")]')
            elem.click()
            print '^',
        except NoSuchElementException:
            break
        except ElementNotInteractableException:
            break
        except WebDriverException:
            break
    conteudo = browser.page_source
    Navegador.quit()
    return conteudo


def subdepartamentos(home):
    subdepts = PADRAO_DE_SUBDEPARTAMENTOS.search(downloader(home)).group(1)
    links = findall(PADRAO_DE_LINK_PARA_SUBDEPARTAMENTOS, subdepts)
    return reversed(links)


def produtos(subdepartamento, mostrar_mais=False):
    texto = downloader(subdepartamento, mostrar_mais=mostrar_mais)
    return findall(PADRAO_DE_LINK_PARA_PRODUTO, texto)

    
def detalhes(link_para_o_produto):
    produto = downloader(link_para_o_produto)
    
    match_title = PADRAO_DE_TITULO.search(produto)
    match_nome = PADRAO_DE_NOME.search(produto)

    titulo = nome = None
    if match_title:
        titulo = match_title.group(1)
    if match_nome:
        nome = match_nome.group(1)

    return [nome, titulo, link_para_o_produto]


def crowler(home, bd, mostrar_mais=False):
    for subdepartamento in subdepartamentos(home):
        print '[%s]' % subdepartamento,
        for link_para_produto in produtos(subdepartamento, mostrar_mais=mostrar_mais):
            if not bd.exists(link_para_produto):
                linha = detalhes(link_para_produto)
                linha.append(subdepartamento)
                try:
                    bd.insert(*linha)
                    print '.',
                except IntegrityError:
                    print '!',  # log url duplicada!
            else:
                print '!',  # log url duplicada!
    Navegador.quit()


if __name__ == '__main__':
    from db import db
    crowler('http://epocacosmeticos.com.br', db, mostrar_mais=False)
    Navegador.quit()
