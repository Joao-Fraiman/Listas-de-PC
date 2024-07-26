n = int(input("Digite um número: "))
ultimo=1
penultimo=1

print('Os {} primeiros termos da série de Fibonacci são: '.format(n))
if (n==1) or (n==2):
    print("1")
else:
    count=3
    print('1')
    print('1')
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)
