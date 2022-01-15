ano = {
    'Janeiro': 31,
    'Fevereiro': 28,
    'Março': 31,
    'Abril': 30,
    'Maio': 31,
    'Junho': 30,
    'Julho': 31,
    'Agosto': 31,
    'Setembro': 30,
    'Outubro': 31,
    'Novembro': 30,
    'Dezembro': 31
}

def imprime(d1: dict):
    for k, v in d1.items():
        print(f'{k} - {v}')

imprime(ano)