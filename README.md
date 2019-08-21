# BibWorld

Sistema CRUD para gerenciamento de livros, com interface Desktop implementada na linguagem Python e armazenamento de dados no Firebase Realtime Database. O sistema foi desenvolvido como trabalho prático da disciplina de Sistemas Distribuídos.

Principais funcionalidades:
* Cadastro e alteração de dados do usuário;
* Cadastro, alteração, busca e remoção de livros, mediante autenticação do usuário.

## Iniciando o sistema

### Requisitos

Possuir uma conta no Firebase.

### Instalação

Inicialmente, realize o download da versão mais recente do projeto pelo nosso [repositório GitHub](<https://github.com/JedersonLuz/BibWorld>). Em seguida, é necessário fazer o download das bibliotecas [PyQt5](<https://pypi.org/project/PyQt5/>) e [pyrebase](<https://github.com/thisbejim/Pyrebase>), através dos seguintes comandos:
    
    pip install PyQt5
    pip install pyrebase

### Execução

Para inicializar o sistema, execute a classe principal do projeto, através do comando:

    python3 stackmainwindow.py

A primeira tela exibida pelo sistema é a tela de login, responsável por realizar a autenticação do usuário e permitir seu acesso à aplicação. Caso o usuário ainda não possua uma conta, poderá efetuar seu cadastro ao pressionar o botão "Cadastre-se".

## Desenvolvedores

* Açucena Rodrigues dos Santos Soares - [acucenarodrigues1998](<https://github.com/acucenarodrigues1998/>)
* Jederson Sousa Luz - [JedersonLuz](<https://github.com/JedersonLuz/>)
* Vitória de Carvalho Brito - [VitoriaCarvalho](<https://github.com/VitoriaCarvalho/>)

## Licença

[MIT](https://github.com/JedersonLuz/BibWorld/blob/master/LICENSE)
