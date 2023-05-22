"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    for i in range(2,number):
        if (number % i) == 0:
            return True
    return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    factor_list = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factor_list.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factor_list
