def is_prime(num):
  if num < 2:
    return False
  for k in range(2, int(num**(1/2))+1):
    if num % k == 0:
      return False
  return True


n1=int(input('n1? '))
n2=int(input('n2? '))
tot=0
if n1>n2:
  n1,n2=n2, n1

lista = []

for i in range(n2):
    if not is_prime(i) and n1 < i < n2 and  i % 2 != 0:

        lista.append(i)

print(f'Lista dos números ímpares não primos [{n1}-{n2}]: {lista}')
