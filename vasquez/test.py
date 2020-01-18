import libreria

assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("F") == True)
assert ( libreria.es_respuesta_validad("H") == True)
assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("I") == True)
print("es_respuesta_valida OK")

assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("K") == True)
assert ( libreria.es_respuesta_validad("L") == True)
assert ( libreria.es_respuesta_validad("A") == False)
assert ( libreria.es_respuesta_validad("M") == True)
print("es_respuesta_valida OK")

assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("P") == True)
assert ( libreria.es_respuesta_validad("Q") == True)
assert ( libreria.es_respuesta_validad("A") == False)
assert ( libreria.es_respuesta_validad("R") == True)
print("es_respuesta_valida OK")

assert ( libreria.es_respuesta_validad("A") == False)
assert ( libreria.es_respuesta_validad("U") == True)
assert ( libreria.es_respuesta_validad("V") == True)
assert ( libreria.es_respuesta_validad("B") == False)
assert ( libreria.es_respuesta_validad("X") == True)
print("es_respuesta_valida OK")


assert ( libreria.es_respuesta_validad("LL") == False)
assert ( libreria.es_respuesta_validad("AB") == True)
assert ( libreria.es_respuesta_validad("CD") == True)
assert ( libreria.es_respuesta_validad("PP") == False)
assert ( libreria.es_respuesta_validad("EF") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LL") == False)
assert ( libreria.es_respuesta_validad("KL") == True)
assert ( libreria.es_respuesta_validad("MN") == True)
assert ( libreria.es_respuesta_validad("OG") == False)
assert ( libreria.es_respuesta_validad("ST") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LL") == False)
assert ( libreria.es_respuesta_validad("UV") == True)
assert ( libreria.es_respuesta_validad("XY") == True)
assert ( libreria.es_respuesta_validad("OG") == False)
assert ( libreria.es_respuesta_validad("AG") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLE") == False)
assert ( libreria.es_respuesta_validad("ABC") == True)
assert ( libreria.es_respuesta_validad("DEF") == True)
assert ( libreria.es_respuesta_validad("ODE") == False)
assert ( libreria.es_respuesta_validad("JKL") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLE") == False)
assert ( libreria.es_respuesta_validad("MNO") == True)
assert ( libreria.es_respuesta_validad("PQR") == True)
assert ( libreria.es_respuesta_validad("ODE") == False)
assert ( libreria.es_respuesta_validad("STU") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLEV") == False)
assert ( libreria.es_respuesta_validad("ABCD") == True)
assert ( libreria.es_respuesta_validad("EFGH") == True)
assert ( libreria.es_respuesta_validad("IPOK") == False)
assert ( libreria.es_respuesta_validad("IJKL") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLEV") == False)
assert ( libreria.es_respuesta_validad("QRST") == True)
assert ( libreria.es_respuesta_validad("KLOP") == True)
assert ( libreria.es_respuesta_validad("IPOK") == False)
assert ( libreria.es_respuesta_validad("YZAB") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLEV") == False)
assert ( libreria.es_respuesta_validad("ABLM") == True)
assert ( libreria.es_respuesta_validad("GFBH") == True)
assert ( libreria.es_respuesta_validad("IPOK") == False)
assert ( libreria.es_respuesta_validad("PWQO") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLEVP") == False)
assert ( libreria.es_respuesta_validad("ABCDE") == True)
assert ( libreria.es_respuesta_validad("FGHIJ") == True)
assert ( libreria.es_respuesta_validad("IPOKB") == False)
assert ( libreria.es_respuesta_validad("PQRST") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LLEVP") == False)
assert ( libreria.es_respuesta_validad("UVXYZ") == True)
assert ( libreria.es_respuesta_validad("ARGLO") == True)
assert ( libreria.es_respuesta_validad("FDSRW") == False)
assert ( libreria.es_respuesta_validad("SGBLM") == True)
print("es_respuesta_valida OK")



assert ( libreria.es_respuesta_validad("LL") == False)
assert ( libreria.es_respuesta_validad("HL") == True)
assert ( libreria.es_respuesta_validad("FJ") == True)
assert ( libreria.es_respuesta_validad("FD") == False)
assert ( libreria.es_respuesta_validad("PT") == True)
print("es_respuesta_valida OK")
