def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    text_len = len(plaintext)
    keyword += keyword * ((text_len - 1) // len(keyword))
    for i in range(text_len):
        character = plaintext[i]
        key_chr = keyword[i]
        key_num = ord(key_chr)
        if key_num > 96:
            key = key_num - 97
        else:
            key = key_num - 65
        chr_num = ord(character)
        if chr_num > 96:
            ciphertext += chr((chr_num - 97 + key) % 26 + 97)
        else:
            ciphertext += chr((chr_num - 65 + key) % 26 + 65)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    text_len = len(ciphertext)
    keyword += keyword * ((text_len - 1) // len(keyword))
    for i in range(text_len):
        character = ciphertext[i]
        key_chr = keyword[i]
        key_num = ord(key_chr)
        if key_num > 96:
            key = key_num - 97
        else:
            key = key_num - 65
        chr_num = ord(character)
        if chr_num > 96:
            plaintext += chr((chr_num - 97 - key) % 26 + 97)
        else:
            plaintext += chr((chr_num - 65 - key) % 26 + 65)
    return plaintext