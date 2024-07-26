n1 = float(input('n1? '))
n2 = float(input('n2? '))
n3 = float(input('n3? '))

if n1 > n2 > n3:
  print(f'maior: {n1}')
  print(f'menor: {n2}')
  print(f'meio: {n3}')
elif n1 > n3 > n2:
  print(f'maior: {n1}')
  print(f'menor: {n3}')
  print(f'meio: {n2}')
elif n2 > n1 > n3:
  print(f'maior: {n2}')
  print(f'menor: {n1}')
  print(f'meio: {n3}')
elif n2 > n3 > n1:
  print(f'maior: {n2}')
  print(f'menor: {n3}')
  print(f'meio: {n1}')
elif n3 > n2 > n1:
  print(f'maior: {n3}')
  print(f'menor: {n2}')
  print(f'meio: {n1}')
elif n3 > n1 > n2:
  print(f'maior: {n3}')
  print(f'menor: {n1}')
  print(f'meio: {n2}')
elif n1 == n2 and n1 > n3:
  print(f'maiores: {n1}')
  print(f'menor: {n3}')
  print('não há elementos do meio')
elif n1 == n2 and n1 < n3:
  print(f'maior: {n3}')
  print(f'menores: {n1}')
  print('não há elementos do meio')
elif n1 == n3 and n1 < n2:
  print(f'maior: {n2}')
  print(f'menores: {n1}')
  print('não há elementos do meio')
elif n1 == n3 and n1 > n2:
  print(f'maiores: {n1}')
  print(f'menor: {n2}')
  print('não há elementos do meio')
elif n2 == n3 and n1 > n3:
  print(f'maior: {n1}')
  print(f'menores: {n2}')
  print('não há elementos do meio')
elif n2 == n3 and n1 < n3: 
  print(f'maior3s: {n2}')
  print(f'menor: {n1}')
  print('não há elementos do meio')
else:
  print(f'todos são iguais a {n1}')
