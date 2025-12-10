# Importar librerías necesarias
from itertools import product  # Para generar todas las combinaciones posibles
import time                    # Para medir el tiempo de ejecución
import re                      # Para usar expresiones regulares
import scipy                   # Para optimización matemática

def parse_line(line):
    """Función para analizar cada línea del archivo de entrada"""
    # Extraer el diagrama que está entre corchetes []
    diagram = line.split('[')[1].split(']')[0]  # Dividir por '[' y ']' para obtener el contenido
    # Convertir el diagrama a lista binaria: '#' = 1, cualquier otro = 0
    target = [1 if c == '#' else 0 for c in diagram]

    # Extraer todos los botones que están entre paréntesis ()
    parts = line.split(')')  # Dividir la línea por ')'
    buttons = []             # Lista para almacenar los botones
    for p in parts:          # Recorrer cada parte
        if '(' in p:         # Si la parte contiene '('
            inside = p.split('(')[1]  # Obtener el contenido después de '('
            inside = inside.strip()   # Quitar espacios en blanco
            if inside:                # Si hay contenido
                # Convertir los números separados por comas a enteros
                nums = [int(x) for x in inside.split(',') if x.strip().isdigit()]
                buttons.append(nums)  # Agregar la lista de números a botones

    return target, buttons  # Devolver el objetivo y los botones


def min_presses(target, buttons):
    """Función para encontrar el mínimo número de presiones de botones"""
    n = len(buttons)  # Número de botones disponibles
    m = len(target)   # Longitud del patrón objetivo

    # Convertir cada botón en un vector binario
    bvecs = []        # Lista para almacenar vectores binarios
    for btn in buttons:  # Para cada botón
        v = [0] * m      # Crear vector de ceros del tamaño del objetivo
        for idx in btn:  # Para cada índice que afecta el botón
            if idx < m:  # Si el índice está dentro del rango
                v[idx] ^= 1  # Aplicar XOR (cambiar el bit)
        bvecs.append(v)  # Agregar el vector a la lista

    best = float('inf')  # Inicializar el mejor resultado como infinito

    # Fuerza bruta: probar todas las combinaciones 0/1 para cada botón
    for mask in product([0, 1], repeat=n):  # Generar todas las combinaciones
        presses = sum(mask)  # Contar cuántos botones se presionan
        if presses >= best:  # Si ya tenemos una solución mejor
            continue         # Saltar esta combinación

        state = [0] * m      # Estado inicial (todas las luces apagadas)
        # Aplicar el efecto de cada botón presionado
        for use, v in zip(mask, bvecs):  # Para cada botón y su vector
            if use:          # Si el botón se presiona (use = 1)
                # Aplicar XOR entre el estado actual y el efecto del botón
                state = [(a ^ b) for a, b in zip(state, v)]

        if state == target:  # Si el estado final coincide con el objetivo
            best = presses   # Actualizar el mejor resultado

    return best  # Devolver el mínimo número de presiones


def solve_file(filename):
    """Función para resolver todas las líneas del archivo"""
    total = 0  # Contador total de presiones
    with open(filename, "r") as f:  # Abrir el archivo en modo lectura
        for line in f:              # Leer línea por línea
            line = line.strip()     # Quitar espacios y saltos de línea
            if not line:            # Si la línea está vacía
                continue            # Saltar a la siguiente línea
            target, buttons = parse_line(line)  # Analizar la línea
            total += min_presses(target, buttons)  # Sumar las presiones mínimas
    return total  # Devolver el total


# Leer todo el archivo de entrada
with open("10.txt", 'r') as f:
    inp = f.read()  # Leer todo el contenido del archivo

# Dividir el contenido en líneas
inp = inp.split('\n')
# Si la última línea está vacía, eliminarla
if len(inp[-1]) == 0:
    inp.pop()

# Listas para almacenar los datos procesados
machines = []  # Patrones de las máquinas
buttons = []   # Botones de cada máquina
joltages = []  # Valores de voltaje objetivo

# Procesar cada línea del archivo
for line in inp:
    # Extraer el patrón de la máquina (entre corchetes [])
    mach = re.findall(r'\[([^\]]*)\]', line)
    machines.append(mach[0])  # Agregar el primer patrón encontrado

    # Extraer los botones (entre paréntesis ())
    buts = re.findall(r'\(([^\(]*)\)', line)
    # Convertir cada grupo de botones a lista de enteros
    buts = [[int(x) for x in but.split(',')] for but in buts]
    buttons.append(buts)  # Agregar la lista de botones

    # Extraer los voltajes objetivo (entre llaves {})
    jolts = re.findall(r'\{([^\{]*)\}', line)
    # Convertir los voltajes a lista de enteros
    jolts = [int(x) for x in jolts[0].split(',')]
    joltages.append(jolts)  # Agregar la lista de voltajes


def solve_joltage_file():
    """Función para resolver el problema de voltajes usando programación lineal"""
    ans = 0  # Respuesta acumulada
    # Procesar cada máquina
    for i, jolts in enumerate(joltages):
        buts = buttons[i]  # Obtener los botones de la máquina actual
        
        # Crear matriz A para el sistema de ecuaciones lineales
        # A[j][k] = 1 si el botón k afecta la luz j, 0 en caso contrario
        A = [[0 for i_ in range(len(buts))] for j in range(len(jolts))]
        for j, but in enumerate(buts):  # Para cada botón
            for light in but:           # Para cada luz que afecta
                A[light][j] = 1         # Marcar que el botón j afecta la luz

        # Vector de costos: cada botón tiene costo 1 (queremos minimizar presiones)
        c = [1 for i_ in range(len(buts))]
        # Resolver el problema de programación lineal entera
        # Minimizar c^T * x sujeto a A * x = jolts, x entero
        res = scipy.optimize.linprog(c, A_eq=A, b_eq=jolts, integrality=1)

        # Verificar si se encontró una solución
        if not res.success:
            print("No se pudo encontrar una solución óptima")
            return -1

        # Sumar el número total de presiones de botones
        ans += sum(res.x)
    return ans  # Devolver la respuesta total

# Medir el tiempo de ejecución
start = time.time()  # Tiempo de inicio

# Ejecutar la solución y mostrar el resultado
print(solve_joltage_file())

# Calcular y mostrar el tiempo transcurrido
end = time.time()
print(f"Tardó {(end - start) * 1000} ms")


# Ejecutar la solución alternativa si este archivo se ejecuta directamente
if __name__ == "__main__":
    result = solve_file("10.txt")  # Resolver usando el método de fuerza bruta
    print("Resultado total:", result)  # Mostrar el resultado
