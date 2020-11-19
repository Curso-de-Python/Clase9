'''
-----------------------------
 EJERCICIO N°2
 Diccionarios
-----------------------------
 OBTENCIÓN DE VALORES
-----------------------------
'''
numerosTelefono = {'jefe' : 5551234, 'Suzy' : 2265785, 'Lucas': 2665010}
nombres = ['Lucas', 'presidente', 'jefe']

for nombre in nombres:
  if nombre in numerosTelefono:
    print(nombre, "->", numerosTelefono[nombre])
  else:
    print(nombre, "no está en el diccionario")

'''
-----------------------------
 MÉTODOS DE DICCIONARIOS
-----------------------------
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

# keys() y sorted()
for key in dict.keys():
  print(key, "->", dict[key])

# item()
#for español, frances in dict.items():
#  print(español, "->", frances)

# values()
#for frances in dict.values():
#  print(frances)

-----------------------------
 OPERACIONES EN DICCIONARIOS
-----------------------------

# CAMBIANDO VALORES
dict['gato'] = 'minou'

# AGREGANDO CLAVES
#dict['cisne'] = 'cygne'
#dict.update({"pato":"canard"})

# ELIMINANDO CLAVES
#del dict ['perro']

# ELIMINANDO EL ÚLTIMO ELEMENTO
#dict.popitem()

print(dict)
'''
