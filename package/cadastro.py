from connections import ConnectionLivro, ConnectionUsers

def cadastrar_usuario(nome_usuario: str, nascimento_usuario: str, email_usuario: str, cpf_usuario: str, numero_usuario: int) -> bool:
    if encontrar_usuario(nome_usuario, cpf_usuario):
        con = ConnectionUsers()
        con.insert(nome_usuario, cpf_usuario, numero_usuario, email_usuario, nascimento_usuario)
        return True
    
    return False

def cadastrar_livro(titulo:str, autor:str, genero:str, valor:float) -> bool:
    if encontrar_livro(titulo, autor):
        con = ConnectionLivro()
        return True
    
    return False

def encontrar_usuario(nome_usuario: str, cpf_usuario: str) -> bool:
    con = ConnectionUsers()
    lista_cpfs_nomes = con.select('nome_usuario, cpf_usuario')
    lista_cpfs = [c for n, c in lista_cpfs_nomes]
    lista_nomes = [n for n, c in lista_cpfs_nomes]
    if nome_usuario in lista_nomes and cpf_usuario in lista_cpfs:
        return False
    return True

def encontrar_livro(titulo:str, autor:str) -> bool:
    ...
    