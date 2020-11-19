'''
-----------------------------
 EJERCICIO N°1
 Tuplas
-----------------------------
'''
# CREACIÓN DE TUPLAS
tuplaVacia = ()                   # vacía

tupla1 = (1, 2.5, "manzana", 8)
tupla2 = 1., "Python", .25, 125

tuplaUnElemento1 = (1,)           # 1 elemento
tuplaUnElemento2 = 1.,

print(tuplaVacia)

'''
-----------------------------
¿Cómo utilizar una tupla?
-----------------------------

# DEFINIR
miTupla = (1, 10, 100, 1000)

# LEER ELEMENTOS
print("Índices: ", miTupla[0])
print("Rodaja: ", miTupla[:-2])

for elem in miTupla:
  print(elem)

# CONCATENACIÓN Y REPLICACIÓN
#t1 = miTupla + (1000, 10000)
#t2 = miTupla * 3
#print(t1)

# LONGITUD
#print(len(t1))

# INTERCAMBIO DE VALORES
#t1, t2 = t2, t1
#print(t1)

# TRUE O FALSE
#print(10 in miTupla)

# INSTRUCCIONES ERRÓNEAS

# Método .append()
#miTupla.append(10000)

# Instrucción del
#del miTupla[0]

# Modificar su contenido
#miTupla[1] = -10
'''
