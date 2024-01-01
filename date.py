from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#Criar uma data
lancamento_app = datetime(2024, 5, 15)
print(f'O app vai ser lancado em {lancamento_app}')
# Receber a data de lancamento
data_lancamento = datetime.strptime(input('Quando será lancado o app?'),'%d/%m/%Y')
print(type(data_lancamento))

#Calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(f'O intervalo entre a data de lancamento e a data atual é {prazo.days} dias!')
