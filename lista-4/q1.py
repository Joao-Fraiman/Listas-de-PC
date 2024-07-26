def cripto(termo):
  termo = termo.lower()
  resultado = ''
  
  for c in termo:
    if c >= 'a' and c <= 'e':
      resultado += '1'
    elif c >= 'f' and c <= 'j':
      resultado += '2'
    elif c >= 'k' and c <= 'o':
      resultado += '3'
    elif c >= 'p' and c <= 'z':
      resultado += '4'
    else:
      resultado += '5'
  
  return resultado


palavra = str(input('Digite o texto: '))
print('Encriptado: {}'.format(cripto(palavra)))
