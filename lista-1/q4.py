a=input('Digite o texto A: ')
b=input('Digite o texto B: ')
print('Texto A dividido em duas partes: '+a[:len(a)//2]+' e '+ a[len(a)//2:])
print('Texto B dividido em duas partes: '+b[:len(b)//2]+' e '+b[len(b)//2:])
print(a[:len(a)//2] + ' + ' + b[len(b)//2:] + ' = ' + a[:len(a)//2] + b[len(b)//2:])
print(a[len(a)//2:] + ' + ' + b[:len(b)//2] + ' = ' + a[len(a)//2:] + b[:len(b)//2])

print(a[0] + ' + ' + b[1] + ' + ' + a[-1] + ' + ' + b[-1] + ' = ' + a[0] + b[1] + a[-1] + b[-1])
