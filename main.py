'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano
2-Cualquier otra entrada debe dar error
'''
class RomanNumberError( Exception ):
    pass

dic_entero_a_romano={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM', 
    1000:'M',2000:'MM',3000:'MMM'
}





dic_romano_a_entero={


 'I':1, 'V':5, 'X':10,'L':50, 'C':100, 'D':500, 'M':1000
}
'''
Reglas a cumplir con romano_a_entero
Los símbolos se suman y ordenan de mayor a menor
Si un símbolo de menor valor antecede a uno de mayor, el de menor valor se resta al de mayor
Solo se puede restar un símbolo de valor pequeño de cualquier símbolo de valor grande.
Los símbolos "I", "X", "C" y "M" se pueden repetir tres veces seguidas, pero no más. (Pueden aparecer más de tres veces si no aparecen secuencialmente, como en XXXIX.) "D", "L" y "V" no se pueden repetir.
Restas
"I" solo se puede restar de "V" y "X".
"X" se puede restar de "L" y "C" solamente. 
"C" se puede restar de "D" y "M" solamente. 
"V", "L" y "D" nunca se pueden restar.
Si se ha producido repetición de “I”, “X” o “C” ya no pueden restarse de sus digitos respectivos. Esto IIX es incorrecto, IX es correcto
Las restas correctas solo pueden realizarse una vez
'''


#Solo se puede restar un símbolo de valor pequeño de 
# cualquier símbolo de valor grande.
#'I':1 < 'V':5 <  'X':10 < 'L':50 < 'C':100 < 'D':500 <'M':1000

# Menor valor en lado izquierdo resta
# Menor valor en lado derecho suma 
#"I" solo se puede restar de "V" y "X".

def romano_a_entero(rom:str)->int: #M < D->C->C->X->I->I->I
    print("valor romano: ",rom)
    lista = list(rom)  # convertirmos en lista el romano recibido #['M','D','C','C','X','I','I','I']
    print("lista romano: ",lista)
    
    valor_entero=0

    for i in rom:
  
        #if i != len(lista)-1:
            """
            if dic_romano_a_entero.get(lista[i]) < dic_romano_a_entero.get(lista[i+1]):
                # si es I and V  or I and X
                #   restar si
                #  
                valor_entero += dic_romano_a_entero.get(lista[i+1]) - dic_romano_a_entero.get(lista[i])
            else:
                valor_entero +=dic_romano_a_entero.get(lista[i])    
            """
            valor_entero +=dic_romano_a_entero.get(i) 
    return valor_entero
    
print("Romano a entero: ",romano_a_entero("MDCCXIII"))#MMXIX


def entero_a_romano(num:int)->str:

    num = "{:0>4d}".format(num)
    lista = list(num) 
    longitud = len(lista)
    numero_romano=""

    for i in range(longitud):       
        longitud -=1
        lista[i] += "0"*longitud        
        numero_romano += dic_entero_a_romano.get( int(lista[i]),'')

    return numero_romano

#print("funcion en accion",entero_a_romano(336))
 
