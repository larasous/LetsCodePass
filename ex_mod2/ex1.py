def total_pares():
    par = 0
    lista = []
    
    tam = int(input('Informe o tamanho da lista: '))
    
    for i in range(0, tam):
        num = int(input('Informe o número da lista: '))
        lista.append(num)
        
        if not lista[i] % 2: par += 1
    
    print(f'\n{par} números da lista são pares\n')

total_pares()