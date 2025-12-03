def calculate_password_from_file(file_name):
    # El dial comienza apuntando al número 50
    dial = 50
    # Contador de veces que el dial apunta a 0
    zeros = 0

    with open(file_name, "r") as file:
        for line in file:
            instruction = line.strip()
            if not instruction:
                continue  # Ignora líneas vacías

            # Extrae la dirección ('L' o 'R') y el valor numérico
            direction = instruction[0]      # 'L' para izquierda, 'R' para derecha
            value = int(instruction[1:])    # Número de clics a rotar

            # Rota el dial según la dirección
            if direction == "L":
                dial = (dial - value) % 100  # Rotación hacia la izquierda
            elif direction == "R":
                dial = (dial + value) % 100  # Rotación hacia la derecha

            # Cuenta si el dial apunta a 0 después de la rotación
            if dial == 0:
                zeros += 1

    return zeros


# Ejecutar parte 1
file_path = "01_test.txt"
result = calculate_password_from_file(file_path)
print("La contraseña real es:", result)


def count_zeros_in_right_rotation(position, steps):
    """
    Cuenta cuántas veces (entre los pasos 1..steps) la posición (position + k) % 100 == 0.
    position en 0..99, steps >= 0
    """
    if steps <= 0:
        return 0
    # Calcula el primer paso k donde (position + k) % 100 == 0
    # k tal que position + k ≡ 0 (mod 100) => k ≡ (100 - position) % 100
    first_k = (100 - position) % 100
    if first_k == 0:
        first_k = 100
    if steps < first_k:
        return 0
    # Cuenta cuántas veces ocurre el cero en el rango de pasos
    return 1 + (steps - first_k) // 100

def count_zeros_in_left_rotation(position, steps):
    """
    Cuenta cuántas veces (entre los pasos 1..steps) la posición (position - k) % 100 == 0.
    Esto ocurre cuando k ≡ position (mod 100).
    """
    if steps <= 0:
        return 0
    # Para rotación izquierda, el primer k donde llegamos a 0 es igual a la posición actual
    first_k = position % 100
    if first_k == 0:
        first_k = 100
    if steps < first_k:
        return 0
    # Cuenta cuántas veces ocurre el cero en el rango de pasos
    return 1 + (steps - first_k) // 100

def calculate_password_optimized(file_name):
    # Posición inicial del dial
    position = 50
    # Contador total de ceros encontrados durante todas las rotaciones
    total_zeros = 0

    with open(file_name, "r") as f:
        for line in f:
            instruction = line.strip()
            if not instruction:
                continue
            # Extrae dirección y número de pasos
            direction = instruction[0].upper()
            steps = int(instruction[1:])

            # Cuenta los ceros que ocurren durante la rotación (no solo al final)
            if direction == 'R':
                total_zeros += count_zeros_in_right_rotation(position, steps)
                position = (position + steps) % 100
            elif direction == 'L':
                total_zeros += count_zeros_in_left_rotation(position, steps)
                position = (position - steps) % 100
            else:
                raise ValueError(f"Instrucción desconocida: {instruction}")

    return total_zeros


# Ejecutar parte 2 (método optimizado)
file_path = "01.txt"
print("La contraseña (método optimizado) es:", calculate_password_optimized(file_path))
