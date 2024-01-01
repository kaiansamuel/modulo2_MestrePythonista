from datetime import datetime
aniversario = datetime(2024, 9, 25)
dias_para_aniversario = aniversario - datetime.now()
print(f'Faltam {dias_para_aniversario.days} dias para o meu aniversario!')