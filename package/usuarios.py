from validations import ValidationNumero, ValidationAge, ValidationCpf, ValidationEmail, ValidationName
from abc import ABC, abstractmethod
from cadastro import cadastrar_usuario

class Usuario(ABC):
    def __init__(self, nome_usuario:str, nascimento_usuario:str, email_usuario:str, cpf_usuario:str, numero_usuario:int) -> None:
        self.id_usuario = int()
        self.nome_usuario = nome_usuario
        self.nascimento_usuario = nascimento_usuario
        self.email_usuario = email_usuario
        self.cpf_usuario = cpf_usuario
        self.numero_usuario = numero_usuario

#Property do usuario:
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def nome_usuario(self):
        return self._nome_usuario
    
    @property
    def nascimento_usuario(self):
        return self._nascimento_usuario
    
    @property
    def email_usuario(self):
        return self._email_usuario
    
    @property
    def cpf_usuario(self):
        return self._cpf_usuario
    
    @property
    def numero_usuario(self):
        return self._numero_usuario
    
#Setters
    
    @id_usuario.setter
    @abstractmethod
    def id_usuario(self, val:int): ...

    @nome_usuario.setter
    @abstractmethod
    def nome_usuario(self, val:str): ...

    @nascimento_usuario.setter
    @abstractmethod
    def nascimento_usuario(self, val:str): ...

    @email_usuario.setter
    @abstractmethod
    def email_usuario(self, val:str): ...

    @cpf_usuario.setter
    @abstractmethod
    def cpf_usuario(self, val:str): ...

    @numero_usuario.setter
    @abstractmethod
    def numero_usuario(self, val:int): ...

    @abstractmethod
    def cadastrar(self):...

    @abstractmethod
    def logar(self):...

class UsuarioAdmin(Usuario):
    def __init__(self, nome_usuario: str, nascimento_usuario: str, email_usuario: str, cpf_usuario: str, numero_usuario: int) -> None:
        super().__init__(nome_usuario, nascimento_usuario, email_usuario, cpf_usuario, numero_usuario)

#Setter do usuario:

    @Usuario.id_usuario.setter
    def id_usuario(self, val):
        if isinstance(val, int):    
            self._id_usuario = val
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de um int!')

    @Usuario.nome_usuario.setter
    def nome_usuario(self, val:str):
        self._nome_usuario = ValidationName().validation(val)
                
    @Usuario.nascimento_usuario.setter
    def nascimento_usuario(self, val:str):
        self._nascimento_usuario = ValidationAge().validation(val)

    @Usuario.email_usuario.setter
    def email_usuario(self, val:str):
        self._email_usuario = ValidationEmail().validation(val)
        
    @Usuario.cpf_usuario.setter
    def cpf_usuario(self, val:str):
        self._cpf_usuario = ValidationCpf().validation(val)
        
    @Usuario.numero_usuario.setter
    def numero_usuario(self, val):
        self._numero_usuario = ValidationNumero().validation(val)
        
    #nome_usuario:str, cpf_usuario:str, num_usuario:str, email_usuario:str, nascimento_usuario:str
    def cadastrar(self) -> None:
        cadastrar_usuario(self.nome_usuario, self.nascimento_usuario, self.email_usuario, self.cpf_usuario, self.nome_usuario)

    def logar(self):
        ...
class UsuarioConsumidor(Usuario):
    def __init__(self, nome_usuario: str, nascimento_usuario: str, email_usuario: str, cpf_usuario: str, numero_usuario: int) -> None:
        super().__init__(nome_usuario, nascimento_usuario, email_usuario, cpf_usuario, numero_usuario)

#Setter do usuario:

    @Usuario.id_usuario.setter
    def id_usuario(self, val):
        if isinstance(val, int):    
            self._id_usuario = val
        else:
            raise TypeError('Esta atributo não pode ser outra coisa alem de um int!')

    @Usuario.nome_usuario.setter
    def nome_usuario(self, val:str):
        self._nome_usuario = ValidationName().validation(val)
            
    @Usuario.nascimento_usuario.setter
    def nascimento_usuario(self, val:str):
        self._nascimento_usuario = ValidationAge().validation(val)

    @Usuario.email_usuario.setter
    def email_usuario(self, val:str):
        self._email_usuario = ValidationEmail().validation(val)
        
    @Usuario.cpf_usuario.setter
    def cpf_usuario(self, val:str):
        self._cpf_usuario = ValidationCpf().validation(val)
        
    @Usuario.numero_usuario.setter
    def numero_usuario(self, val:str):
        self._numero_usuario = ValidationNumero().validation(val)
        
    def cadastrar(self):
        cadastrar_usuario(self.nome_usuario, self.nascimento_usuario, self.email_usuario, self.cpf_usuario, self.nome_usuario)

    def logar(self):
        ...

        
if __name__ == '__main__':
    ...