# Herança

class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome


    def andar(self):
        print(f"o animal {self.nome} andou.")
        return 

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"
    
class Gato(Animal):
    def emitir_som(self):
        return "miau"
    
dog = Cachorro(nome = "Rex")
cat = Gato(nome="Felix")
animais= [dog,cat]

for animal in animais:
    print(f"o animal{animal.nome} faz {animal.emitir_som()}")


class ContaBancaria:
    def __init__(self,saldo) -> None:
        self._saldo = saldo

    def depositar(self,valor):
        if valor >0:
            self._saldo += valor
    
    def sacar(self,valor):
        if valor>=self._saldo:
            self._saldo-=valor

    def consultar_saldo(self):
        return self._saldo
    
conta = ContaBancaria(saldo=10000)
print(f"{conta.consultar_saldo()}")
conta.depositar(10)
conta.sacar(999)
print(f"{conta.consultar_saldo()}")


from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass


class carro(Veiculo):
    def __init__(self) -> None:
        pass
    def ligar(self):
        return "ligou"
    def desligar(self):
        return "desligou"
    

carro_vermelho = carro()
print(carro_vermelho.ligar())