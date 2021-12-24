def porcents(value):
    return (value - value * (15 / 100))

valor = input('Informe um valor monetário: ').replace(',','').replace('.','')

try:
    valor = float(valor)
except:
    print('Valor inserido inválido!')

print(porcents(valor))