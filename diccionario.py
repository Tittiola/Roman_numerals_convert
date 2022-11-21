
d1={
    "nombre":"Carlos",
    "edad":"45",
    "dni":"Y32987B",
    10:"X"
}
print(d1)
d2=dict([
    ('nombre','Dulce'),
    ('edad',25),
    ('dni','T8787R')
])
print(d2)


#funcion get
print("funcion get ",d1.get(100,"No se encuentra!!!"))
print(type(d1.get(10)))

#funcion clear elimina todo el diccionario
d2.clear()
print("funcion clear ",d2)

#funcion items devuelve una lista con los keys y values del diccionario

valores = d1.items()
print("funcion items ",valores)

for key,val in valores:
    print(str(key) +"-"+str(val))

#funcion keys devuelve una lista con todas las keys del diccionario 

llaves = d1.keys()
print("funcion key ",llaves)

#funcion values devuelve una lista con todos los valores del diccionario

valores = d1.values()
print("funcion values ",valores)


#funcion para agregar pop(key)
d1.pop(10)
print("funcion pop(10) ",d1)

#funcion update para añadir mas valores a un diccionario

#d3={'a':100,'b':50,'c':60}
d1.update({'a':100,'b':50,'c':60})
print("funcion update ",d1)

#popitem() elimina de manera aleatoria un elemento del diccionario

d1.popitem()
print("funcion popitem ",d1)0pl .