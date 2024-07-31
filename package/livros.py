class Livro:
    def __init__(self, titulo:str, autor:str, genero:str, valor:float) -> None:
        self.titulo_livro = titulo
        self.autor_livro = autor
        self.genero_livro = genero
        self.valor_livro = valor

    @property
    def titulo_livro(self):
        return self._titulo_livro
    
    @property
    def autor_livro(self):
        return self._autor_livro
    
    @property
    def genero_livro(self):
        return self._genero_livro
    
    @property
    def valor_livro(self):
        return self._valor_livro

#Setters dos attrs

    @titulo_livro.setter
    def titulo_livro(self, val):
        if isinstance(val, str):
            self._titulo_livro = val.lower()
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de uma string!')
    
    @autor_livro.setter
    def autor_livro(self, val):
        if isinstance(val, str):
            self._titulo_livro = val.lower()
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de uma string!')
    
    @genero_livro.setter
    def genero_livro(self, val):
        if isinstance(val, str):
            self._titulo_livro = val.lower()
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de uma string!')

    @valor_livro.setter
    def valor_livro(self, val):
        if isinstance(val, (int, float)):
            self._valor_livro = val
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de um int ou float!')

if __name__ == '__main__':
    lv = Livro('Memórias')
    print(lv.titulo_livro)