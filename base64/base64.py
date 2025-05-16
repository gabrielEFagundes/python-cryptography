import base64

texto = 'Gabriel Ehrat Fagundes'

# ENCRYPT
encriptografar = base64.b64encode(texto.encode('utf-8'))
print('Encriptografado -> ' + encriptografar.decode('utf-8'))

# DECRYPT
decriptografar = base64.b64decode(encriptografar).decode('utf-8')
print('Descriptografado -> ' + decriptografar)

