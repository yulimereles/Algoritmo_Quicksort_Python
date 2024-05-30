def quicksort(array):
    """
    Función Quicksort que ordena una lista.
    
    Parámetro:
    array (list): Lista de elementos a ordenar.
    
    Retorna:
    list: Lista ordenada.
    """
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(array) <= 1:
        return array
    
    # Selección del pivote: se elige el elemento del medio para mejorar el rendimiento en algunos casos
    pivot = array[len(array) // 2]

    # Listas de elementos menores, iguales y mayores que el pivote
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # Llamada recursiva y concatenación de los resultados
    return quicksort(left) + middle + quicksort(right)

# Prueba 1: Lista ordenada
print("Prueba 1: Lista ordenada")
print(quicksort([1, 2, 3, 4, 5]))

# Prueba 2: Lista desordenada
print("Prueba 2: Lista desordenada")
print(quicksort([5, 2, 8, 1, 9, 3, 7, 4, 6]))

# Prueba 3: Lista con elementos repetidos
print("Prueba 3: Lista con elementos repetidos")
print(quicksort([5, 2, 8, 1, 9, 3, 7, 4, 6, 5, 3]))

# Prueba 4: Lista vacía
print("Prueba 4: Lista vacía")
print(quicksort([]))

# Prueba 5: Lista con un solo elemento
print("Prueba 5: Lista con un solo elemento")
print(quicksort([42]))
