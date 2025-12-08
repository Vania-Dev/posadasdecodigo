# Importa combinations para generar pares de puntos
from itertools import combinations

class DSU:
    """Disjoint Set Union (Union-Find) para agrupar elementos en conjuntos."""
    def __init__(self, n):
        # Inicializa cada elemento como su propio padre
        self.parent = list(range(n))
        # Inicializa el tamaño de cada conjunto en 1
        self.size = [1] * n

    def find(self, x):
        """Encuentra la raíz del conjunto al que pertenece x (con compresión de ruta)."""
        # Si x no es su propio padre, busca recursivamente y comprime la ruta
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        # Retorna la raíz del conjunto
        return self.parent[x]

    def union(self, a, b):
        """Une los conjuntos que contienen a y b."""
        # Encuentra las raíces de ambos elementos
        ra = self.find(a)
        rb = self.find(b)
        # Si ya están en el mismo conjunto, no hace nada
        if ra == rb:
            return False
        # Une el conjunto más pequeño al más grande
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        # Actualiza el padre del conjunto más pequeño
        self.parent[rb] = ra
        # Actualiza el tamaño del conjunto resultante
        self.size[ra] += self.size[rb]
        # Retorna True indicando que la unión fue útil
        return True


def read_points(filename):
    """Lee las coordenadas 3D de los puntos desde un archivo."""
    # Lista para almacenar todos los puntos
    points = []
    # Abre el archivo en modo lectura
    with open(filename, "r") as f:
        # Procesa cada línea del archivo
        for line in f:
            # Salta líneas vacías
            if not line.strip():
                continue
            # Separa las coordenadas por comas y las convierte a enteros
            x, y, z = map(int, line.strip().split(","))
            # Agrega la tupla de coordenadas a la lista
            points.append((x, y, z))
    # Retorna la lista de puntos
    return points


def solve(points, K):
    """Conecta los K pares más cercanos y retorna el producto de los 3 grupos más grandes."""
    # Obtiene el número total de puntos
    n = len(points)
    # Crea una estructura DSU para n puntos
    dsu = DSU(n)

    # Lista para almacenar todas las aristas con sus distancias
    edges = []
    # Genera todas las combinaciones posibles de pares de puntos
    for i, j in combinations(range(n), 2):
        # Obtiene las coordenadas del primer punto
        x1, y1, z1 = points[i]
        # Obtiene las coordenadas del segundo punto
        x2, y2, z2 = points[j]

        # Calcula la distancia euclidiana al cuadrado (evita raíz cuadrada)
        dist2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

        # Agrega la arista con su distancia y los índices de los puntos
        edges.append((dist2, i, j))

    # Ordena las aristas por distancia (de menor a mayor)
    edges.sort()

    # Conecta los K pares más cercanos
    for i in range(K):
        # Extrae la distancia y los índices de los puntos
        dist2, a, b = edges[i]
        # Une los dos puntos en el mismo grupo
        dsu.union(a, b)

    # Cuenta cuántos puntos hay en cada grupo
    groups = {}
    for i in range(n):
        # Encuentra la raíz del grupo al que pertenece el punto i
        root = dsu.find(i)
        # Incrementa el contador del grupo
        groups[root] = groups.get(root, 0) + 1

    # Ordena los tamaños de los grupos de mayor a menor
    sizes = sorted(groups.values(), reverse=True)
    # Retorna el producto de los tres grupos más grandes
    return sizes[0] * sizes[1] * sizes[2]


def solve_part2(points):
    """Encuentra la primera conexión que une todos los puntos en un solo grupo."""
    # Obtiene el número total de puntos
    n = len(points)
    # Crea una estructura DSU para n puntos
    dsu = DSU(n)
    
    # Lista para almacenar todas las aristas con sus distancias
    edges = []
    # Genera todas las combinaciones posibles de pares de puntos
    for i, j in combinations(range(n), 2):
        # Obtiene las coordenadas de ambos puntos
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        # Calcula la distancia euclidiana al cuadrado
        dist2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
        # Agrega la arista a la lista
        edges.append((dist2, i, j))
    
    # Ordena las aristas por distancia
    edges.sort()
    
    # Procesa las aristas en orden de distancia
    for dist2, a, b in edges:
        # Intenta unir los dos puntos
        if dsu.union(a, b):
            # Si después de la unión todos los puntos están conectados
            if dsu.size[dsu.find(a)] == n:
                # Retorna el producto de las coordenadas X de los dos puntos
                return points[a][0] * points[b][0]


# EJECUCIÓN
points = read_points("08.txt")
# Parte 1: Conecta los 1000 pares más cercanos
# print("Part 1:", solve(points, 1000))
# Parte 2: Encuentra la primera conexión que une todo
print("Part 2:", solve_part2(points))
