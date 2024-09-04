lista_livro = []
id_global = 0




# Função para cadastrar um livro na lista
def cadastrar_livro(id):
    global id_global
    id_global += 1
    nome = input("Por favor escolha o nome do livro: ")
    autor = input("Por favor escolha o nome do autor do livro: ")
    editora = input("Por favor escolha o nome da editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)




# Função para consultar livros
def consultar_livro():
    while True:
        print("Consultar Livro(s):")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            for livro in lista_livro:
                print(f"Livro: [ Nome: {livro['nome']} "
                      f"| ID: {livro['id']} "
                      f"| Autor: {livro['autor']} "
                      f"| Editora: {livro['editora']} ]\n")
        elif opcao == 2:
            id_consulta = int(input("Digite o ID do livro desejado: "))
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
                    break
            else:
                print("Livro não encontrado.")
                break
        elif opcao == 3:
            autor_consulta = input("Digite o nome do autor desejado: ")
            for livro in lista_livro:
                if livro['autor'] == autor_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente")
            continue




# Função para remover um livro da lista
def remover_livro():
    while True:
        id_livro_para_remover = int(input("Digite o ID do livro que quer remover ou digite 0 para retorna ao menu principal: "))
        if id_livro_para_remover == 0:
            break
        for livro in lista_livro:
            if livro['id'] == id_livro_para_remover:
                lista_livro.remove(livro)
                print("Livro '{}' removido com sucesso.".format(livro['nome']))
                break
        else:
            print("ID inválido. Tente novamente")
            continue




# Mensagem de boas-vindas e loop principal do programa
print("Bem vindo à livraria do Gabriel")
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar ")
    escolha_menu_principal = int(input("Escolha uma das opçãos: "))

    if escolha_menu_principal == 1:
        print("")
        cadastrar_livro(id_global + 1)
    elif escolha_menu_principal == 2:
        print("")
        consultar_livro()
    elif escolha_menu_principal == 3:
        print("")
        remover_livro()
    elif escolha_menu_principal == 4:
        print("Encerrando.")
        break
    else:
        print("Opção inválida.")
        continue
