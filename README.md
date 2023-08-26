# Template de projeto Python3 com Flask e Flask-RESTX

Abaixo está descrito o passo a passo para configurar o ambiente de desenvolvimento e executar o projeto.

1. Crie o ambiente virtual:
```
python3 -m venv venv
```

2. Ative o ambiente virtual:
```
source venv/bin/activate
```

3. Instale as dependências do projeto:
```
pip install -r requirements.txt
```

4. Instale as dependências de desenvolvimento:
```
pip install -r requirements-dev.txt
```

5. Instale os hooks de pre-commit:
```
pre-commit install
```

6. Execute o projeto
```
python3 run.py
```
___
***Observações:***

* Alguns comandos podem variar no Windows (consulte a documentação oficial das ferramentas);
* Caso o comando `python3` não funcione, tente utilizar apenas `python`;
* Caso o comando `pip` não funcione, tente utilizar `pip3`.

***Comandos úteis:***

* `pre-commit run --all-files`: executa os hooks de pre-commit em todos os arquivos do projeto;
* `pytest .`: executa todos os testes do projeto;
* `python3 -m flake8 src/`: executa o flake8 em todos os arquivos dentro de **src**;
* `python3 - m black src/`: executa o black em todos os arquivos dentro de **src**.
