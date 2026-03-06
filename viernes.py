from datetime import date, timedelta
import locale

# Fecha inicial: hoy
hoy = date.today()

# Lista para guardar los viernes
viernes = []

# Buscar los próximos 8 viernes
dia = hoy

while len(viernes) < 8:
    if dia.weekday() == 4:  # 4 = viernes
        viernes.append(dia.strftime("%d-%m-%Y"))
    dia += timedelta(days=1)

# Mostrar los viernes encontrados
for v in viernes:
    print(v)

print ("\n",len(viernes),"\n")



