# Práctica 7 – Informática I (UdeA)

Ordenamiento, búsqueda y predicción en Python.

## Cómo ejecutar
```
python main.py
```
Requiere en la misma carpeta: `plots.py`, `notas_estudiantes.csv` y `hist_matriculados.csv`.

## Módulos
- `archivos.py`: lectura de los CSV.
- `estadisticas.py`: búsqueda, eliminación, mayor nota, promedios, burbuja y selección (por índices).
- `prediccion.py`: regresión lineal y = ax + b y MAE.
- `main.py`: menú principal.

## Tanteo de a y b
Modelo: y = a·x + b, donde x es el año y y los estudiantes matriculados.

| Intento | a | b | MAE |
|---|---|---|---|
| 1 | 1.0 | -1950 | 10.37 |
| 2 | 1.5 | -2960 | 10.45 |
| 3 | 1.8 | -3555 | 4.97 |
| 4 | 2.0 | -3950 | 3.95 |
| 5 | 1.95 | -3853 | 3.72 |
| 6 | **2.0** | **-3952** | **3.63** |

Valores finales: a = 2.0, b = -3952 (MAE ≈ 3.63).

## Dependencias
```
pip install numpy matplotlib
```
