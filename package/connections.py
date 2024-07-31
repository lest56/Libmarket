import mysql.connector as connector
from abc import ABC

class Connection(ABC):
    def __init__(self) -> None:
        self.conn = connector.connect(host='localhost', user='root', password='1234', database='DB_livraria')
        self.cur = self.conn.cursor()
        self._DB_name = 'DB_livraria'
        self._table = None
        

class ConnectionLivro(Connection):
    def __init__(self) -> None:
        super().__init__()
        self._table = 'tb_livros'

    def insert(self, nome_livro:str, livro_genero:str, data_pub:str, preco_livro:int) -> None:
        self.cur.execute(f"INSERT INTO tb_livros (nome_livro, livro_gen, data_pub, preco_livro) VALUES (%s, %s, %s, %s)", (nome_livro, livro_genero, data_pub, preco_livro))
        self.conn.commit()

    def update(self):
        ...

    def delete(self):
        ...

    def select(self):
        ...

class ConnectionUsers(Connection):
    def __init__(self) -> None:
        super().__init__()
        self._TABLE = 'tb_usuarios'

    def insert(self, nome_usuario:str, cpf_usuario:str, num_usuario:str, email_usuario:str, nascimento_usuario:str) -> None:
        self.cur.execute("INSERT INTO tb_usuarios (nome_usuario, nascimento_usuario, email_usuario,cpf_usuario, num_usuario) VALUES (%s, %s, %s, %s, %s)", (nome_usuario, nascimento_usuario, email_usuario, cpf_usuario, num_usuario))
        self.conn.commit()

    def update(self):
        ...

    def delete(self):
        ...

    def select(self, string:str):
        self.cur.execute(f"SELECT {string} from {self._TABLE}")
        resultado = self.cur.fetchall()
        return resultado

    @property
    def table_name(self):
        return self._TABLE

    

if __name__ == '__main__':
    dbl = ConnectionLivro()
    dbu = ConnectionUsers()
    data = dbu.select('nome_usuario, cpf_usuario')
    print(data)
    

    # dbl.insert('Manifesto Comunista', 'Politico', '1848-02-21', 20.99)