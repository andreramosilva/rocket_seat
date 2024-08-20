class Animal:
    def __init__(self,nome):
        self.nome = nome

    def emitir_som():
        pass
class Mamifero(Animal):
    def amamentar(self):
        return f"o animal {self.nome} está amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"O animal {self.nome} está voando"
    

class Morcego(Mamifero,Ave):
    def emitir_som(self):
        return "AAAAAAAAAAAAA"

    
morcego  = Morcego("Bat")

print(morcego.nome)
print(morcego.amamentar())
print(morcego.voar())