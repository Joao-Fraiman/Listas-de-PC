numero1 = float(input('Digite o número A: '))
numero2 = float(input('Digite o número B: '))
add = float(numero1)+float(numero2)
sub = float(numero1)-float(numero2)
div = float(numero1)/float(numero2)
divint = int(numero1)//int(numero2)
rest = int(numero1)%int(numero2)
print(str(numero1) + ' + ' + str( numero2) + ' = ' + str(add))
print(str(numero1) + ' - ' + str( numero2) + ' = ' + str(sub))
print(str(numero1) + ' / ' + str( numero2) + ' = ' + str(div))
print(str(int(numero1)) + ' // ' + str(int(numero2)) + ' = ' + str(divint))
print(str(int(numero1)) + ' % ' + str(int(numero2)) + ' = ' + str(rest))
