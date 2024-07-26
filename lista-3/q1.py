alunos = int(input("Quantos nomes? "))

lista = []
for c in range(alunos):
    nome = input("Nome do aluno: ")
    lista.append(nome)

print("Você digitou:")
for n in reversed(lista):
    print(n)
