import sys
import os
import hashlib

arquivo = 'users.txt'

if not os.path.isfile(arquivo):
    with open(arquivo, 'w') as a:
        a.write("usuario,senha")

def exibir_menu():
    print("Menu:")
    print("1. Cadastrar Novo Usuário")
    print("2. Autenticar Usuário")
    print("3. Sair")

def verificar_usuario(a, usuario_atual):
    for i in a:
        linha = i.split(',')
        usuario = linha[0]
        senha = linha[1]
        if usuario == usuario_atual:
            return True
        
    return False
    

def cadastrar_usuario(usuario_atual):
    with open(arquivo, 'r+') as a:
        usuario_existe = verificar_usuario(a, usuario_atual)

        if usuario_existe:
            print("Falha ao cadastrar. Já existe um usuário com esse nome.")
        else:
            senha_confirma, senha = confirma_senha()
            senha_hashed = hashlib.md5(senha.encode())
            print(senha_hashed)

            if senha_confirma:
                a.write(f"\n{usuario_atual.rstrip().lstrip()},{senha.rstrip().lstrip()}")
                a.flush()
                input("Usuário cadastrado com sucesso. Pressione qualquer tecla para continuar...")
            else:
                input("As senhas não conferem! Pressione qualquer tecla para continuar...")
            
        
def confirma_senha():

    senha_atual = input("Insira uma senha com pelo menos 8 digitos: ")
    confirma_senha = input("Confirme a senha: ")

    if senha_atual == confirma_senha:
        return True, senha_atual
    else:
        return False, None


def autenticar_usuario():
    usuario_atual = input("Usuário: ")
    senha_atual = input("Senha: ")

    with open(arquivo, 'r+') as a:
        for i in a:
            
            linha = i.split(',')
            usuario = linha[0]
            senha = linha[1]
            # print(f"USUARIO: {usuario} USUARIO ATUAL: {usuario_atual} SENHA: {senha} SENHA ATUAL: {senha_atual}")

            if usuario == usuario_atual and senha == senha_atual:
                return True, usuario_atual, senha_atual
            
        return False, usuario_atual, senha_atual


def main():
        
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuario_atual = input("Digite um nome para seu usuário: ")
            cadastrar_usuario(usuario_atual)
        elif opcao == "2":
            autenticado, usuario_atual, senha_atual = autenticar_usuario()

            if autenticado:
                input("Usuário autenticado com sucesso. Pressione qualquer tecla para continuar...")
            else:
                input("Falha na autenticação. Usuário ou senha incorretos. Pressione qualquer tecla para continuar...")


        elif opcao == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()