# Parte 1: Encuentra el rectángulo más grande usando cualquier par de tiles rojos como esquinas
def largest_rectangle_from_file(filename):
    red_tiles = []

    # Leer archivo y extraer coordenadas
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                red_tiles.append((x, y))

    max_area = 0

    # Calcular área máxima probando cada par de tiles rojos
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            width = abs(x2 - x1) + 1   # +1 porque las celdas se cuentan
            height = abs(y2 - y1) + 1

            area = width * height

            if area > max_area:
                max_area = area

    return max_area


# Ejecutar con el archivo input.txt
print(largest_rectangle_from_file("09.txt"))


import functools
import os
import time
from itertools import combinations


# Decorador para medir el tiempo de ejecución de una función
def timer(func):
    """Decorator to measure the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function to execute the decorated function and print its runtime."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] Result: {result}")
        duration = end - start
        time_units = {
            "ns": (1e-6, 1e9),
            "us": (1e-3, 1e6),
            "ms": (1, 1e3),
            "s": (float("inf"), 1),
        }
        for unit, (threshold, multiplier) in time_units.items():
            if duration < threshold:
                print(f"[{func.__name__}] Time: {duration * multiplier:.4f} {unit}")
                break
        return result

    return wrapper


def read_input() -> str:
    """Read and parse the input file."""
    input_path = os.path.join(os.path.dirname(__file__), "09.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read().strip()


# Convierte el texto de entrada en una lista de coordenadas (x, y)
def parse_tiles(data: str) -> list[tuple[int, int]]:
    """Parse input data into a list of coordinate tuples."""
    tiles = []
    for line in data.splitlines():
        parts = line.split(",")
        tiles.append((int(parts[0]), int(parts[1])))
    return tiles


# Crea los bordes del polígono conectando tiles rojos consecutivos
# Cada borde es una tupla (min_x, min_y, max_x, max_y)
def get_normalized_edges(
    tiles: list[tuple[int, int]],
) -> list[tuple[int, int, int, int]]:
    """Convert tiles into a list of normalized edge tuples (min_x, min_y, max_x, max_y)."""
    edges = []
    n = len(tiles)
    # Conectar cada tile con el siguiente
    for i in range(n - 1):
        p1 = tiles[i]
        p2 = tiles[i + 1]
        edges.append(
            (
                min(p1[0], p2[0]),
                min(p1[1], p2[1]),
                max(p1[0], p2[0]),
                max(p1[1], p2[1]),
            )
        )

    # Conectar el último tile con el primero para cerrar el loop
    p_last = tiles[-1]
    p_first = tiles[0]
    edges.append(
        (
            min(p_last[0], p_first[0]),
            min(p_last[1], p_first[1]),
            max(p_last[0], p_first[0]),
            max(p_last[1], p_first[1]),
        )
    )
    return edges


def calculate_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Calculate rectangle area including both corners."""
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


# Verifica si un rectángulo está completamente dentro del polígono
# Retorna True si no intersecta con ningún borde
def is_fully_contained(
    edges: list[tuple[int, int, int, int]],
    min_x: int,
    min_y: int,
    max_x: int,
    max_y: int,
) -> bool:
    """Check if the rectangle is fully contained."""
    # Si el rectángulo intersecta con algún borde, no está contenido
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return False
    return True


# Parte 2: Encuentra el rectángulo más grande que esté completamente dentro del polígono
# Solo considera rectángulos que no intersecten con los bordes del loop
@timer
def part2_opt(data: str) -> int:
    """Find the largest rectangle fully contained within the polygon."""
    tiles = parse_tiles(data)
    edges = get_normalized_edges(tiles)

    result = 0

    # Probar todas las combinaciones de pares de tiles rojos
    for p1, p2 in combinations(tiles, 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        # Optimización: saltar si el área es menor o igual al resultado actual
        if area <= result:
            continue

        # Calcular los límites del rectángulo
        min_x, max_x = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
        min_y, max_y = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])

        # Verificar si el rectángulo está completamente dentro del polígono
        if is_fully_contained(edges, min_x, min_y, max_x, max_y):
            result = area

    return result


def main():
    """Execute the solution for both parts."""
    input_data = read_input()
    part2_opt(input_data)


if __name__ == "__main__":
    main()