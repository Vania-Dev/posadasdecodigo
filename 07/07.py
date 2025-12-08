# Importa deque para cola eficiente y defaultdict para contadores
from collections import deque, defaultdict

def count_splits_from_file(filename):
    """Cuenta cuántas veces se divide el rayo de taquión."""
    # Abre y lee el archivo línea por línea
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Calcula las dimensiones de la grilla
    rows = len(lines)
    cols = max(len(l) for l in lines)
    # Normaliza todas las líneas al mismo ancho
    grid = [l.ljust(cols) for l in lines]

    # Busca la posición inicial marcada con 'S'
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
                break

    # Inicializa la cola con la posición inicial
    q = deque([start])
    # Set para evitar procesar la misma celda múltiples veces
    visited = set()
    # Set para rastrear qué divisores ya fueron activados
    used_splitters = set()
    # Contador de divisiones totales
    total_splits = 0

    # Procesa la cola mientras tenga elementos
    while q:
        # Extrae la siguiente posición de la cola
        r, c = q.popleft()

        # Si ya visitamos esta celda, la saltamos
        if (r, c) in visited:
            continue
        # Marca la celda como visitada
        visited.add((r, c))

        # Calcula la siguiente fila (el rayo se mueve hacia abajo)
        nr = r + 1
        # Si sale de la grilla, termina este rayo
        if nr >= rows:
            continue

        # Obtiene el contenido de la celda siguiente
        cell = grid[nr][c]

        # Si encuentra un divisor (^)
        if cell == '^':
            # Solo cuenta el divisor si es la primera vez que lo activa
            if (nr, c) not in used_splitters:
                used_splitters.add((nr, c))
                total_splits += 1

            # Genera dos nuevos rayos: uno a la izquierda y otro a la derecha
            if c - 1 >= 0:
                q.append((nr, c - 1))
            if c + 1 < cols:
                q.append((nr, c + 1))

        else:
            # Si no hay divisor, el rayo continúa hacia abajo
            q.append((nr, c))

    # Retorna el total de divisiones
    return total_splits

# EJECUCIÓN PARTE 1
filename = "07.txt"
total_splits = count_splits_from_file(filename)
print(total_splits)


def count_timelines_from_file(filename):
    """
    Lee el diagrama desde filename y devuelve la cantidad de timelines finales
    producidas por un único taquión bajo la interpretación many-worlds.
    """
    # Abre y lee el archivo
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Si el archivo está vacío, retorna 0
    if not lines:
        return 0

    # Calcula las dimensiones de la grilla
    rows = len(lines)
    cols = max(len(l) for l in lines)
    # Normaliza todas las líneas al mismo ancho
    grid = [l.ljust(cols) for l in lines]

    # Busca la posición inicial 'S'
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break
    # Valida que se haya encontrado la posición inicial
    if start is None:
        raise ValueError("No se encontró 'S' en el archivo")

    # Diccionario que mapea posición -> cantidad de timelines en esa posición
    counts = defaultdict(int)
    # Inicia con 1 timeline en la posición de inicio
    counts[start] = 1

    # Contador de timelines que han salido del diagrama
    final_timelines = 0

    # Propaga las timelines hacia abajo hasta que no queden activas
    while counts:
        # Diccionario para la siguiente iteración
        new_counts = defaultdict(int)

        # Procesa cada posición con timelines activas
        for (r, c), cnt in counts.items():
            # Calcula la siguiente fila (movimiento hacia abajo)
            nr = r + 1
            # Si sale del diagrama, estas timelines terminan
            if nr >= rows:
                final_timelines += cnt
                continue

            # Obtiene el contenido de la celda siguiente
            below = grid[nr][c]
            # Si encuentra un divisor
            if below == '^':
                # Cada timeline se divide en dos: izquierda y derecha
                for nc in (c - 1, c + 1):
                    # Solo cuenta si la nueva posición está dentro de la grilla
                    if 0 <= nc < cols:
                        new_counts[(nr, nc)] += cnt
                    # Las timelines que salen lateralmente se pierden
            else:
                # Si no hay divisor, las timelines continúan hacia abajo
                new_counts[(nr, c)] += cnt

        # Actualiza el diccionario de conteos para la siguiente iteración
        counts = new_counts

    # Retorna el total de timelines finales
    return final_timelines


# EJECUCIÓN PARTE 2
print(count_timelines_from_file("07.txt"))