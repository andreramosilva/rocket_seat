class Animal:
    def comer(self):
        print('I am an animal, I eat food.')
    
    def andar(self):
        print('I am an animal, I walk.')


class Felino(Animal):
    def lamber(self):
        print('I am a feline, I lick my fur.')

class Leao(Felino):
    def rugir(self):
        print('I am a lion, I roar.')

class Pessoa:
    def observa(self,animal:Animal):
        animal.comer()

animal = Animal()
felino = Felino()

animal.comer()
felino.comer()

renatin = Pessoa()
renatin.observa(felino)