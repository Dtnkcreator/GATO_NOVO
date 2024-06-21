from gato_class import Gato
from usuario_class import Usuario

def salva_gato(usuario:Usuario,gato:Gato):
    with open('usuarios_texto.txt', 'a') as file:
        file.write(f'Gato: {usuario.nome}=nome:{gato.nome};idade:{gato.idade};cor do pelo:{gato.cor}\n')
def salva_usuario(usuario:Usuario):
    with open('usuarios_texto.txt', 'a') as file:
        file.write(f'Usuario:{usuario.nome};Senha:{usuario.senha}\n')

def salva_lista_gato(list_gato:list[Gato]):
    with open ("usuarios_texto.txt", 'r') as file:
        for gato in list_gato:
            salva_gato(gato)
