def exibir_menu():
    print("Bem vindo ao menu Cadastro!")
    print("1 - Novo cadastro")
    print("2 - Ver casdastro")
    print("3 - Sair")
    print("---------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    turma = input("Digite sua turma:")
    curso = input("Digite seu curso:")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})