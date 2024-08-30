#personagem

#heroi

#inimigo

import random

class Personagem:
    def __init__(self,nome, vida, lvl)->None:
        self._nome = nome
        self._vida = vida
        self._lvl = lvl
    def get_nome(self):
        return self._nome
    
    def get_vida(self):
        return self._vida
    
    def get_lvl(self):
        return self._lvl
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \n Vida: {self.get_vida()} \n Lvl: {self.get_lvl()}"

    def atacar(self, alvo):
        dano = random.randint(self.get_lvl * 2, self.get_lvl *4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome} e causou {dano} de dano!!")

    def receber_ataque(self,dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

class Heroi(Personagem):
    def __init__(self,nome,vida,lvl,habilidade):
        super().__init__(nome,vida,lvl)
        self._especial = habilidade

    def get_especial(self):
        return self._especial
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \n Habilidade: {self.get_especial()}"
    
    def ataque_especial(self,alvo):
        dano = random.randint(self.get_lvl() *5 , self.get_lvl * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome} usou especial {self.ataque_especial} em {alvo.get_nome()} e causou {dano} de dano. ")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, lvl,tipo) -> None:
        super().__init__(nome, vida, lvl)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \n Tipo: {self.get_tipo()}"
    




class Jogo:

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Jose",vida=100,lvl=1,habilidade="fedor de suvaco")
        self.inimigo = Inimigo(nome="bat",vida=80,lvl=5,tipo="petista")
        
    def iniciar_batalha(self):
        print("Começou o jogo!!!")
        while self.heroi.get_vida() >0 and self.inimigo.get_vida() >0:
            print("\nDetalhes personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            input("precione Enter para atacar!!")
            escolha = input("Ataque normal(1) ou especial?(2): ")
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("escolha invalida escolha novamente. ") 

            if self.inimigo.get_vida() >0:
                self.inimigo.atacar(self.heroi)
        if self.heroi.get_vida()>0:
            print("Parabens voce venceu a batalha")
        else: 
            print("Voce foi derrotado :/ ")

jogo = Jogo()
jogo.iniciar_batalha()