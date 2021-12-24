def tabuada(num: int):
    print('='*20)
    for i in range(1,10):
        print(f"    {num} * {i} = {num*i}")
    print('='*20)
    
    
while True:     
    try:
        numero = input('Deseja a tabuada de qual número: ')
        numero = int(numero)
        break
    except ValueError:
        print('Insira um valor inteiro!\n')

tabuada(numero)
    