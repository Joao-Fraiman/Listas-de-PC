def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n1 = int(input('N1: '))
n2 = int(input('N2: '))
if n1 > n2 :
  n1, n2 = n2, n1

count = 0
for num in range(n1, n2 + 1):
    if is_prime(num):
        count += 1

print('A quantidade de números primos no intervalo é: {}'.format(count))
