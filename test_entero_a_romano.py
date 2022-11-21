from main import entero_a_romano,romano_a_entero
'''
Casos de prueba
a) 1994 -> MCMXCIV
b) 4000->RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberErro("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
def test_entero_a_romano():
    assert entero_a_romano(336) == ['0000','300','30','6']
'''

def test_336():
    assert entero_a_romano(336) == "CCCXXXVI"

def test_2022():
    assert entero_a_romano(2022) == "MMXXII"


def test_1():
    assert romano_a_entero("I") == 1

def test_1713():
    assert romano_a_entero("MDCCXIII") == 1713  