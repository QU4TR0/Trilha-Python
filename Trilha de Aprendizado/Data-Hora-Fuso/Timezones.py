import datetime as dt
import pytz

d = dt.datetime.now(pytz.timezone('America/Sao_Paulo'))
d = dt.datetime.now(pytz.timezone('Europe/Madrid'))
d = dt.datetime.now(pytz.utc)

print(d)