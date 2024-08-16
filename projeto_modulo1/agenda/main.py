contatos = list()

def consultar(nome) -> dict:
    for contato in contatos:
      if contato.get(nome):
         return contato

def favoritador(nome)->None:
   for contato in contatos:
      if contato.get(nome) == nome:
        contato["favorito"] = True
        print(contato)

def editar(nome)->None:
    contato = consultar(nome)
    print("deseja editar o contato: ")
    print(contato)
    campos_para_editar = input("Qual/Quais campos deseja editar separe as opçoes por virgola como no exempo (nome,telefone, email)")
    # campos_para_editar = campos_para_editar.
    campos = campos_para_editar.split(",")
    for con in contatos:
       if con.get(nome) == nome:
          con = contato
          return 
    

def listar_favoritos()-> list:
   for contato in contatos: 
      if contato.get("favorito") == True:
         print(contato)

def salvar(contato):
   contatos.append(contato)
   print("contato adicionado com sucesso!")

def deletar(nome):
   #contato = consultar(nome)
    count = 0
    for contato in contatos:
        if contato.get("nome") == nome:
           contatos.remove(count)
        count+=1



opcao = ""
while opcao not in ["end","exit","stop","finish"]:
   contato = {"nome": "",
            "telefone":"",
            "email":"",
            "favorito": False}
   opcao = input("Escolha uma opçao (salvar(1), editar(2), deletar(3) e marcar um contato como favorito(4)) \n")

   if opcao == "salvar" or opcao == "1":
      contato["nome"] = input("Digite o nome do seu contato: ")
      contato["telefone"] = input("Digite o telefone do seu contato: ")
      contato["email"] = input("Digite o email do seu contato: ")
      contato["favorito"] = True if input("deseja adicionar contato aos seus favoritos? y/n: ") == "y" else False
      
      salvar(contato)
   elif opcao == "editar" or opcao == "2":
      nome = input("Digite o nome do contato que deseja editar: ")
      editar(nome)
   elif opcao == "deletar" or opcao == "3":
      nome = input("Digite o nome do contato que deseja deletar: ")
   elif opcao == "favorito" or opcao == "4":
      nome = input("Digite o nome do contato que deseja favoritar: ")
      favoritador(nome)
   
    
