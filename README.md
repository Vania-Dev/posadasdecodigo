# Posadas de Código - Advent of Code 2024

¡Bienvenido al repositorio de **Posadas de Código**! 🎄✨

Este repositorio contiene las soluciones para los desafíos de programación del Advent of Code 2024, presentados por la comunidad de [Posadas de Código](https://posadasdecodigo.com).

## 📖 Acerca del Proyecto

**Posadas de Código** es una iniciativa que combina la tradición navideña mexicana de las posadas con la pasión por la programación. Durante el mes de diciembre, resolvemos juntos los desafíos diarios del Advent of Code, creando una comunidad de aprendizaje y colaboración.

### ¿Qué es Advent of Code?

Advent of Code es un calendario de adviento de pequeños desafíos de programación que se pueden resolver en cualquier lenguaje de programación. Los problemas varían en dificultad y cubren una amplia gama de temas de ciencias de la computación.

## 🗂️ Estructura del Repositorio

```
PosadasDeCodigo/
├── 01/                     # Día 1: Secret Entrance
│   ├── 01.py              # Solución en Python
│   ├── 01.txt             # Input del problema
│   ├── 01_test.txt        # Input de prueba
│   ├── Day 1: Part One.md # Descripción parte 1
│   └── Day 1: Part Two.md # Descripción parte 2
├── 02/                     # Día 2: ID Validation
│   ├── 02.py              # Solución en Python
│   ├── 02.txt             # Input del problema
│   ├── 02_test.txt        # Input de prueba
│   ├── Day 2: Part One.md # Descripción parte 1
│   └── Day 2: Part Two.md # Descripción parte 2
├── 03/                     # Día 3: Joltage Banks
│   ├── 03.py              # Solución en Python
│   ├── 03.txt             # Input del problema
│   ├── 03_test.txt        # Input de prueba
│   ├── Day 3: Part One.md # Descripción parte 1
│   └── Day 3: Part Two.md # Descripción parte 2
├── 04/                     # Día 4: Printing Department
│   ├── 04.py              # Solución en Python
│   ├── 04.txt             # Input del problema
│   ├── 04_test.txt        # Input de prueba
│   ├── Day 4: Part One.md # Descripción parte 1
│   └── Day 4: Part Two.md # Descripción parte 2
├── 05/                     # Día 5: Cafeteria
│   ├── 05.py              # Solución en Python
│   ├── 05.txt             # Input del problema
│   ├── 05_test.txt        # Input de prueba
│   ├── Day 5: Part One.md # Descripción parte 1
│   └── Day 5: Part Two.md # Descripción parte 2
├── 06/                     # Día 6: Trash Compactor
│   ├── 06.py              # Solución en Python
│   ├── 06.txt             # Input del problema
│   ├── 06_test.txt        # Input de prueba
│   ├── Day 6: Part One.md # Descripción parte 1
│   └── Day 6: Part Two.md # Descripción parte 2
├── 07/                     # Día 7: Laboratories
│   ├── 07.py              # Solución en Python
│   ├── 07.txt             # Input del problema
│   ├── 07_test.txt        # Input de prueba
│   ├── Day 7: Part One.md # Descripción parte 1
│   └── Day 7: Part Two.md # Descripción parte 2
├── 08/                     # Día 8: Playground
│   ├── 08.py              # Solución en Python
│   ├── 08.txt             # Input del problema
│   ├── 08_test.txt        # Input de prueba
│   ├── Day 8: Part One.md # Descripción parte 1
│   └── Day 8: Part Two.md # Descripción parte 2
└── README.md              # Este archivo
```

## 🚀 Cómo Ejecutar las Soluciones

### Prerrequisitos

- Python 3.6 o superior
- Los archivos de input correspondientes (incluidos en cada carpeta)

### Ejecución

1. Navega al directorio del día que quieres ejecutar:
   ```bash
   cd 01/  # Para el día 1
   ```

2. Ejecuta el script de Python:
   ```bash
   python 01.py
   ```

3. El programa mostrará los resultados para ambas partes del desafío.

## 📝 Resumen de Problemas

### Día 1: Secret Entrance 🔐
**Problema**: Descifrar la contraseña de una entrada secreta mediante rotaciones de un dial circular.

**Conceptos clave**:
- Aritmética modular
- Simulación de procesos
- Optimización de algoritmos

**Funciones principales**:
- `calculate_password_from_file()`: Solución básica que simula cada rotación
- `calculate_password_optimized()`: Solución optimizada que cuenta zeros durante las rotaciones

### Día 2: ID Validation 🆔
**Problema**: Identificar y sumar IDs inválidos basados en patrones específicos.

**Conceptos clave**:
- Análisis de patrones en strings
- Validación de datos
- Algoritmos de detección de repeticiones

**Funciones principales**:
- `is_invalid()`: Detecta IDs con mitades idénticas
- `is_invalid_pattern()`: Detecta IDs con patrones repetitivos más complejos

### Día 3: Joltage Banks ⚡
**Problema**: Maximizar el voltaje de salida de bancos de energía mediante selección óptima de dígitos.

**Conceptos clave**:
- Algoritmos greedy
- Subsecuencias óptimas
- Optimización combinatoria

**Funciones principales**:
- `max_joltage_for_bank()`: Encuentra el máximo voltaje con dos dígitos
- `best_joltage_subsequence()`: Algoritmo greedy para encontrar la mejor subsecuencia

### Día 4: Printing Department 📄
**Problema**: Optimizar el acceso de montacargas a rollos de papel en una grilla, eliminando rollos accesibles iterativamente.

**Conceptos clave**:
- Navegación en grillas 2D
- Algoritmos de vecindad (8 direcciones)
- Simulación iterativa
- Procesamiento de archivos

**Funciones principales**:
- `is_accessible()`: Verifica si un rollo tiene menos de 4 vecinos
- `count_accessible_rolls()`: Cuenta rollos accesibles iniciales
- `total_removable_rolls()`: Simula eliminación iterativa hasta completar

### Día 5: Cafeteria 🍽️
**Problema**: Determinar qué ingredientes están frescos basándose en rangos de IDs y fusionar rangos superpuestos para contar IDs únicos.

**Conceptos clave**:
- Procesamiento de rangos numéricos
- Fusión de intervalos superpuestos
- Validación de datos contra rangos
- Algoritmos de ordenamiento

**Funciones principales**:
- `parse_input()`: Separa rangos frescos e IDs disponibles del archivo
- `is_fresh()`: Verifica si un ID está dentro de algún rango fresco
- `merge_ranges()`: Fusiona rangos superpuestos en una lista consolidada
- `count_total_fresh_ids()`: Cuenta IDs únicos en rangos fusionados

### Día 6: Trash Compactor 🗑️
**Problema**: Resolver hojas de trabajo de matemáticas de cefalópodos donde los problemas están dispuestos horizontalmente con números verticales.

**Conceptos clave**:
- Transposición de matrices
- Procesamiento de grillas 2D
- Separación de bloques por columnas vacías
- Lectura bidireccional (izquierda-derecha y derecha-izquierda)

**Funciones principales**:
- `read_matrix()`: Lee el archivo preservando espacios
- `transpose()`: Convierte filas en columnas para facilitar el procesamiento
- `separate_blocks()`: Agrupa columnas en problemas individuales
- `process_block()`: Extrae números y operador, calcula el resultado
- `solve_worksheet()`: Resuelve todos los problemas y suma los resultados
- `solve_cephalopod_file()`: Versión alternativa que lee de derecha a izquierda

### Día 7: Laboratories 🔬
**Problema**: Simular el comportamiento de rayos de taquiones que se dividen al encontrar divisores en un manifold.

**Conceptos clave**:
- Búsqueda en anchura (BFS) con cola
- Simulación de propagación de rayos
- Conteo de divisiones y timelines
- Interpretación many-worlds (múltiples universos)

**Funciones principales**:
- `count_splits_from_file()`: Cuenta cuántas veces se divide el rayo (Parte 1)
- `count_timelines_from_file()`: Cuenta timelines finales bajo interpretación many-worlds (Parte 2)

### Día 8: Playground 🎮
**Problema**: Conectar cajas de conexión eléctricas en espacio 3D usando el algoritmo de Kruskal para encontrar componentes conectados.

**Conceptos clave**:
- Disjoint Set Union (Union-Find)
- Algoritmo de Kruskal para MST
- Distancia euclidiana en 3D
- Componentes conectados en grafos

**Funciones principales**:
- `DSU`: Clase para estructura Union-Find con compresión de ruta
- `read_points()`: Lee coordenadas 3D desde archivo
- `solve()`: Conecta K pares más cercanos y calcula producto de 3 grupos mayores
- `solve_part2()`: Encuentra la primera conexión que une todos los puntos

### Día 9: Rectangle Selection 🟩
**Problema**: Encontrar el rectángulo más grande usando solo tiles rojos y verdes, donde los rojos forman un loop conectado por verdes.

**Conceptos clave**:
- Flood fill (BFS)
- Suma de prefijos 2D
- Detección de regiones interiores/exteriores
- Optimización de consultas de rectángulos

**Funciones principales**:
- `part2_opt()`: Encuentra el área máxima de rectángulos válidos usando suma de prefijos 2D para verificación O(1)

## 🛠️ Características del Código

### Estilo y Convenciones

- **Nombres en inglés**: Todas las variables y funciones están nombradas en inglés para seguir las mejores prácticas de programación
- **Comentarios en español**: Los comentarios están en español para facilitar la comprensión de la comunidad hispanohablante
- **Código limpio**: Implementaciones concisas y eficientes
- **Documentación**: Cada función incluye docstrings explicativos

### Optimizaciones Implementadas

- **Día 1**: Algoritmo matemático para contar zeros sin simular cada paso
- **Día 2**: Detección eficiente de patrones repetitivos
- **Día 3**: Algoritmo greedy con stack para subsecuencias óptimas
- **Día 4**: Comentarios detallados en español para facilitar el aprendizaje
- **Día 5**: Fusión eficiente de rangos y nomenclatura en inglés con comentarios en español
- **Día 6**: Transposición de matrices y procesamiento bidireccional
- **Día 7**: BFS eficiente con propagación de contadores para timelines
- **Día 8**: Union-Find optimizado con compresión de ruta y unión por tamaño
- **Día 9**: Suma de prefijos 2D para verificación de rectángulos en O(1)

## 🎯 Objetivos de Aprendizaje

Este repositorio está diseñado para:

1. **Practicar algoritmos**: Cada problema presenta desafíos algorítmicos únicos
2. **Mejorar el código**: Implementaciones limpias y eficientes
3. **Aprender optimización**: Comparación entre soluciones básicas y optimizadas
4. **Fomentar la comunidad**: Código comentado y documentado para facilitar el aprendizaje colaborativo

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes:

- Optimizaciones adicionales
- Soluciones alternativas
- Mejoras en la documentación
- Correcciones de bugs

No dudes en crear un pull request o abrir un issue.

## 📚 Recursos Adicionales

- [Advent of Code 2025](https://adventofcode.com/2025)
- [Posadas de Código](https://posadasdecodigo.com)
- [Documentación de Python](https://docs.python.org/3/)

## 📊 Progreso

- ✅ Día 1: Secret Entrance
- ✅ Día 2: ID Validation
- ✅ Día 3: Joltage Banks
- ✅ Día 4: Printing Department
- ✅ Día 5: Cafeteria
- ✅ Día 6: Trash Compactor
- ✅ Día 7: Laboratories
- ✅ Día 8: Playground
- ✅ Día 9: Rectangle Selection

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

**¡Felices fiestas y feliz programación!** 🎄🐍

*Hazlo con el tipo de ❤️ que deja huellas en el alma*