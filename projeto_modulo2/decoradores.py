class MeuDecorator:
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self) -> any:
        print("Antes da funcao")
        self.func()
        print("Depois da funcao ser chamada")

@MeuDecorator
def minha_func():
    for i in range(10):
        print(i)

minha_func()