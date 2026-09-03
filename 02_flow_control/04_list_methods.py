###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###
import subprocess
import os

consola = 'cls' if os.name == 'nt' else 'clear'
subprocess.call(consola, shell=True)

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista) # Debería imprimir [0, 2, 10, 3, 4, 5, 6]

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
eliminado =lista_a.pop(3)
lista_b.clear()
print(f"Lista a: {lista_a}") # Debería imprimir Lista a: [2, 3, 4, 6, 1, 2]
print(f"Lista b: {lista_b}") # Debería imprimir Lista b: []

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:5]
print(lista)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
conteo = lista.count(2)
lista_siete = 7 in lista
print(f"Lista ordenada: {lista}") # Debería imprimir Lista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"El número 2 aparece {conteo} veces") # Debería imprimir El número 2 aparece 2 veces
print(f"¿Está el número 7 en la lista?: {lista_siete}") # Debería imprimir ¿Está el número 7 en la lista?: False

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(f"Original: {original}")       # Output: Original: [10, 2, 3]
print(f"Copia 1 (slicing): {copia_1}") # Output: Copia 1 (slicing): [1, 2, 3]
print(f"Copia 2 (copy()): {copia_2}") # Output: Copia 2 (copy()): [1, 2, 3]
print(f"Referencia: {referencia}")     # Output: Referencia: [10, 2, 3]

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str)
print(frutas)