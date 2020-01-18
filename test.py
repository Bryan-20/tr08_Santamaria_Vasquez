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

