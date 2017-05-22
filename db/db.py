#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('produtos.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS links (nome text, titulo text, url text UNIQUE, subdepartamento text)''')
c.execute('''CREATE TABLE IF NOT EXISTS web (link text UNIQUE, html text, callback text)''')


def insert(nome, titulo, url, subdepartamento):
    c.execute("INSERT INTO links VALUES (?, ?, ?, ?)", (nome, titulo, url, subdepartamento))
    con.commit()


def select():
    return c.execute('SELECT * from links').fetchall()


def exists(url):
    return c.execute('SELECT * from links where url=?', (url, )).fetchone()


def delete():
    c.execute('DELETE FROM links')
    con.commit()


def close():
    con.close()
