'''Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento 
em portugues. O usuario deverá fornecer a temperatura.

Temperatura - cozimento

120ºF ou 48ºC - RARE (Selada)
130ºF ou 54ºC - Medium Rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passado)

'''
temp_cel = int(input('Qual a temperatura da carne? '))

if temp_cel < 48:
    print('Cozinhar por mais alguns minutos!')
elif temp_cel in range(48, 53):
    print('Selada')
elif temp_cel in range(54, 59):
    print('Ao ponto para o mal')
elif temp_cel in range(60, 64):
    print('Ao ponto')
elif temp_cel in range(65, 70):
    print('Ao ponto para o bem')
elif temp_cel >=71:
    print('Bem passadada')
           







