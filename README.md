## como instalar:

funciona com Python 2.7 e Python 3.6 \o/

clone o projeto:

```
git clone https://github.com/berrondo/desafio-captura.git
```

crie e ative seu virtualenv ;-)

rode:

```
pip install -r requirements.txt
```

você vai precisar do Firefox e do driver para o selenium, o qual pode ser obtido aqui, entre drivers para outros browsers:

> http://seleniumhq.github.io/selenium/docs/api/py/#drivers

## funciona?... execute:

```
python test_crowler.py
```

## como usar:

no diretório do projeto, execute:

```
python crowler.py
```

o crowler populará um banco Sqlite com `nome, titulo e url` de todos os produtos do site [epocacosmeticos.com.br](http://www.epocacosmeticos.com.br/)

```
python csv.py
```

a partir do banco será gerado no diretório da aplicação um arquivo `.csv` separado por `;` com `nome, titulo e url` dos produtos.

## versão assíncrona:

há uma versão assíncrona incipiente do crowler em acrowler.py que somente funciona com Python 3.5+

## a melhorar:

  * abordagem naive para obtenção dos links baseada em regexes. há .group(1) diretamente no objeto match em alguns casos. funcionou para todo este site ;-)
  * melhorar estratégia de fixtures off-line (em banco?) para poder testar o crowler o o "csv"
  * parâmetros de linha de comando!
  * utilizar um log em vez dos prints
  * abordagem distribuída/assíncrona!