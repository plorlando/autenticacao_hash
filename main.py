import sys
import os
import hashlib

arquivo = 'users.txt'

# VERIFICA SE O ARQUIVO DE USUARIOS EXISTE, SENÃO O CRIA
if not os.path.isfile(arquivo):
    with open(arquivo, 'w') as a:
        a.write("usuario,senha")


# FUNÇÃO PARA EXIBIR O MENU
def exibir_menu():
    os.system('clear')
    print("Menu:")
    print("1. Cadastrar Novo Usuário")
    print("2. Autenticar Usuário")
    print("3. Sair")


# FUNÇÃO PARA VERIFICAR SE O USUÁRIO JÁ EXISTE NO ARQUIVO
def verificar_usuario(a, usuario_atual):
    for i in a:
        linha = i.split(',')
        usuario = linha[0]
        senha = linha[1]
        if usuario == usuario_atual:
            return True
        
    return False
    

# FUNÇÃO PARA CADASTRAR UM USUÁRIO
def cadastrar_usuario(usuario_atual):
    with open(arquivo, 'r+') as a:
        usuario_existe = verificar_usuario(a, usuario_atual)

        # HASH DE SENHA PARA REGISTRAR O USUÁRIO
        if usuario_existe:
            input("Falha ao cadastrar. Já existe um usuário com esse nome. Pressione ENTER para continuar...")
        else:
            senha_confirma, senha = confirma_senha()
            senha_hashed = hashlib.md5(senha.encode())

            if senha_confirma:
                a.write(f"\n{usuario_atual.rstrip().lstrip()},{senha_hashed.hexdigest()}")
                a.flush()
                input("Usuário cadastrado com sucesso. Pressione ENTER para continuar...")
            else:
                input("As senhas não conferem! Pressione ENTER para continuar...")
            

        
# FUNÇÃO PARA CONFIRMAR SE A SENHA ESTÁ CORRETA
def confirma_senha():
    
    condicao_senha = False
    
    while condicao_senha == False:
        senha_atual = input("Insira uma senha com pelo menos 8 digitos: ").rstrip().lstrip()
        
        if len(senha_atual) < 8:
            condicao_senha = False
        else:
            condicao_senha = True
        
    confirma_senha = input("Confirme a senha: ").rstrip().lstrip()
    
    if senha_atual == confirma_senha:
        return True, senha_atual
    else:
        return False, None


# FUNÇÃO PARA AUTENTICAR O USUÁRIO, FAZENDO A CONSULTA COM A SENHA HASH
def autenticar_usuario():
    usuario_atual = input("Usuário: ").rstrip().lstrip()
    senha_atual = input("Senha: ").rstrip().lstrip()
    senha_atual_hased = hashlib.md5(senha_atual.encode()).hexdigest()

    with open(arquivo, 'r+') as a:
        for i in a:
            
            linha = i.split(',')
            usuario = linha[0]
            senha = linha[1]
            # print(f"USUARIO: {usuario} USUARIO ATUAL: {usuario_atual} SENHA: {senha} SENHA ATUAL: {senha_atual}")

            if usuario == usuario_atual and senha == senha_atual_hased:
                return True, usuario_atual, senha_atual
            
        return False, usuario_atual, senha_atual


# CHAMA O MENU
def main():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuario_atual = input("Digite um nome para seu usuário: ").rstrip().lstrip()
            cadastrar_usuario(usuario_atual)
        elif opcao == "2":
            autenticado, usuario_atual, senha_atual = autenticar_usuario()

            if autenticado:
                input("Usuário autenticado com sucesso. Pressione ENTER para continuar...")
            else:
                input("Falha na autenticação. Usuário ou senha incorretos. Pressione ENTER para continuar...")


        elif opcao == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente. Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()