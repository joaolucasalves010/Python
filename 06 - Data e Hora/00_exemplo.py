from datetime import datetime, date, time

dia = int(input("Digite o dia "))
mes = int(input("Digite o mês "))
ano = int(input("Digite o ano "))

d = date(ano, mes, dia)
print(d)
print(date.today())

print(datetime.now())

date_hour = datetime(2024, 9, 9)
print(date_hour)

hora = time(16, 19, 0)
print(hora)