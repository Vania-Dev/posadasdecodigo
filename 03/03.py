def max_joltage_for_bank(bank):
    """
    Dado un string con dígitos (ej. '987654321111111'),
    calcula el mayor número posible formado por dos dígitos sin reordenar.
    """
    max_value = 0
    
    # Recorre todas las parejas posibles manteniendo el orden (i < j)
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Forma el número de dos dígitos tomando dígitos en posiciones i y j
            number = int(bank[i] + bank[j])
            # Guarda el máximo valor encontrado
            if number > max_value:
                max_value = number
    
    return max_value


def total_output_joltage(file_name):
    """
    Suma el máximo joltage de cada banco.
    """
    # Lee todos los bancos de energía del archivo
    with open(file_name, "r") as f:
        banks = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            banks.append(line)
    
    # Calcula la suma total del joltage máximo de todos los bancos
    total = 0
    for bank in banks:
        total += max_joltage_for_bank(bank)
    return total


# Ejecutar parte 1
file_path = "03.txt"
print("Joltage total (parte 1):", total_output_joltage(file_path))


def best_joltage_subsequence(bank, k=12):
    """
    Devuelve la subsecuencia más grande posible de longitud k,
    manteniendo el orden de los dígitos.
    """
    # Calcula cuántos dígitos necesitamos eliminar para llegar a k dígitos
    digits_to_remove = len(bank) - k
    stack = []

    # Usa un algoritmo greedy con stack para encontrar la subsecuencia máxima
    for digit in bank:
        # Mientras podamos eliminar dígitos y el último en el stack sea menor al actual
        while digits_to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()  # Elimina el dígito menor
            digits_to_remove -= 1
        stack.append(digit)

    # Asegura que la longitud final sea exactamente k
    return "".join(stack[:k])


def total_max_joltage_optimized(file_name, k=12):
    """
    Suma los joltages máximos para cada banco,
    cada uno construido con k dígitos usando el algoritmo optimizado.
    """
    # Lee todos los bancos del archivo
    with open(file_name, "r") as f:
        banks = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            banks.append(line)
    
    # Calcula la suma total usando la mejor subsecuencia de k dígitos para cada banco
    total = 0
    for bank in banks:
        # Obtiene la mejor subsecuencia de k dígitos
        sequence = best_joltage_subsequence(bank, k)
        # Convierte la secuencia a entero y la suma al total
        total += int(sequence)
    return total

# Ejecutar parte 2 (algoritmo optimizado con subsecuencias)
file_path = "03.txt"
print("Joltage total optimizado (parte 2):", total_max_joltage_optimized(file_path))
