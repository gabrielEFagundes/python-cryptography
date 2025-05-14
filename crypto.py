from cryptography.fernet import Fernet

chave = Fernet.generate_key()
f = Fernet(chave)

frase = f.encrypt(b'Esta eh uma frase incrivel!')
print(frase)

f.decrypt(frase)
print(frase)