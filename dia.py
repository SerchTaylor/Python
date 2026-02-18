from datetime import date
import locale

# Configurar locale a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dias=date.today()
dia_ini_git = date(2026, 2,11)
dia_git = date(2026, 2,19)
dia_ini_go = date(2026, 2,20)
dia_go = date(2026, 2,27)


falta = dia_git - dias
falta2 = dia_go - dia_git


#paginas de git y github
pag = 500
pag_actual = 413
pag_falta = pag-pag_actual


#paginas de go
pag_go = 500
pag_actual_go = 0
pag_falta_go = pag_go-pag_actual_go



print("\nHoy es", dias.strftime("%A %d-%m-%Y"),"\n")
if (falta.days >= 2 ):
    print("Del curso de Git / Github!!")
    print("Y faltan",falta.days, "dias, para acabar el curso de Git / Github!!")
    print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
elif (falta.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Queda",falta.days, "dia, para acabar el curso de Git / Github!!")
     print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
elif (falta.days == 0 ):
    print("Hoy",dias.strftime("%A %d-%m-%Y")," es el último dia del curso de Git / Githut!!")
    print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
else:
    print("Has acabado el curso de Git / Githut!!")
    print("Fueron",dia_git-dia_ini_git,"días. Y",pag,"páginas")


if (falta2.days >= 2 ):
    print("Del curso de go!!")
    print("Y faltan",falta2.days, "dias, para acabar el curso de GO!!")
    print("Nos faltan:",pag_falta_go,"para acabar el temario de GO!!\n")
elif (falta.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Queda",falta2.days, "dia, para acabar el curso de Git / Github!!")
     print("Nos faltan:",pag_falta_go,"para acabar el temario de Git / Github!!\n")
elif (falta2.days == 0 ):
    print("Hoy",dias.strftime("%A %d-%m-%Y")," es el último dia del curso de GO!!")
    print("Nos faltan:",pag_falta_go,"para acabar el temario de GO!!\n")
else:
    print("Has acabado el curso de GO!!")
    print("Fueron",dia_go-dia_ini_go,"días. Y",pag_actual,"páginas")

print("Proximo curso: Robotica, linux y python\n\n")