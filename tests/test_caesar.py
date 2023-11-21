from src.lab2.caesar import encrypt_caesar, decrypt_caesar


def test_encrypt_caesar():
    assert encrypt_caesar("python", 0) == "python"
    assert encrypt_caesar("", 0) == ""
    assert encrypt_caesar("PYTHON", 0) == "PYTHON"
    assert encrypt_caesar("", 3) == ""
    assert encrypt_caesar("PYTHON", 3) == "SBWKRQ"
    assert encrypt_caesar("python", 3) == "sbwkrq"
    assert encrypt_caesar("Python", 3) == "Sbwkrq"


def test_decrypt_caesar():
    assert decrypt_caesar("python", 0) == "python"
    assert decrypt_caesar("", 0) == ""
    assert decrypt_caesar("PYTHON", 0) == "PYTHON"
    assert decrypt_caesar("", 3) == ""
    assert decrypt_caesar("SBWKRQ", 3) == "PYTHON"
    assert decrypt_caesar("sbwkrq", 3) == "python"
    assert decrypt_caesar("Sbwkrq", 3) == "Python"