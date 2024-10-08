#def cubo(num):
 #   return num ** 3


cubo = lambda num: num ** 3

user_number = int(input(f'Digite um número: '))
print(f'O cubo de {user_number} é {cubo(user_number)}')