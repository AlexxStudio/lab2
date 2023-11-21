def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for character in plaintext:
        chr_num = ord(character)
        if chr_num > 96:
            ciphertext += chr((chr_num - 97 + shift) % 26 + 97)
        else:
            ciphertext += chr((chr_num - 65 + shift) % 26 + 65)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for character in ciphertext:
        chr_num = ord(character)
        if chr_num > 96:
            plaintext += chr((chr_num - 97 - shift) % 26 + 97)
        else:
            plaintext += chr((chr_num - 65 - shift) % 26 + 65)
    return plaintext

