import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('meubanco.db')
cursor = conexao.cursor()

# Cria a tabela dos usuários
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conexao.commit()

# Função para adicionar um usuário
def adicionar_usuario(nome, email, senha):
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
    conexao.commit()

# Função para listar todos os usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f"\033[91m{usuario[0]}\033[0m  "  # ID Vermelho
              f"\033[32m{usuario[1]}\033[0m  "  # Nome Verde
              f"\033[34m{usuario[2]}\033[0m  "  # Email Azul
              f"\033[33m{usuario[3]}\033[0m  "  # Senha Amarelo
              f"\033[36m{usuario[4]}\033[0m")   # Data de criação Ciano

# Função para filtrar usuário
def filtrar_usuario_por_id_ou_nome(filtrar):
    if filtrar.isdigit():
        # Filtrar por ID
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (int(filtrar),))
    else:
        # Filtrar por nome
        cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + filtrar + '%',))

    resultados = cursor.fetchall()

    if resultados:
        for usuario in resultados:
            print(f"\033[91m{usuario[0]}\033[0m  "
                  f"\033[32m{usuario[1]}\033[0m  "
                  f"\033[34m{usuario[2]}\033[0m  "
                  f"\033[33m{usuario[3]}\033[0m  "
                  f"\033[36m{usuario[4]}\033[0m")
    else:
        print("Nenhum usuário encontrado com essa informação.")

# Função para atualizar um usuário
def atualizar_usuario(id, nome, email, senha):
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (nome, email, senha, id))
    conexao.commit()

# Função para deletar um usuário
def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()

# Função principal
def main():
    criar_tabela()

    while True:
        print("\nMenu:")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Filtrar usuário")
        print("6. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            adicionar_usuario(nome, email, senha)
            print("Usuário adicionado com sucesso!")

        elif opcao == '2':
            print("\033[92m\nLista de usuários:\033[0m")
            print("\033[91m●ID\033[0m", "\033[32m●Nome\033[0m", "\033[34m●Email\033[0m", "\033[33m●Senha\033[0m", "\033[36m●Data Criação\033[0m")
            listar_usuarios()

        elif opcao == '3':
            id = int(input("ID do usuário a ser atualizado: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            atualizar_usuario(id, nome, email, senha)
            print("Usuário atualizado com sucesso!")

        elif opcao == '4':
            id = int(input("ID do usuário a ser deletado: "))
            deletar_usuario(id)
            print("Usuário deletado com sucesso!")

        elif opcao == '5':
            filtrar = input("\nDigite o ID ou Nome do usuário: ")
            print("\033[92m\nResultados da busca:\033[0m")
            print("\033[91m●ID\033[0m", "\033[32m●Nome\033[0m", "\033[34m●Email\033[0m", "\033[33m●Senha\033[0m", "\033[36m●Data Criação\033[0m")
            filtrar_usuario_por_id_ou_nome(filtrar)

        elif opcao == '6':
            print("\n\033[91mO sistema foi encerrado!\033[0m")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a conexão ao final
    conexao.close()

# Executar o programa
if __name__ == "__main__":
    main()