n = int(input('Digite um número: '))

if n<0 or n>10:
  print('NÚMERO INVÁLIDO') 
else:
  for c in range(1, n+1):
    print('{}'.format(str(c)*c))
