
altura = float(input('Qual é a sua altura em cm?'))
peso = float(input('Qual é seu peso em KG?'))

resultado = peso / (altura/100)**2

if resultado < 18.5:
    print('Magreza')
    
elif resultado >= 18.5 and resultado < 24.9:
    print('Normal')
        
elif resultado >= 25 and resultado < 29.9:
    print('Sobrepeso')
        
elif resultado >= 30 and resultado < 39.9:
    print('Obesidade')
    
else:
    print('Obesidade grave!')
    
        

        
    


