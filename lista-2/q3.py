def testes(n):
    import math
    raiz = math.floor(n ** (1 / 3))
    maior = raiz

    if maior * (maior + 1) * (maior + 2) == n:
        return "É triangular"
    else:
        return "Não é triangular"

numero = int(input("Digite um número inteiro positivo: "))
resultado = testes(numero)
print(resultado)
