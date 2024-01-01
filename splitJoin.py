frase = 'Olá bem vindo a esse treinamento'
print(frase.split())
print(frase.split(', '))
print(frase.split('-'))
nomes = 'jhonathan, rafael, carol, amanda, jeferson'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #drummer #js #react #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
# Como concatenar strings
hashtags_separadas_por_espaço = hashtags.split('  ')
print(hashtags_separadas_por_espaço)
print(','.join(hashtags_separadas_por_espaço))
print('.'.join(hashtags_separadas_por_espaço))
print(' '.join(hashtags_separadas_por_espaço))