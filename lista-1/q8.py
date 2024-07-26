texto= input('Texto? ')
i1= int(input('i1? '))
i2= int(input('i2? '))
if i1 > i2 :
  i1, i2 = i2, i1
if i1>=len(texto) or i2>=len(texto):
  print('Erro! índices precisam ser menores do que o tamanho do texto ('+ str(len(texto))+')')
else:
  print('Parte 1: '+ texto[:i1])
  print('Parte 2: '+ texto[:i2])
  print('Parte 3: '+ texto[i1:i2])
  print('Parte 4: '+ texto[i1:])
  print('Parte 5: '+ texto[i2:])
