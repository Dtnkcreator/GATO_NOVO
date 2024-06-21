from usuario_class import Usuario
from gato_class import Gato
from salvas import salva_usuario
from salvas import salva_lista_gato

def ler_dados():

    with open('GATO_NOVO/usuarios_texto.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Usuario:'):
            atributos = line.strip().split('Usuario:')[1]
            usuario_nome = atributos.split(';')[0]
            usuario_senha = atributos.split(':')[1]
            usuarinho = Usuario(usuario_nome,usuario_senha)
            return usuarinho
        
        if line.startswith('Gato:'):
            atributos = line.strip().split('Gato:')[1]
            gato_nome = atributos.strip().split('=')[1].split(",")[0]
            gato_idade = atributos.strip().split('=')[1].split(",")[1]
            gato_cor = atributos.strip().split('=')[1].split(",")[2]
            gatinho = Gato(gato_nome, gato_idade, gato_cor)
            return gatinho
            

def adicionar_usuario(usuarios):
    nome = input("Novo nome de usuário: ")
    senha = input("Nova senha: ")
    usuarios.append(Usuario(nome,senha))
    salva_usuario(usuarios)

def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def main():
    usuarios = []
    gatos = []
    #usuarios, gatos = ler_dados()

    print("Bem-vindo a Clínica de Gatos!\n")
    print("Escolha o que deseja fazer: \n1.Adicionar Usuário \n2.Login \n3.Sair")
    escolha = int(input("Escolha a alternativa desejada: "))

    match escolha:
         
            case 1:
                adicionar_usuario(usuarios)


            case 2:
                login(usuarios)
                while True:
                    print("Login realizado com sucesso!")
                    print("1. Ver Informações do Pet\n2. Adicionar Informações de seu gato\n3. Sair\n")
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                         for info in gatos:
                                    print(info)
                                    if not info in gatos:
                                        print("Não há informações de seu pet. Adicione por favor!")
                                        break
                        
                    if opcao == '2':
                        print("Informações do pet:\n")
                        
                        info_gato = input("Adicione nome, peso e cor do seu pet: ")
                        gatos.append(Gato(info_gato))

                    elif opcao == '3':
                        salva_lista_gato(gatos)
                        salva_usuario(usuarios)
                        print("Dados salvos. Saindo...")
                        break
                    else:
                        print("Algo deu errado.")

                if not login(usuarios):
                    print("Usuário ou senha incorretos.")
                    return quit



            case 3:
                print("Fechando...")
                quit



            case _:
                print("\nALGO ESTÁ INCORRETO, TENTE NOVAMENTE!\n")
                quit
main()