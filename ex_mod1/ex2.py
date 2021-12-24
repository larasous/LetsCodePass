SEXO = ['M', 'F', 'Outro']

def validate_age(age):
    return (age > 0 and age < 150)


def validate_salary(salary):
    return (salary > 0)


def validate_sex(sex):
    return sex in SEXO


def read():

    while True:
        age = input("\nInforme uma idade no intervalo [0, 150]: ")
        try:
            age = int(age)
        except:
            print('Erro ao converter, insira um valor válido!')
        
        if validate_age(age):
            break
        else:
            print('\nIdade inserida inválida!')
        
    while True:  
        salary = input("\nInforme o salário: ")
        
        try:
            salary = float(salary)
        except:
            print('Erro ao converter, insira um valor válido!')
        
        if validate_salary(salary):
            break
        else:
            print('\nSalário inserido inválido!')
    
    while True:
        sex = input("\nInforme o sexo - [M, F, Outro]: ").upper()
        
        if validate_sex(sex):
            break
        else:
            print('\nSexo inserido inválido!')
    
    print('\nInformações válidas!')


read()