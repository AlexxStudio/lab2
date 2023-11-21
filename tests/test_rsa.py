from src.lab2.rsa import is_prime, gcd, multiplicative_inverse


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(11) == True
    assert is_prime(8) == False


def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(3, 7) == 1


def test_multiplicative_inverse():
    assert multiplicative_inverse(7, 40) == 23


