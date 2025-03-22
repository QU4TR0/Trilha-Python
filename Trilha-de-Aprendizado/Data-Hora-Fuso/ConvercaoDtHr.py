import datetime as dt

d = dt.datetime.now()

print(d.strftime("%d/%m/%Y - %H:%M - %a")) # Converte pra data no modo passado dd/mm/YY HH:MM

date_string = "07/03/2025 21:00"
d = dt.datetime.strptime(date_string, "%d/%m/%Y %H:%M") # Converte o valor de string para data e hora
print(d)