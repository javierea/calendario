__author__ = "Javier E. Aguirre"
__version__ = "2021.06.21"

aniobisiesto = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
anionosiesto = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def cantidad_dias(dd, mm, aaaa):
    """ Devuelve la cantidad de días desde 01/01 del año dado hasta la fecha ingresada"""
    global cantidaddias
    cantidaddias = dd
    if mm == 1:
        pass
    else:
        if aaaa%4 != 0 or aaaa == 1900: #1900 es no bisiesto a pesar de ser divisible por 4
            for i in range(1, mm):
                cantidaddias = cantidaddias + anionosiesto.get(i)
        else:
            for i in range(1, mm):
                cantidaddias = cantidaddias + aniobisiesto.get(i)
    return cantidaddias

def dias_del_mes(mm, aaaa):
    """ Devuelve la cantidad de días que tiene un mes"""
    if aaaa%4 != 0 or aaaa == 1900: #1900 es no bisiesto a pesar de ser divisible por 4
        return anionosiesto.get(mm)
    else:
        return aniobisiesto.get(mm) 

def cantidad_anios(aaaa):
    """ Devuelve la cantidad de días desde 01/01/1900 hasta el 31/12 del año anterior al ingresado"""
    anios = [365, 365, 365, 366]
    aniosbis = []
    aniosbis = anios * (((aaaa - 1900)//4)+1)
    global cantidadanios
    if aaaa <= 1900:
        cantidadanios = 0
    else: cantidadanios = 365
    for i in range(aaaa-1901):
        cantidadanios += aniosbis[i]
    return cantidadanios

def dia_dela_semana(day, month, year):
    """ Devuelve el día de la semana de la fecha dada, 0 es domingo, 1 lunes... 6 sábado"""
    cantidad_dias(day, month, year)
    cantidad_anios(year)
    return (cantidaddias + cantidadanios) % 7 

def quierocalendario(month, year):
    calendario = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    separadores = ["  ", "  ", "  ", "  ", "  "]
    diasdelmes = dias_del_mes(month, year)
    ancla = dia_dela_semana(1, month, year)
    print(ancla)
    
    if ancla > 0:
        ancla = ancla - 1
    else:
        ancla = 6 
    for i in range(1, diasdelmes+ 1):
        calendario[ancla] = i
        ancla = ancla + 1
    
    if len(str(calendario[9])) == 2 and len(str(calendario[10])) == 2:
        separadores[0] = " "
    else: 
        pass
    if len(str(calendario[10])) == 2 and len(str(calendario[11])) == 2:
        separadores[1] = " "
    else: 
        pass
    if len(str(calendario[11])) == 2 and len(str(calendario[12])) == 2:
        separadores[2] = " "
    else: 
        pass
    if len(str(calendario[12])) == 2 and len(str(calendario[13])) == 2:
        separadores[3] = " "
    else: 
        pass
    if len(str(calendario[14])) == 2 and len(str(calendario[15])) == 2:
        separadores[4] = " "
    else: 
        pass

    print("  L    M    M    J    V    S    D\n==================================\n")
    print("  ", calendario[0], "  ", calendario[1], "  ", calendario[2], "  ", calendario[3], "  ", calendario[4], "  ", calendario[5], "  ", calendario[6])
    print("  ", calendario[7], "  ", calendario[8], "  ", calendario[9], separadores[0], calendario[10], separadores[1], calendario[11], separadores[2], calendario[12], separadores[3], calendario[13])
    print("  ", calendario[14], separadores[4], calendario[15], " ", calendario[16], " ", calendario[17], " ", calendario[18], " ", calendario[19], " ", calendario[20])
    print("  ", calendario[21], " ", calendario[22], " ", calendario[23], " ", calendario[24], " ", calendario[25], " ", calendario[26], " ", calendario[27])
    print("  ", calendario[28], " ", calendario[29], " ", calendario[30], " ", calendario[31], " ", calendario[32], " ", calendario[33], " ", calendario[34])
    print("  ", calendario[35], " ", calendario[36], " ", calendario[37], " ", calendario[38], " ", calendario[39], " ", calendario[40], " ", calendario[41])

if __name__ == "__main__":
    fecha = input("Ingrese mes y año del calendario que necesita con el siguiente formato (mm/aaaa): ")
    month, year = fecha.split("/")
    month, year = int(month), int(year)
    quierocalendario(month, year)