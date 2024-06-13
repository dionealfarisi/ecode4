#Dibuat Oleh Dione
#ini adalah versi alpha

def encrypt(text):
    encrypted = ''
    for char in text:
        if char.isupper():  # Huruf besar
            encrypted += '*' * (ord(char) - ord('A')) + ','
        elif char.islower():  # Huruf kecil
            encrypted += '=' * (ord(char) - ord('a')) + ','
        elif char.isdigit():  # Angka
            encrypted += '+' * (ord(char) - ord('0')) + ','
        else:  # Simbol
            encrypted += '-' * (ord(char) - ord(' ')) + ','
    return encrypted

def decrypt(encrypted_text):
    decrypted = ''
    parts = encrypted_text.split(',')
    for part in parts:
        if part.startswith('*'):  # Huruf besar
            decrypted += chr(int(part.count('*')) + ord('A'))
        elif part.startswith('='):  # Huruf kecil
            decrypted += chr(int(part.count('=')) + ord('a'))
        elif part.startswith('+'):  # Angka
            decrypted += chr(int(part.count('+')) + ord('0'))
        elif part.startswith('-'):  # Simbol
            decrypted += chr(int(part.count('-')) + ord(' '))
    return decrypted

print("What you need?")