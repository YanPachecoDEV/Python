print ('Seleção para o Exercito BR')

#media_idade = ('18')
#media_peso = ('60')
#media_altura = ('1.72')

idade = input ('Digite sua idade: ') 
peso = input ('Digite seu peso: ')
altura = input ('Digite sua altura: ')

#if (idade >= media_idade and peso >= media_peso and altura >= media_altura):
if (idade >= ('18') and peso >= ('60') and altura >= ('1.72')):
    print ('Parabéns! Você se encaixa nos padrões da seleção!')
else:
    print ('Desculpe, você não se encaixa nos padrões exigidos.')