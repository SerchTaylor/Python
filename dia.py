from datetime import date
import locale

# Configurar locale a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dias=date.today()
dia_ini_git = date(2026, 2,11)
dia_git = date(2026, 2,19)
dia_ini_go = date(2026, 2,20)
dia_go = date(2026, 2,27)
dia_ini_python = date(2026, 3, 6)
dia_python = date(2026, 5, 8)

year = date.today().year
cumple = date(year+1, 2, 23)

diacumple = cumple - date.today()

falta = dia_git - dias
falta2 = dia_go - dias
falta3 = dia_python - dias

git = dia_git-dia_ini_git
go = dia_go-dia_ini_go

#paginas de git y github
pag = 500
pag_actual = 430
pag_falta = pag-pag_actual


#paginas de go
pag_go = 411
pag_actual_go = 301
pag_falta_go = pag_go-pag_actual_go
tema_go = 0
tema_actual = 134
tema_total = 34
tema = tema_total - tema_actual

#paginas de python
pag_python = 411
pag_actual_python = 0
python = pag_python - pag_actual_python

tema_python = 11

print("\nHoy es", dias.strftime("%A %d-%m-%Y"),"\n")
if (falta.days >= 2 ):
    print("Del curso de Git / Github!!")
    print("Faltan",falta.days, "dias, para acabar el curso de Git / Github!!")
    print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
elif (falta.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Nos queda",falta.days, "dia, para acabar el curso de Git / Github!!")
     print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
elif (falta.days == 0 ):
    print("Hoy es",dias.strftime("%A %d-%m-%Y"),",y es el último dia del curso de Git / Githut!!")
    print("Nos faltan:",pag_falta,"para acabar el temario de Git / Github!!\n")
else:
    print("Has acabado el curso de Git / Githut!!")
    print("Fueron",git.days,"días, con sus",pag,"páginas\n")


if (falta2.days >= 2 ):
    print("Del curso de go!!")
    print("Faltan",falta2.days, "dias, para acabar el curso de GO!!")
    print("Nos faltan:",pag_go,"para acabar el temario de GO!!\n")
    print("Nos faltan",tema_go,"temas para acabar el temario de GO!!\n")
elif (falta2.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Nos queda",falta2.days, "dia, para acabar el curso de GO!!")
     print("Nos faltan:",pag_go,"para acabar el temario de GO!!\n")
     print("Nos faltan",tema_go,"temas para acabar el temario de GO!!\n")
elif (falta2.days == 0 ):
    print("Hoy es",dias.strftime("%A %d-%m-%Y"),",y es el último dia del curso de GO!!")
    print("Nos faltan:",pag_go,"para acabar el temario de GO!!\n")
    print("Nos faltan",tema_go,"temas para acabar el temario de GO!!\n")
else:
    print("Has acabado el curso de GO!!")
    print("Fueron",go.days,"días, con sus",pag_go,"páginas",tema_go,"temas\n")


if (falta3.days >= 2 ):
    print("Del curso de Python!!")
    print("Faltan",falta3.days, "dias, para acabar el curso de Python!!")
    print("Nos faltan:",python,"para acabar el temario de Python!!\n")
    print("Nos faltan",tema_python,"temas para acabar el temario de Python!!\n")
elif (falta3.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Nos queda",falta3.days, "dia, para acabar el curso de Python!!")
     print("Nos faltan:",python,"para acabar el temario de Python!!\n")
     print("Nos faltan",tema_python,"temas para acabar el temario de Python!!\n")
elif (falta3.days == 0 ):
    print("Hoy es",dias.strftime("%A %d-%m-%Y"),",y es el último dia del curso de Python!!")
    print("Nos faltan:",python,"para acabar el temario de Python!!\n")
    print("Nos faltan",tema_python,"temas para acabar el temario de Python!!\n")
else:
    print("Has acabado el curso de Python!!")
    print("Fueron",python.days,"días, con sus",pag_actual_python,"páginas\n")
    print("Fueron",python.days,"días, con sus",tema_python,"temas\n")

if(cumple == dias): print("Muchas Felicidades!!!!\n")
else:print("Aun no es tu cumple, faltan",diacumple.days,"dias.\n")


print("Proximos cursos: Linux1 17 Marzo y Robotica el 23 Marzo o el de nivel 3 de programacion Web el 23 marzo.\n\n")
