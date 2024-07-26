n1 = int(input('N1 = '))
n2 = int(input('N2 = '))
if n1 > n2 :
  n1, n2 = n2, n1


if (n1<1 or n1>10) or (n2<1 or n2>10):
  print('NÚMEROS INVÁLIDOS')
else:
  for k in range(n1, n2 + 1):
    print('=-=-=-= Tabuada do {} =-=-=-='.format(k))
    for c in range(1,11):
       print('{} x {:2} = {}'.format(n1, c, c*n1))
    n1 += 1
