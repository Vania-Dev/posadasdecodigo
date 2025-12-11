from collections import defaultdict

def count_paths_from_file(filename, start="you", target="out"):
    """
    Cuenta todos los caminos posibles desde un nodo inicial hasta un nodo objetivo.
    
    Args:
        filename: Archivo con la descripción del grafo
        start: Nodo de inicio (por defecto "you")
        target: Nodo objetivo (por defecto "out")
    
    Returns:
        Número total de caminos desde start hasta target
    """
    # --- Leer archivo y construir grafo ---
    graph = defaultdict(list)  # Diccionario que mapea cada nodo a sus conexiones
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():  # Saltar líneas vacías
                continue
            left, right = line.split(":")
            node = left.strip()  # Nodo origen
            outputs = right.strip().split()  # Lista de nodos destino
            graph[node] = outputs

    # --- DFS con memoización para evitar recálculos ---
    memo = {}  # Cache para almacenar resultados ya calculados

    def dfs(node):
        """
        Búsqueda en profundidad recursiva con memoización.
        Cuenta todos los caminos desde 'node' hasta 'target'.
        """
        # Caso base: si llegamos al objetivo, hay exactamente 1 camino
        if node == target:
            return 1
        
        # Si ya calculamos este nodo, devolver resultado guardado
        if node in memo:
            return memo[node]

        # Sumar todos los caminos desde los nodos vecinos
        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)

        # Guardar resultado en cache y devolverlo
        memo[node] = total
        return total

    return dfs(start)


def count_paths_with_devices(filename, start="svr", target="out", must_have=("dac", "fft")):
    """
    Cuenta caminos desde start hasta target que DEBEN pasar por todos los dispositivos especificados.
    
    Args:
        filename: Archivo con la descripción del grafo
        start: Nodo de inicio (por defecto "svr" - servidor)
        target: Nodo objetivo (por defecto "out" - salida)
        must_have: Tupla de dispositivos que DEBEN visitarse (dac, fft)
    
    Returns:
        Número de caminos válidos que pasan por todos los dispositivos requeridos
    """
    # --- Leer archivo y construir grafo ---
    graph = defaultdict(list)  # Diccionario que mapea cada nodo a sus conexiones
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():  # Saltar líneas vacías
                continue
            left, right = line.split(":")
            node = left.strip()  # Nodo origen
            outputs = right.strip().split()  # Lista de nodos destino
            graph[node] = outputs

    required = set(must_have)  # Conjunto de dispositivos que DEBEN visitarse

    # Cache: memo[(nodo_actual, dispositivos_visitados)] = número_de_caminos_válidos
    memo = {}

    def dfs(node, visited):
        """
        Búsqueda en profundidad que rastrea qué dispositivos requeridos hemos visitado.
        
        Args:
            node: Nodo actual en el recorrido
            visited: frozenset con los dispositivos requeridos ya visitados
        
        Returns:
            Número de caminos válidos desde este punto
        """
        # Crear clave única para memoización
        key = (node, visited)
        if key in memo:
            return memo[key]

        # Caso base: si llegamos al objetivo
        if node == target:
            # Solo es válido si visitamos TODOS los dispositivos requeridos
            return 1 if visited == required else 0

        # Actualizar conjunto de visitados si el nodo actual es requerido
        new_visited = visited | ({node} & required)

        # Sumar caminos válidos desde todos los nodos vecinos
        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, new_visited)

        # Guardar resultado en cache y devolverlo
        memo[key] = total
        return total

    # Iniciar búsqueda desde el nodo de inicio con conjunto vacío de visitados
    return dfs(start, frozenset())


# --- Ejecución de las soluciones ---
if __name__ == "__main__":
    # Parte 1: Contar todos los caminos desde "you" hasta "out"
    print("Parte 1 - Total de caminos:", count_paths_from_file("11.txt"))
    
    # Parte 2: Contar caminos desde "svr" hasta "out" que pasen por "dac" y "fft"
    print("Parte 2 - Caminos que pasan por dac y fft:", count_paths_with_devices("11.txt"))