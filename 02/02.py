def is_invalid(n):
    # Convierte el número a string para analizar sus dígitos
    s = str(n)
    # Solo es inválido si tiene un número par de dígitos
    if len(s) % 2 != 0:
        return False
    # Divide el string por la mitad
    half = len(s) // 2
    # Es inválido si la primera mitad es igual a la segunda mitad
    return s[:half] == s[half:]


def sum_invalid_ids(file_name):
    # Lee todos los rangos del archivo
    with open(file_name, "r") as f:
        lines = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            lines.append(line)
    
    total = 0
    print(lines)  # Debug: muestra los rangos leídos

    # Procesa cada rango de IDs
    for range_str in lines:
        if not range_str:
            continue
        # Extrae el inicio y fin del rango (formato: "inicio-fin")
        start, end = map(int, range_str.split("-"))
        # Verifica cada número en el rango
        for n in range(start, end + 1):
            if is_invalid(n):
                total += n

    return total


# Ejecutar parte 1
file_path = "02.txt"
print("Suma total de IDs inválidos:", sum_invalid_ids(file_path))


def is_invalid_pattern(n):
    # Convierte el número a string para analizar patrones
    s = str(n)
    length = len(s)

    # Prueba todos los tamaños posibles de patrón repetitivo
    for pattern_size in range(1, length // 2 + 1):
        # El patrón debe dividir exactamente la longitud total
        if length % pattern_size != 0:
            continue

        # Calcula cuántas veces se repite el patrón
        repetitions = length // pattern_size
        if repetitions < 2:
            continue

        # Extrae el patrón y verifica si se repite
        pattern = s[:pattern_size]
        if pattern * repetitions == s:
            return True

    return False


def sum_invalid_ids_pattern(file_name):
    # Lee todos los rangos del archivo
    with open(file_name, "r") as f:
        ranges = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            ranges.append(line)

    total = 0

    # Procesa cada rango usando el nuevo criterio de patrones repetitivos
    for range_str in ranges:
        start, end = map(int, range_str.split("-"))
        for n in range(start, end + 1):
            if is_invalid_pattern(n):
                total += n

    return total


# Ejecutar parte 2 (criterio de patrones repetitivos)
file_path = "02.txt"
print("Suma total de IDs inválidos (patrones):", sum_invalid_ids_pattern(file_path))
