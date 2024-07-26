t1=input('Texto 1?').lower()
t2=input('Texto 2?').lower()
t3=input('Texto 3?').lower()

print('Seguem os textos em ordem: ')

if t1>t3 and t2>t3:
  print('1o. '+ t3)
  if t2>t1:
    print('2o. '+ t1)
    print('3o. '+ t2)
  else:
    print('2o. '+ t2)
    print('3o. '+ t1)
if t1>t2 and t3>t2:
  print('1o. '+ t2)
  if t3>t1:
    print('2o. '+ t1)
    print('3o. '+ t3)
  else:
    print('2o. '+ t3)
    print('3o. '+ t1)
if t3>t1 and t2>t1:
  print('1o. '+ t1)
  if t2>t3:
    print('2o. '+ t3)
    print('3o. '+ t2)
  else:
    print('2o. '+ t2)
    print('3o. '+ t3)
    
