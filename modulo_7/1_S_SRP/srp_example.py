class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username=username,password=password): # 1
            self.__verify_input_in_database(username=username) # 2
            self.__insert_new_user(username=username, password=password) # 3
        else:
            raise Exception("Erro ao cadastrar usuario")
    
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
    def __verify_input_in_database(self, username: str) -> None:
        print("Acessando bd ...") # 2
        print("verificando existencia usuario ...")

    def __insert_new_user(self, username: str, password: str) -> None:
        print("Inserindo novo usuario ...")