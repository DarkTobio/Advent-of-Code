#ADVENT OF CODE [2 - 1]

# ESTRUCTURACIÓN DE LA DATA

import re

pw = ['3-5 f: fgffh',
'6-20 n: qlzsnnnndwnlhwnxhvjn',
'6-7 j: jjjjjwrj',
'8-10 g: gggggggggg',
'7-9 v: vhqvlvwvzqwqvrxvjnf',
'1-5 r: rvmjr']

split = [] #separa string en substrings por valores
min = [] #min clave
max = [] #max clave
letras = [] #letra evaluada
claves = [] #clave del string

for i in range(0,len(pw)):
  split.append(re.findall(r"[\w']+", pw[i])) #separa pw según carácteres de palabras

  min.append(int(split[i][0])) #guarda mínimos del pw
  max.append(int(split[i][1])) #guarda máximos del pw
  letras.append(split[i][2]) #guarda letra evaluada del pw
  claves.append(split[i][3]) #guarda los pw

################
# PROBLEMA (2-1)

contador = [] #cuenta q repeticiones de la letra
validador = [] #compara q repeticiones con el max

for elements in range(0,len(letras)):
  #print(claves[elements].count(letras[elements]))
  contador.append(claves[elements].count(letras[elements]))
  #print(claves.count(elements))
  #print(contador)

a = 0

for elements in range(0,len(contador)):
  if contador[elements] > max[elements] or contador[elements] < min[elements]:
    validador.append(0)
  else:
    validador.append(1)
    a+=1

respuesta = sum(validador)

# print("repeticiones de letra    ",contador)
# print("min aparicion de la letra", min)
# print("max aparicion de la letra", max)
# print("cumpla o no (1/0)        ",validador)



# print("total de claves que cumplen:",respuesta)
# print("total de claves que cumplen:",a)

################
# PROBLEMA (2-2)

out_of_range = 0
pw_invalida = 0
pw_valida = 0

for cont in range(0,len(claves)):
  if (max[cont] > len(claves[cont])): #cuenta si el verificador de posición max es mayor que el largo de la clave (error)
    out_of_range += 1
  elif (((claves[cont][min[cont]-1]) == letras[cont]) and ((claves[cont][max[cont]-1]) == letras[cont])) or (((claves[cont][min[cont]-1]) != letras[cont]) and ((claves[cont][max[cont]-1]) != letras[cont])):
    #contador de si la clave tiene ambas posiciones igual o diferente a la letra. Esto la hace inválida.
    pw_invalida +=1
  else:
    #el resto de claves son válidas
    pw_valida +=1

print(pw_invalida)
print(pw_valida)