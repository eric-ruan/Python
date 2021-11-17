#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
print('Digite o nome de sua cidade...')
city = str(input()).strip()

print(city[:5].upper() == 'SANTO')
