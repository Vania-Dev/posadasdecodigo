def is_accessible(grid, r, c):
    """
    Verifica si un rollo '@' en la posición (r, c)
    tiene menos de 4 rollos en las casillas adyacentes.
    """
    # Obtener el número total de filas en la grilla
    rows = len(grid)
    # Obtener el número total de columnas (usando la primera fila como referencia)
    cols = len(grid[0])
    
    # Lista con las 8 direcciones posibles alrededor de una casilla
    # Cada tupla representa (cambio_fila, cambio_columna)
    # (-1,-1) = arriba-izquierda, (-1,0) = arriba, (-1,1) = arriba-derecha
    # (0,-1) = izquierda, (0,1) = derecha
    # (1,-1) = abajo-izquierda, (1,0) = abajo, (1,1) = abajo-derecha
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    # Contador para los rollos adyacentes encontrados
    count_adjacent = 0
    
    # Revisar cada una de las 8 direcciones
    for dr, dc in dirs:
        # Calcular la nueva posición sumando el offset a la posición actual
        nr, nc = r + dr, c + dc
        # Verificar que la nueva posición esté dentro de los límites de la grilla
        if 0 <= nr < rows and 0 <= nc < cols:
            # Si en esa posición hay un rollo ('@'), incrementar el contador
            if grid[nr][nc] == '@':
                count_adjacent += 1
    
    # Retornar True si hay menos de 4 rollos adyacentes (es accesible)
    return count_adjacent < 4


def count_accessible_rolls(file_name):
    """
    Cuenta cuántos '@' son accesibles.
    """
    # Abrir el archivo en modo lectura usando 'with' para cerrarlo automáticamente
    with open(file_name, "r") as f:
        # Crear una lista vacía para almacenar las líneas de la grilla
        grid = []
        # Leer cada línea del archivo
        for line in f:
            # Eliminar espacios en blanco al inicio y final de la línea
            line = line.strip()
            # Si la línea está vacía, saltarla
            if not line:
                continue
            # Agregar la línea a la grilla
            grid.append(line)
    
    # Inicializar contador de rollos accesibles
    total = 0
    # Recorrer cada fila de la grilla
    for r in range(len(grid)):
        # Recorrer cada columna de la fila actual
        for c in range(len(grid[0])):
            # Si en esta posición hay un rollo ('@')
            if grid[r][c] == '@':
                # Verificar si es accesible usando la función anterior
                if is_accessible(grid, r, c):
                    # Si es accesible, incrementar el contador
                    total += 1
    # Retornar el total de rollos accesibles
    return total


# PARTE 1: Ejecutar el ejemplo del problema
# Definir la ruta del archivo con los datos de entrada
file_path = "04.txt"
# Imprimir el resultado de contar rollos accesibles
print(count_accessible_rolls(file_path))


def count_adjacent_rolls(grid, r, c):
    # Obtener dimensiones de la grilla
    rows = len(grid)
    cols = len(grid[0])
    # Definir las 8 direcciones posibles (igual que antes)
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    # Inicializar contador de rollos adyacentes
    count = 0

    # Revisar cada dirección
    for dr, dc in dirs:
        # Calcular nueva posición
        nr, nc = r + dr, c + dc
        # Verificar que esté dentro de los límites
        if 0 <= nr < rows and 0 <= nc < cols:
            # Si hay un rollo en esa posición, contar
            if grid[nr][nc] == '@':
                count += 1
    # Retornar el número total de rollos adyacentes
    return count


def find_accessible(grid):
    """
    Devuelve una lista con coordenadas de rollos accesibles.
    """
    # Crear lista vacía para almacenar coordenadas de rollos accesibles
    accessible = []
    # Recorrer cada fila de la grilla
    for r in range(len(grid)):
        # Recorrer cada columna de la fila actual
        for c in range(len(grid[0])):
            # Si en esta posición hay un rollo
            if grid[r][c] == '@':
                # Contar cuántos rollos tiene alrededor
                neighbors = count_adjacent_rolls(grid, r, c)
                # Si tiene menos de 4 vecinos, es accesible
                if neighbors < 4:
                    # Agregar las coordenadas (fila, columna) a la lista
                    accessible.append((r, c))
    # Retornar la lista de coordenadas accesibles
    return accessible


def total_removable_rolls(file_name):
    """
    Repite el proceso hasta que no se puedan quitar más rollos.
    Devuelve cuántos rollos totales fueron eliminados.
    """
    # Leer el archivo de la misma manera que antes
    with open(file_name, "r") as f:
        grid = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            grid.append(line)
    
    # Convertir cada string (fila) en una lista de caracteres
    # Esto permite modificar la grilla (los strings son inmutables)
    g = [list(row) for row in grid]

    # Contador total de rollos eliminados
    total_removed = 0

    # Bucle infinito que se rompe cuando no hay más rollos accesibles
    while True:
        # Encontrar todos los rollos accesibles en el estado actual
        accessible = find_accessible(g)

        # Si no hay rollos accesibles, terminar el bucle
        if not accessible:
            break  # no hay más rollos accesibles

        # Eliminar todos los rollos accesibles encontrados
        for r, c in accessible:
            # Cambiar el rollo '@' por un espacio vacío '.'
            g[r][c] = '.'

        # Sumar la cantidad de rollos eliminados en esta iteración
        total_removed += len(accessible)

    # Retornar el total de rollos eliminados
    return total_removed


# PARTE 2: Ejecutar el ejemplo del problema
# Usar el mismo archivo de entrada
file_path = "04.txt"
# Imprimir el total de rollos que se pueden eliminar
print(total_removable_rolls(file_path))
