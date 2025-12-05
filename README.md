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

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

**¡Felices fiestas y feliz programación!** 🎄🐍

*Hazlo con el tipo de ❤️ que deja huellas en el alma*