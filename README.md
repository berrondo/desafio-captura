## como instalar:

funciona com Python 2.7

clone o projeto:

```
git clone https://github.com/berrondo/desafio-captura.git
```

crie e ative seu virtualenv ;-)

rode:

```
pip install requirements.txt
```

você vai precisar do Firefox e do driver para o selenium, o qual pode ser obtido aqui, entre drivers para outros browsers:

```
http://seleniumhq.github.io/selenium/docs/api/py/#drivers
```

## funciona?... execute:

```
python test_crowler.py
```

## como usar:

no diretório do projeto, execute:

```
python crowler.py
```

o crowler populará um banco Sqlite com nome, titulo e url de todos os produtos do site epocacosmeticos.com.br

```
python csv.py
```

a partir do banco será gerado no diretório da aplicação um arquivo .csv separado por ; com nome, titulo e url dos produtos

## a melhorar:

...