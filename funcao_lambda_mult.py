#Função normal abaixo:

'''def multiplicar(user_number1, user_number2):
    return user_number1 * user_number2'''

#Função multiplicar com Lambda:

multiplicar = lambda num1, num2: user_number1 * user_number2

user_number1 = int(input('Digite o primeiro número: '))
user_number2 = int(input('Digite o segundo número: '))

print(f'A multiplicação de {user_number1} vezes {user_number2} é {multiplicar(user_number1, user_number2)}')

