import sys
import os

arquivo = 'users.txt'

def exibir_menu():
    print("Menu:")
    print("1. Cadastrar Novo Usuário")
    print("2. Autenticar Usuário")
    print("3. Sair")

def verificar_usuario(arquivo_usuarios, usuario_atual):
    for i in arquivo_usuarios:
        linha = i.split(',')
        usuario = linha[0]
        senha = linha[1]
        if usuario == usuario_atual:
            return True
        else:
            return False
    

def cadastrar_usuario(arquivo_usuarios):
    usuario_existe = verificar_usuario(arquivo_usuarios)
    
    pass

def autenticar_usuario():
    # Lógica para exibir as tarefas existentes
    print("Tarefas existentes:")
    print("- Tarefa 1")
    print("- Tarefa 2")



def main():
    
    try:
        arquivo_usuarios = open(arquivo, 'r+')
        print("Aberto arquivo de usuários")
    except FileNotFoundError:
        arquivo_usuarios = open(arquivo, 'w+')
        print("Criado arquivo de usários")
    
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuario_atual = 'pedro'
            cadastrar_usuario(arquivo_usuarios, usuario_atual)
        elif opcao == "2":
            autenticar_usuario()
        elif opcao == "3":
            arquivo_usuarios.close()
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()