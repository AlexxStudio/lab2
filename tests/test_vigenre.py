from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


def test_encrypt_vigenere():
    assert encrypt_vigenere("PYTHON", "A") == "PYTHON"
    assert encrypt_vigenere("python", "a") == "python"
    assert encrypt_vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"


def test_decrypt_vigenere():
    assert decrypt_vigenere("PYTHON", "A") == "PYTHON"
    assert decrypt_vigenere("python", "a") == "python"
    assert decrypt_vigenere("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"