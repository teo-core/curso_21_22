nota = -1

"""
si <5 suspenso
entre 5 y 8 notable
mas de 8 sobresaliente


"""
if nota >=0 and nota <=10:
    if nota < 5:
        print("suspenso")
    elif nota < 7:
        print("aprobado")
    elif nota < 9:
        print("Notable")
    else:
        print("sobresaliente")
else:
    print("Valor incorrecto")