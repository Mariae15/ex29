import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("Bem vindo ao menu Cadastro!")
    print("1 - Novo cadastro")
    print("2 - Ver cadastro")
    print("3 - Sair")
    print("---------------------------")

def salvar_cadastros(cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_pessoa(cadastros):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    turma = input("Digite sua turma:")
    curso = input("Digite seu curso:")
    
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

def ver_cadastro(cadastros):
    if not cadastros:
        print("\n Não há cadastros no sistema")
    else:
        print("\n ------LISTA DE CADASTROS------")
        
        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i} . Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastro (cadastros)
        
        elif opção == "3":
            print("Obrigado por utilizar o sistema!")
            break

        else:
            print("Opção incorreta! Tente novamente.")

if __name__== "__main__":
    main()
