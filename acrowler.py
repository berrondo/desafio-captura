#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.stdout.flush()

from db import db
import signal
import asyncio
import aiohttp

from re import findall

from padroes import *

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def adowloader(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def detalhes(link_para_o_produto):
    texto = await adowloader(client, link_para_o_produto)
    match_title = PADRAO_DE_TITULO.search(texto.decode('utf-8'))
    titulo = None
    if match_title:
        titulo = match_title.group(1)
    print([titulo, titulo, link_para_o_produto])


async def produtos(client, subdepartamento):
    texto = await adowloader(client, subdepartamento)
    links = findall(PADRAO_DE_LINK_PARA_PRODUTO, texto.decode('utf-8'))
    for produto in links:
        await detalhes(produto)


async def subdepartamentos(client, home):
    texto = await adowloader(client, home)
    subdepts = PADRAO_DE_SUBDEPARTAMENTOS.search(texto.decode('utf-8')).group(1)
    subdepts = findall(PADRAO_DE_LINK_PARA_SUBDEPARTAMENTOS, subdepts)
    for subdept in subdepts:
        print(subdept)
        await produtos(client, subdept)


def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# asyncio.ensure_future(subdepartamentos(client, 'http://www.epocacosmeticos.com.br'))

subdepts = [
    'http://www.epocacosmeticos.com.br/perfumes',
    'http://www.epocacosmeticos.com.br/maquiagem',
    'http://www.epocacosmeticos.com.br/cabelos',
    'http://www.epocacosmeticos.com.br/dermocosmeticos',
    'http://www.epocacosmeticos.com.br/tratamentos',
    'http://www.epocacosmeticos.com.br/corpo-e-banho',
    'http://www.epocacosmeticos.com.br/unhas',
    'http://www.epocacosmeticos.com.br/selecao/ofertas'
]

for subdept in subdepts:
    asyncio.ensure_future(produtos(client, subdept))

loop.run_forever()
