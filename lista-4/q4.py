def imprimePartes(lista, separador):
    partes = []
    parte_atual = []
    
    for elemento in lista:
        if elemento != separador:
            parte_atual.append(elemento)
        else:
            if parte_atual:
                partes.append(parte_atual)
                parte_atual = []
    
    if parte_atual:
        partes.append(parte_atual)
    
    if not partes:
        print('Nenhuma')
    else:
        for parte in partes:
            print(' '.join(str(x) for x in parte))


N = int(input("N? "))
print("Qual a sequência?")
sequencia = []
for _ in range(N):  # Corrigido para ler exatamente N elementos
    numero = int(input())
    sequencia.append(numero)

separador = int(input("Qual o elemento separador? "))

print("Sequências resultantes:")
imprimePartes(sequencia, separador)
