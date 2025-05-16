import os
import base64

directory = os.getcwd()
finalDirectory = directory + r'\base64\Texto.txt'

# encrypts what is written on the text file
with open(finalDirectory, 'rb') as file:
    encoded = base64.b64encode(file.read())
    print(encoded)

# overwrites the encrypted text onto the text file
with open(finalDirectory, 'wb') as file:
    file.write(encoded)