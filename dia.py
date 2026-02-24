from datetime import date
import locale

# Configurar locale a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dias=date.today()
dia_ini_git = date(2026, 2,11)
dia_git = date(2026, 2,19)
dia_ini_go = date(2026, 2,20)
dia_go = date(2026, 2,27)


year = date.today().year
cumple = date(year, 2, 23)
cumple2 = date(year+1, 2, 23)

diacumple = cumple2-cumple

falta = dia_git - dias
falta2 = dia_go - dias

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
tema_actual = 12
tema_total = 34
tema = tema_total - tema_actual

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
    print("Nos faltan:",pag_falta_go,"para acabar el temario de GO!!\n")
    print("Nos faltan",tema,"temas para acabar el temario de GO!!\n")
elif (falta.days == 1 ):
     print("Del curso de Git / Github!!")
     print("Nos queda",falta2.days, "dia, para acabar el curso de GO!!")
     print("Nos faltan:",pag_falta_go,"para acabar el temario de GO!!\n")
     print("Nos faltan",tema,"temas para acabar el temario de GO!!\n")
elif (falta2.days == 0 ):
    print("Hoy es",dias.strftime("%A %d-%m-%Y"),",y es el último dia del curso de GO!!")
    print("Nos faltan:",pag_falta_go,"para acabar el temario de GO!!\n")
    print("Nos faltan",tema,"temas para acabar el temario de GO!!\n")
else:
    print("Has acabado el curso de GO!!")
    print("Fueron",go.days,"días, con sus",pag_actual,"páginas\n")
    print("Fueron",go.days,"días, con sus",tema,"temas\n")


if(cumple == dias): print("Muchas Felicidades!!!!\n")
else:print("Aun no es tu cumple, faltan",diacumple.days,"dias.\n")


print("Proximos cursos: Linux1 17 Marzo, Robotica el 23 Marzo y Python el 6 de Marzo durante 6 viernes.\n\n")