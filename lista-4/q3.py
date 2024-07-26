def encontrar_divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

def verificar_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input("Qual o valor de N? "))
print("Digite os valores:")
nums = []
for c in range(N):
    num = int(input())
    nums.append(num)

print("A classificação é:")
for num in nums:
    l = encontrar_divisores(num)
    if verificar_primo(num):
        print("{} é primo".format(num))
    else:
        print("{} não é primo, os divisores são: {}".format(num, l))
