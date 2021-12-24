def questions():
    
    result = 0
    
    q1 = input('1 - Mora perto da vítima? ').upper()
    q2 = input('2 - Já trabalhou com a vítima? ').upper()
    q3 = input('3 - Telefonou para a vítima? ').upper()
    q4 = input('4 - Esteve no local do crime?' ).upper()
    q5 = input('5 - Devia para a vítima? ').upper()

    if q1 == 'S': result += 1
    if q2 == 'S': result += 1
    if q3 == 'S': result += 1
    if q4 == 'S': result += 1
    if q5 == 'S': result += 1
    
    return result
    
def crime():
    name = input("Informe seu nome: ").title()
    
    print(f"\n{name} você irá responder algumas perguntas agora.")
    print('\nDigite S para sim ou N para não!')
    
    result = questions()
    
    if result == 5: print(f"\n{name} você é o(a) assassino(a). Pegamos você!")
    elif result < 5 and result > 2: print(f"\n{name} você é um(a) cúmplice!")
    elif result == 2: print(f"\n{name} você é um(a) de nossos(as) suspeitos(as)!")
    elif result <= 1: print(f"\n{name} você está liberado(a)!")
    
crime()