"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    for i in range(2,number):
        if (number % i) == 0:
            return True
    return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    list = []
    # Começar com um divisor 2.
    # Enquanto o número não for 1:
        # Se o divisor não é primo, incrementar o divisor e continua.
        # Se o divisor é primo, e o número é divisível por ele:
            # Adicionar o divisor à lista.
            # Dividir o número pelo divisor.
        # Se o divisor é primo, e o número não é divisível por ele:
            # Incrementar o divisor.

