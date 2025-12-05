def parse_input(file_name):
    """
    Recibe las líneas del input y separa:
    - lista de rangos frescos
    - lista de IDs disponibles
    """
    # Abrir el archivo en modo lectura usando 'with' para cerrarlo automáticamente
    with open(file_name, "r") as file:
        # Crear una lista para almacenar todas las líneas del archivo
        lines = [line.rstrip("\n") for line in file]
    
    # Crear listas vacías para almacenar rangos e IDs
    fresh_ranges = []  # Lista para los rangos de ingredientes frescos
    ingredient_ids = []  # Lista para los IDs de ingredientes disponibles

    # Variable para saber si ya encontramos la línea en blanco
    blank_line_found = False

    # Recorrer cada línea del archivo
    for line in lines:
        # Eliminar espacios en blanco al inicio y final
        line = line.strip()
        # Si la línea está vacía, cambiar el estado
        if line == "":
            blank_line_found = True
            continue  # Saltar a la siguiente línea

        # Si aún no hemos encontrado la línea en blanco
        if not blank_line_found:
            # Es un rango tipo "3-5", separar por el guión
            start_range, end_range = map(int, line.split("-"))
            # Agregar el rango como tupla a la lista
            fresh_ranges.append((start_range, end_range))
        else:
            # Después de la línea en blanco, son IDs individuales
            ingredient_ids.append(int(line))

    # Retornar ambas listas
    return fresh_ranges, ingredient_ids


def is_fresh(ingredient_id, fresh_ranges):
    """
    Devuelve True si el ID está dentro de al menos un rango.
    """
    # Revisar cada rango en la lista de rangos frescos
    for start_range, end_range in fresh_ranges:
        # Si el ID está dentro del rango (inclusive)
        if start_range <= ingredient_id <= end_range:
            return True  # El ingrediente es fresco
    # Si no está en ningún rango, no es fresco
    return False


def count_fresh_ids(fresh_ranges, ingredient_ids):
    """
    Cuenta cuántos IDs son frescos.
    """
    # Usar comprensión de lista para contar IDs frescos
    # Para cada ID en la lista, verificar si es fresco y sumar 1
    return sum(1 for ingredient_id in ingredient_ids if is_fresh(ingredient_id, fresh_ranges))


# ----- PARTE 1: EJEMPLO DEL PROBLEMA -----

# Definir el nombre del archivo de entrada
file_name = "05.txt"

# Parsear el archivo para obtener rangos e IDs
fresh_ranges, ingredient_ids = parse_input(file_name)
# Imprimir la cantidad de IDs frescos
print(count_fresh_ids(fresh_ranges, ingredient_ids))


def parse_range_line(line):
    """
    Convierte una línea 'A-B' en una tupla (A, B).
    """
    # Verificar que la línea contenga un guión
    if '-' not in line:
        return None  # Retornar None si no es un rango válido
    
    # Separar la línea por el guión
    start_str, end_str = line.split('-')
    # Convertir a enteros y retornar como tupla
    return int(start_str), int(end_str)


def merge_ranges(ranges_list):
    """
    Recibe una lista de rangos y devuelve una versión
    fusionada sin traslapes.
    """
    # Filtrar valores None de la lista
    valid_ranges = [range_tuple for range_tuple in ranges_list if range_tuple is not None]
    # Ordenar los rangos por su valor inicial
    sorted_ranges = sorted(valid_ranges, key=lambda x: x[0])
    # Lista para almacenar los rangos fusionados
    merged_ranges = []

    # Procesar cada rango ordenado
    for start, end in sorted_ranges:
        # Si es el primer rango, agregarlo directamente
        if not merged_ranges:
            merged_ranges.append([start, end])
            continue  # Continuar con el siguiente rango

        # Obtener el último rango agregado
        last_start, last_end = merged_ranges[-1]

        # Si hay traslape o son contiguos (diferencia de 1)
        if start <= last_end + 1:
            # Fusionar rangos: extender el final al máximo
            merged_ranges[-1][1] = max(last_end, end)
        else:
            # No hay traslape, agregar como nuevo rango
            merged_ranges.append([start, end])

    # Retornar la lista de rangos fusionados
    return merged_ranges


def count_total_fresh_ids(merged_ranges):
    """
    Dado un conjunto de rangos fusionados,
    cuenta cuántos IDs únicos existen.
    """
    # Inicializar contador total
    total_ids = 0
    # Recorrer cada rango fusionado
    for start, end in merged_ranges:
        # Calcular cuántos números hay en el rango (inclusive)
        # Ejemplo: rango 3-5 tiene 3 números (3, 4, 5) = 5-3+1 = 3
        total_ids += (end - start + 1)
    # Retornar el total de IDs únicos
    return total_ids


def process_fresh_ingredients_file(file_path):
    """
    Función principal que:
      1) lee el archivo,
      2) obtiene rangos,
      3) los fusiona,
      4) cuenta IDs únicos frescos.
    """
    # Abrir y leer todas las líneas del archivo
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]

    # Procesar solo las líneas que contienen rangos (tienen guión)
    ranges_list = [parse_range_line(line) for line in lines if '-' in line]

    # Fusionar los rangos para eliminar traslapes
    merged_ranges = merge_ranges(ranges_list)

    # Contar el total de IDs únicos en los rangos fusionados
    return count_total_fresh_ids(merged_ranges)


# ----- PARTE 2: PROCESAR ARCHIVO COMPLETO -----

# Procesar el archivo para obtener el total de IDs frescos
result = process_fresh_ingredients_file("05.txt")
# Imprimir el resultado final
print("Total de IDs frescos:", result)
