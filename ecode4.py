__AUTHOR__ = "dionealfarisi"
__VERSION__ = "1.0.1"
__LATEST_UPDATE__ = "03/10/2024"

def encrypt(text):
    """
    Mengubah teks menjadi format terenkripsi menggunakan simbol khusus.

    Args:
        text (str): Teks asli yang akan dienkripsi.

    Returns:
        str: Teks yang sudah dienkripsi.
    """
    if not text:
        return ''
    
    symbols = {
        'upper': '*',
        'lower': '=',
        'digit': '+',
        'symbol': '-'
    }

    encrypted = []
    for char in text:
        if char.isupper():  # Huruf besar
            encrypted.append(symbols['upper'] * (ord(char) - ord('A')) + ',')
        elif char.islower():  # Huruf kecil
            encrypted.append(symbols['lower'] * (ord(char) - ord('a')) + ',')
        elif char.isdigit():  # Angka
            encrypted.append(symbols['digit'] * (ord(char) - ord('0')) + ',')
        else:  # Simbol
            encrypted.append(symbols['symbol'] * (ord(char) - ord(' ')) + ',')
    
    return ''.join(encrypted).rstrip(',')  # Menghapus koma terakhir


def decrypt(encrypted_text):
    """
    Mengubah teks terenkripsi kembali ke bentuk aslinya.

    Args:
        encrypted_text (str): Teks yang sudah dienkripsi.

    Returns:
        str: Teks yang sudah didekripsi kembali.
    
    Raises:
        ValueError: Jika format terenkripsi tidak valid.
    """
    if not encrypted_text:
        return ''
    
    decrypted = []
    parts = encrypted_text.split(',')
    for part in parts:
        length = len(part)  # Hitung panjang simbol hanya sekali
        if part.startswith('*'):  # Huruf besar
            decrypted.append(chr(length + ord('A')))
        elif part.startswith('='):  # Huruf kecil
            decrypted.append(chr(length + ord('a')))
        elif part.startswith('+'):  # Angka
            decrypted.append(chr(length + ord('0')))
        elif part.startswith('-'):  # Simbol
            decrypted.append(chr(length + ord(' ')))
        else:
            raise ValueError(f"Invalid encrypted part: {part}")
    
    return ''.join(decrypted)

# Contoh penggunaan
if __name__ == "__main__":
    text_to_encrypt = "Hello123!"
    encrypted = encrypt(text_to_encrypt)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(encrypted)
    print(f"Decrypted: {decrypted}")