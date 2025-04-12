# Atividade-Python_Banco_de_Dados

1. Introdução

O projeto foi feito com o intuito principal para desenvolver um sistema de gerenciamento de usuários usando python e banco de dados como foi passado em sala de aula. O sistema foi feito com base na praticidade em cadastrar pessoas em um banco de dados e ter facilidade em manipular dados como Id, nome, email, senha do usuário e visualizar a data e horário do cadastro do usuário.


---

2. Estrutura do Banco de Dados

CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )


---

3. Bibliotecas Utilizadas

sqlite3: Biblioteca padrão do Python utilizada para interagir com o banco de dados SQLite.


---

<p align="center">
<img src="Captura de tela 2025-04-11 203642.png" width="500"        
</p>

        

4. Funcionalidades Implementadas

Menu de Opções

O sistema apresenta um menu no terminal com as opções:

1. Adicionar usuário


2. Listar usuários


3. Atualizar usuário


4. Deletar usuário


5. Filtrar usuário por ID ou nome


6. Sair



Adição de Usuário

Solicita nome, email e senha e insere o usuário na tabela.


Listagem de Usuários

Mostra todos os usuários cadastrados, com ID, nome, email, senha e data de criação, formatados com cores no terminal.


Atualização de Usuário

Permite alterar nome, email e senha de um usuário com base no seu ID.


Exclusão de Usuário

Deleta um usuário com base no seu ID.


Filtro por ID ou Nome

Permite buscar usuários pelo ID ou por parte do nome, exibindo os dados encontrados com formatação colorida.

