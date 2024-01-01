from datetime import datetime
import random

print('-----Olá, bem vindo à nossa empresa ------')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
data_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(
  input('Digite sua data de aniversário no formato dd/mm/aaa: '), '%d/%m/%Y'
)

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabéns, houve um sorteio e voce ganhou um cartão de compras no valor de {cartao}')