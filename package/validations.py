from abc import ABC, abstractmethod
class Validation(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def validation(self) -> str: ...

class ValidationName(Validation):

    def validation(self, user_name:str) -> str:
        names = user_name.split()

        for name in names:
            if not name.isalpha():
                raise ValueError('Nome invalido!') from ValidationName
            
        return user_name.lower()

class ValidationAge(Validation):
                                     
    def validation(self, user_age:str) -> str: #dd/mm/AAAA -> mm/dd/AAAA
        age = user_age.replace('/','')
        day, mounth = int(age[:2]), int(age[2:4])

        if age.isdigit() and day <= 31 and mounth <= 12 and day > 0 and mounth > 0:
            return f'{user_age[3:5]}-{user_age[0:2]}-{user_age[6:]}'
        
        else:
            raise ValueError('O valor Inserido não é uma data!') from ValidationAge

class ValidationCpf(Validation):

    def validation(self, user_cpf:str) -> str:
        cpf = user_cpf.replace('.','').replace('-','')

        if cpf.isdigit() and int(cpf[-2]) == digit_cpf(cpf,10) and int(cpf[-1]) == digit_cpf(cpf,11):
            return user_cpf
        
        else:
            raise ValueError ('O CPF inserido não é valido!') from ValidationCpf
        
#Essas duas classes precisariam de Muito mais, porem só ficará no nome
# Que eu acho que seriam autenticações, não validaçoes de entradas
        
class ValidationEmail(Validation):

    def validation(self, email_usuario:str ) -> str:
        if isinstance(email_usuario, str) and '@' in email_usuario:
            return email_usuario
        
        raise ValueError ('O Email inserido não é valido!') from ValidationEmail    

class ValidationNumero(Validation):

    def validation(self, numero_usuario:str) -> str:
        if isinstance(numero_usuario, str) and numero_usuario.isdecimal():
            return numero_usuario
        
        raise ValueError ('O Numero inserido não é valido!') from ValidationNumero
    
def mult_cpf(cpf:str, quant_digit:int) -> int:
    if quant_digit == 1:
        return 0
    
    return int(cpf[0])*quant_digit + mult_cpf(cpf[1:],quant_digit-1)

def digit_cpf(cpf:str, quant_digit:int) -> int:
    val_mult_cpf = mult_cpf(cpf, quant_digit)

    return ((val_mult_cpf*10)%11) if ((val_mult_cpf*10)%11) <= 9 else 0