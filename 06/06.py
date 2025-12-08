def read_matrix(path):
    """Lee el archivo manteniendo espacios y devuelve una lista de strings."""
    # Abre el archivo en modo lectura
    with open(path, "r") as f:
        # Lee cada línea eliminando el salto de línea al final
        lines = [line.rstrip("\n") for line in f]
    # Retorna la lista de líneas
    return lines


def transpose(matrix):
    """
    Convierte filas en columnas asegurando que todas tengan el mismo largo.
    Rellena con espacios a la derecha si es necesario.
    """
    # Encuentra la longitud máxima de todas las filas
    max_len = max(len(row) for row in matrix)
    # Normaliza todas las filas al mismo largo rellenando con espacios
    normalized = [row.ljust(max_len) for row in matrix]
    # Transpone la matriz: convierte filas en columnas usando zip
    return list(zip(*normalized))


def separate_blocks(columns):
    """
    Recibe columnas (tuplas de caracteres) y agrupa en bloques
    separando cuando hay una columna completamente vacía (solo espacios).
    """
    # Lista para almacenar todos los bloques
    blocks = []
    # Bloque actual en construcción
    current = []

    # Itera sobre cada columna
    for col in columns:
        # Si la columna solo contiene espacios, es un separador
        if all(c == " " for c in col):
            # Si hay un bloque actual, lo guarda
            if current:
                blocks.append(current)
                current = []
        else:
            # Agrega la columna al bloque actual
            current.append(col)

    # Agrega el último bloque si existe
    if current:
        blocks.append(current)

    # Retorna la lista de bloques
    return blocks


def process_block(block):
    """
    Un bloque es una lista de columnas que contiene un problema.
    Se extraen los números (de arriba hacia abajo) y el operador (última fila).
    """
    # Convierte las columnas de vuelta a filas
    rows = list(zip(*block))

    # La última fila contiene el operador
    last_row = rows[-1]
    # Extrae los operadores válidos (+ o *)
    operators = [c for c in last_row if c in "+*"]
    # Valida que haya exactamente un operador
    if len(operators) != 1:
        raise ValueError("Bloque inválido, no contiene un operador único")
    operator = operators[0]

    # Las filas anteriores contienen números
    numbers = []
    for row in rows[:-1]:
        # Une los caracteres de la fila y elimina espacios
        s = "".join(row).strip()
        # Si es un número válido, lo agrega a la lista
        if s.isdigit():
            numbers.append(int(s))

    # Valida que haya al menos un número
    if not numbers:
        raise ValueError("Bloque sin números")

    # Calcula el resultado según el operador
    if operator == "+":
        # Suma todos los números
        result = sum(numbers)
    else:
        # Multiplica todos los números
        result = 1
        for n in numbers:
            result *= n

    # Retorna el resultado del problema
    return result


def solve_worksheet(path):
    """Resuelve la hoja de trabajo completa y retorna el total."""
    # Lee la matriz del archivo
    matrix = read_matrix(path)
    # Transpone para trabajar con columnas
    columns = transpose(matrix)
    # Separa en bloques (problemas individuales)
    blocks = separate_blocks(columns)

    # Suma los resultados de todos los problemas
    total = 0
    for b in blocks:
        total += process_block(b)

    # Retorna el total acumulado
    return total


# EJECUCIÓN PARTE 1
total = solve_worksheet("06.txt")
print("Grand total:", total)


def solve_cephalopod_file(filename, verbose=False):
    """Resuelve la hoja de trabajo leyendo de derecha a izquierda."""
    # Abre el archivo y lee todas las líneas
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Valida que el archivo no esté vacío
    if not lines:
        raise ValueError("El archivo está vacío")

    # Calcula las dimensiones de la grilla
    height = len(lines)
    width = max(len(line) for line in lines)
    # Crea una grilla normalizada con todas las filas del mismo ancho
    grid = [list(line.ljust(width)) for line in lines]

    # Encuentra grupos de columnas no vacías separadas por columnas de espacios
    groups = []
    current = []
    # Itera sobre cada índice de columna
    for c in range(width):
        # Extrae todos los caracteres de la columna c
        col = [grid[r][c] for r in range(height)]
        # Si la columna solo tiene espacios, es un separador
        if all(ch == " " for ch in col):
            # Guarda el grupo actual si existe
            if current:
                groups.append(current)
                current = []
        else:
            # Agrega el índice de columna al grupo actual
            current.append(c)
    # Agrega el último grupo si existe
    if current:
        groups.append(current)

    # Invierte los grupos para leer de derecha a izquierda
    groups = groups[::-1]

    # Acumulador del total general
    grand_total = 0
    # Lista para almacenar detalles de cada problema
    problems_details = []

    # Procesa cada grupo (problema)
    for gi, cols in enumerate(groups, start=1):
        # Inicializa operador y operandos para este problema
        operator = None
        operands = []

        # Lee las columnas del grupo de derecha a izquierda
        for c in reversed(cols):
            # Extrae todos los caracteres de la columna
            colchars = [grid[r][c] for r in range(height)]
            # Obtiene el carácter inferior de la columna
            bottom = colchars[-1]
            # Si el carácter inferior es un operador, lo registra
            if bottom in "+*":
                operator = bottom

            # Extrae solo los dígitos de la columna
            digits = "".join(ch for ch in colchars if ch.isdigit())
            # Si hay dígitos, los convierte a número y agrega a operandos
            if digits:
                operands.append(int(digits))

        # Valida que se haya encontrado un operador
        if operator is None:
            raise ValueError(f"No se encontró operador (+ o *) en el problema con columnas {cols}")

        # Calcula el resultado según el operador
        if operator == "+":
            # Suma todos los operandos
            result = sum(operands)
            op_symbol = "+"
        else:
            # Multiplica todos los operandos
            result = 1
            for n in operands:
                result *= n
            op_symbol = "*"

        # Acumula el resultado al total general
        grand_total += result
        # Guarda los detalles del problema
        problems_details.append({
            "group_index_from_right": gi,
            "cols": cols,
            "operator": op_symbol,
            "operands": operands,
            "result": result
        })

    # Si el modo verbose está activado, imprime detalles
    if verbose:
        for pd in problems_details:
            cols = pd["cols"]
            print(f"Problema (desde la derecha) #{pd['group_index_from_right']}: columnas {cols}")
            print(f"  Operador: {pd['operator']}")
            print(f"  Operandos (en orden de evaluación): {pd['operands']}")
            print(f"  Resultado: {pd['result']}")
            print()

        print("Gran total:", grand_total)

    # Retorna el total general
    return grand_total


# EJECUCIÓN PARTE 2
result = solve_cephalopod_file("06.txt")
print("Grand total (parte 2):", result)
