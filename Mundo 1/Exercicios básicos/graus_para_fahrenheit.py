#Crie um algoritmo que converta °C em °F
print('Digite uma temperatura em °C: ')
c = float(input())
f = (c * 1.8) + 32
print('A conversão de temperatura de {}°C para fahrenheit fica {:.1f}°F'.format(c,f))