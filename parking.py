from constantes_paking import DIAS_SEMANA, PRECIO_DIA, PRECIO_SEMANA

def calcular_coste(dias):

    # 1.- Calcular las semanas
    semanas = dias // DIAS_SEMANA
    # 2.- Calcular los días restantes
    dias_restantes = dias % DIAS_SEMANA
    # 3.- Coste por semanas
    coste_semanal = semanas * PRECIO_SEMANA
    # 4.- Coste por días
    coste_dias = dias_restantes * PRECIO_DIA
    # 5.- Cálculo del total
    total = coste_dias + coste_semanal

    return total



print(calcular_coste(1))