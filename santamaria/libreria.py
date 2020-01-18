# Pregunta nro1
def es_respuesta_validad(strRspta):
# verifique si la respuespuesta es valida. puede ser A,E,I,O o U
# Parametro strRspta
#retornar: bool
#1. si la longitud de strRspta es 1
    if( len(strRspta) == 1 ):
#1.1.si la strRspta no es A o E o I o O o U, devolver False, sino retornar  True
        if( strRspta!= "A" and strRspta!= "E" and strRspta!= "I" and strRspta!= "O" and strRspta!= "U"):
            return False
        else:
             return  True
#2. si no retornar False
    return False
#Fin_es_respuesta_valida

#ejerecicio nro2
import libreria
def es_letra_valida(strletra):
    """
    Verifica si strletraes una letra valida del Bingo.Pueden ser B, I , N ,G ,O
    :param strletra:
    :return: bool
    """
    #1
    if (len(strletra) == 1):

    #1.1
        if (strletra != "B" and strletra != "I" and strletra != "N" and strletra != "G" and strletra != "O"):
            return False

    #2
        else:
            return True
#fin_es_letra_valida



# Ejercicio 3

import libreria
def es_cancion_valida(strCancion):
    """
    Verifica si strletraes una letra valida de la cancion .Pueden ser C, A, N , C ,I,O,N
    :param strletra:
    :return: bool
    """
    #1
    if (len(strCancion) == 1):

    #1.1
        if (strCancion != "C" and strCancion != "A" and strCancion != "N" and strCancion != "C" and strCancion != "I" and
            strCancion != "O" and strCancion != "N" ):
            return False

    #2
        else:
            return True
#fin_es_cancion_valida


# Ejercicio nro 4
def es_Alto(intAlto):
    """
    Verifica si X persona es persona alta si esta  entre 160cm y 180cm es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intAlto == 160 or intAlto ==164 or intAlto == 168 or intAlto == 172 or
         intAlto == 174 or intAlto ==176 or intAlto == 180 ):
        return True
    else:
        return False

#fin_Persona_alta


# Ejercicio 5


def mayor_de_edad(intMayor):
    """
    Verifica si X persona es persona es mayor de edad si esta  entre 18 y 60 años es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intMayor == 18 or intMayor == 24 or intMayor == 26 or intMayor == 32 or
         intMayor ==  36 or intMayor == 40 or intMayor == 58 ):
        return True
    else:
        return False

#fin_Mayor_de_edad

# Ejercicio nro 6

import libreria
def gane_un_premio(strPremio):
    """
    Verifica si strletraes una letra valida del Premio.Pueden ser I, P , H ,O,N
    :param strletra:
    :return: bool
    """
    #1
    if (len(strPremio) == 1):

    #1.1
        if (strPremio != "I" and  strPremio != "P" and strPremio != "H" and strPremio != "O" and
                strPremio != "N"):
            return False

    #2
        else:
            return True
#fin_gane_un_premio


# Ejercicio nro 7
def es_Bueno_OK(intBueno):
    """
    Verifica si X persona es Bueno, si x persona saca notas  entre 12 y  20 es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intBueno == 12 or intBueno == 14 or intBueno == 16 or intBueno == 18 or
         intBueno == 20 ):
        return True
    else:
        return False

#fin_es_bueno_Ok
# Ejercicio 8
def es_impar_con_ltr(strImpar):
    # 1. strNum puede ser un numero impar de 1-19 o letras de B-G
    if ( strImpar == "1" or strImpar == "3" or strImpar == "5" or
         strImpar == "7" or strImpar == "9" or strImpar == "11" or
         strImpar == "13" or strImpar == "15" or strImpar == "17" or
         strImpar == "19" or strImpar == "B" or strImpar == "C" or
         strImpar == "D" or strImpar == "E" or strImpar == "F" or
         strImpar == "G"):
        return True
    else:
        # Si no es ningun numero 1-19 ni letras de a-z
        return False
#fin_es_impar_con_ltr

# Ejercicio nro 9
def descuento_valido(tipo, prestamo):
    # Si el tipo de cliente es PREFERENCIAL
    # Aqui se usa la funcion upper()
    if ( tipo.upper() == "PREFERENCIAL" ):
        return 0.10 * prestamo
    else:
        return 0
#fin_descuento

# Ejercicio nro01
import libreria

assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("A") == True)
assert ( libreria.es_respuesta_validad("E") == True)
assert ( libreria.es_respuesta_validad("J") == False)
assert ( libreria.es_respuesta_validad("I") == True)
assert ( libreria.es_respuesta_validad("G") == False)
assert ( libreria.es_respuesta_validad("O") == True)
assert ( libreria.es_respuesta_validad("X") == False)
assert ( libreria.es_respuesta_validad("U") == True)
assert ( libreria.es_respuesta_validad("M") == False)
print("es_respuesta_valida OK")

# Ejercicio nro02
import libreria

assert (libreria.es_letra_valida("A") == False)
assert (libreria.es_letra_valida("B") == True)
assert (libreria.es_letra_valida("I") == True)
assert (libreria.es_letra_valida("Z") == False)
assert (libreria.es_letra_valida("O") == True)
print("es_letra_valida OK")

# Ejercicio nro03
import libreria

assert (libreria.es_cancion_valida("X") == False)
assert (libreria.es_cancion_valida("C") == True)
assert (libreria.es_cancion_valida("A") == True)
assert (libreria.es_cancion_valida("Z") == False)
assert (libreria.es_cancion_valida("C") == True)
assert (libreria.es_cancion_valida("I") == True)
print("es_Cancion_valida OK")

# Ejercicio nro04
import libreria

assert (libreria.es_Alto(160) == True)
assert (libreria.es_Alto(150) == False)
assert (libreria.es_Alto(158) == False)
assert (libreria.es_Alto(159) == False)
assert (libreria.es_Alto(180) == True)
print("X_persona_es_Alta OK")

# Ejercicio nro05
import libreria

assert (libreria.mayor_de_edad(18) == True)
assert (libreria.mayor_de_edad(21) == False)
assert (libreria.mayor_de_edad(59) == False)
assert (libreria.mayor_de_edad(19) == False)
assert (libreria.mayor_de_edad(58) == True)
print("X_Mayor_de_edad OK")



# Ejercicio nro06


import libreria

assert (libreria.gane_un_premio("A") == False)
assert (libreria.gane_un_premio("I") == True)
assert (libreria.gane_un_premio("P") == True)
assert (libreria.gane_un_premio("Z") == False)
assert (libreria.gane_un_premio("H") == True)
assert (libreria.gane_un_premio("O") == True)
assert (libreria.gane_un_premio("L") == False)
assert (libreria.gane_un_premio("N") == True)
print("GANE UN PREMIO OK")

# Ejercicio nro07
import libreria

assert (libreria.es_Bueno_OK(12) == True)
assert (libreria.es_Bueno_OK(10) == False)
assert (libreria.es_Bueno_OK(8) == False)
assert (libreria.es_Bueno_OK(6) == False)
assert (libreria.es_Bueno_OK(18) == True)
print("X_persona_es_buena OK")

# Ejercicio nro08
import libreria

assert (libreria.es_impar_con_ltr("2") == False)
assert (libreria.es_impar_con_ltr("4") == False)
assert (libreria.es_impar_con_ltr("AA") == False)
assert (libreria.es_impar_con_ltr("1") == True)
assert (libreria.es_impar_con_ltr("F") == True)
assert (libreria.es_impar_con_ltr("l") == False)
print("es_Impar_con_ltr OK")

# Ejercicio nro09
import libreria

assert (libreria.descuento_valido("A", 300) == 0)
assert (libreria.descuento_valido("Preferencial", 100) == 10.0)
assert (libreria.descuento_valido("PREFERENCIAL", 100) == 10.0)
assert (libreria.descuento_valido("PrEfErEnCiAl", 100) == 10.0)
assert (libreria.descuento_valido("", 100) == 0)
print("descuento_valido OK")
