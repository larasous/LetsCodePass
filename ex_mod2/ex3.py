def soma_lista(lista1: list, lista2: list):
    lista_soma = []
    
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            lista_soma.append(lista1[i]+lista2[i])
    
    return lista_soma

tam = int(input('Informe o tamanho das listas: '))

l1 = []
l2 = []
  
for i in range(0, tam):
    num = float(input('Informe um número da lista 1: '))
    num2 = float(input('Informe um número da lista 2: '))
    l1.append(num)
    l2.append(num2)

print(soma_lista(l1, l2))
    