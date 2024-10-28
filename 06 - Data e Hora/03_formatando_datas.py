import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

# Converter string para date time
data_string = "12/09/2024 13:23"
d = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(d) # Output >> 12/09/2024 13:23