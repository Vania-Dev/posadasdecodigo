import re
from datetime import datetime

# Día 12: Christmas Tree Farm
# Problema: Determinar si los regalos con formas específicas caben en regiones bajo árboles de Navidad
# Enfoque: Verificación simplificada por área total (no considera la geometría real de colocación)

input_text = open('12.txt').read().strip()

current_datetime = datetime.now()
answerp1 = 0  # Contador de regiones donde caben todos los regalos
closest_call = float('inf')  # Menor área restante encontrada
total_area_of_closest_call = None  # Área total de la región con menor espacio restante
lines = input_text.split('\n')

# Calcular el área (número de '#') de cada forma de regalo
# Las formas están en las líneas 1-3, 6-8, 11-13, 16-18, 21-23, 26-28
# Cada forma ocupa 3 líneas seguidas de una línea vacía
sizes = [
    sum(line.count('#') for line in lines[start:start+3])  # Contar '#' en las 3 líneas de cada forma
    for start in range(1, 27, 5)  # Empezar en línea 1, luego 6, 11, 16, 21, 26 (saltos de 5)
]

# Procesar cada región (líneas después de la 30)
for line in lines[30:]:
    # Parsear línea: "12x5: 1 0 1 0 2 2" -> [12, 5, 1, 0, 1, 0, 2, 2]
    arr = list(map(int, re.split(r'x|: | ', line)))
    
    # Calcular área total de la región
    total_area = arr[0] * arr[1]  # ancho × alto
    
    # Calcular área total ocupada por todos los regalos requeridos
    # arr[i+2] = cantidad de regalos de forma i
    # sizes[i] = área de la forma i
    combined_shapes_area = sum(arr[i+2] * sizes[i] for i in range(6))
    
    # Verificar si hay suficiente espacio
    remaining_area = total_area - combined_shapes_area
    
    if remaining_area >= 0:  # Si el área total es suficiente
        answerp1 += 1
        
        # Rastrear la región con menor espacio restante (más ajustada)
        if remaining_area < closest_call:
            closest_call = remaining_area
            total_area_of_closest_call = total_area

print(f'Answer part 1: {answerp1}')
print(f'The closest call was: {closest_call} remaining area on a total area of: {total_area_of_closest_call}')
print(f'Solved in: {datetime.now() - current_datetime}')