#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs


def arquivo_csv(bd, separador=';'):
    csv = separador.join(('nome', 'titulo', 'url'))
    for rs in bd.select():
        if rs[0]:
            linha = separador.join((rs[0], rs[1], rs[2]))
            csv += '\n'+linha
            print '+',
    with codecs.open('epoca_cosmeticos.csv', 'w', encoding='utf8') as arq:
        arq.write(csv)

        
if __name__ == '__main__':
    from db import db
    arquivo_csv(db)