def ler_valores():
    N = int(input("N? "))
    print("Quais os valores?")
    valores = []
    for _ in range(N):
        numero = int(input())
        valores.append(numero)
    return valores


def par_mais_proximo(valores):
    par_minimo = None
    diferenca_minima = float('inf')
    
    for i in range(len(valores) - 1):
        for j in range(i + 1, len(valores)):
            diferenca = abs(valores[i] - valores[j])
            if diferenca < diferenca_minima:
                diferenca_minima = diferenca
                par_minimo = (valores[i], valores[j])
    
    return par_minimo


valores = ler_valores()
par = par_mais_proximo(valores)

print("Par mais próximo:", par[0], "e", par[1])
