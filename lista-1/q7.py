n_dias= int(input('Digite um número: '))

if n_dias==0:
  print('0 dias equivale à nenhum dia.')
  
if n_dias>=1 and n_dias<=6:
  print(str(n_dias)+' dias equivalem à nenhuma semana!')
  
if n_dias==7:
  print(str(n_dias)+' dias equivalem à 1 semana!')
  
if (n_dias%7==0) and n_dias>7:
  print(str(n_dias)+' dias equivalem à '+ str(n_dias//7)+' semanas!')
  
if n_dias==8:
  print('8 dias equivalem à 1 semana e 1 dia!')
  
if (n_dias>8) and (n_dias%7==1):
  print(str(n_dias)+' dias equivalem à '+ str(n_dias//7)+' semanas e 1 dia!')
  
if (n_dias>7) and (n_dias%7!=1) and (n_dias%7!=0):
  print(str(n_dias)+' dias equivalem à '+ str(n_dias//7)+' semanas e '+ str(n_dias%7)+' dias!')
