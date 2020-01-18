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

