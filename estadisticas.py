"""
Módulo estadisticas: operaciones sobre las estructuras de estudiantes.

Estructuras (desacopladas pero relacionadas por posición):
    cursos[j]      -> código del curso j (columna j de la matriz)
    documentos[i]  -> documento del estudiante i (fila i de la matriz)
    notas[i][j]    -> nota del estudiante i en el curso j
                      -1 = canceló el curso, -2 = no matriculado
"""

CANCELADO = -1
NO_MATRICULADO = -2


def buscar_estudiante(documentos, documento):
    """Retorna la posición del documento en la lista, o -1 si no existe."""
    for i in range(len(documentos)):
        if documentos[i] == documento:
            return i
    return -1


def eliminar_estudiante(documentos, notas, documento):
    """
    Elimina al estudiante y su fila de notas.
    Retorna True si se eliminó, False si no existía.
    """
    pos = buscar_estudiante(documentos, documento)
    if pos == -1:
        return False
    documentos.pop(pos)
    notas.pop(pos)
    return True


def mayor_nota(cursos, notas, pos):
    """
    Retorna (nota, codigo_curso) de la mayor nota del estudiante en la
    posición pos. Ignora cursos cancelados (-1) y no matriculados (-2).
    Si no tiene notas válidas, retorna (None, None).
    """
    fila = notas[pos]
    mejor_j = -1
    for j in range(len(fila)):
        if fila[j] >= 0 and (mejor_j == -1 or fila[j] > fila[mejor_j]):
            mejor_j = j
    if mejor_j == -1:
        return None, None
    return fila[mejor_j], cursos[mejor_j]


def resumen_estudiante(fila):
    """
    Recorre UNA sola vez la fila de notas y retorna (promedio, cantidad)
    considerando solo notas válidas (>= 0).
    """
    suma = 0
    cantidad = 0
    for nota in fila:
        if nota >= 0:
            suma += nota
            cantidad += 1
    promedio = suma / cantidad if cantidad > 0 else 0
    return promedio, cantidad


def calcular_resumenes(notas):
    """
    Calcula promedios y cantidad de cursos de todos los estudiantes
    en una sola pasada por la matriz. Retorna (promedios, cantidades).
    """
    promedios = []
    cantidades = []
    for fila in notas:
        promedio, cantidad = resumen_estudiante(fila)
        promedios.append(promedio)
        cantidades.append(cantidad)
    return promedios, cantidades


def ordenar_burbuja_desc(valores):
    """
    Ordenamiento BURBUJA por índices, de mayor a menor.
    No mueve los datos originales: ordena una lista de índices.
    Optimizaciones: el rango se reduce en cada pasada y se detiene
    si en una pasada no hubo intercambios.
    Retorna la lista de índices ordenada.
    """
    indices = list(range(len(valores)))
    n = len(indices)
    for pasada in range(n - 1):
        hubo_cambio = False
        for k in range(n - 1 - pasada):
            if valores[indices[k]] < valores[indices[k + 1]]:
                indices[k], indices[k + 1] = indices[k + 1], indices[k]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return indices


def ordenar_seleccion_desc(valores):
    """
    Ordenamiento por SELECCIÓN por índices, de mayor a menor.
    Retorna la lista de índices ordenada.
    """
    indices = list(range(len(valores)))
    n = len(indices)
    for i in range(n - 1):
        pos_max = i
        for k in range(i + 1, n):
            if valores[indices[k]] > valores[indices[pos_max]]:
                pos_max = k
        if pos_max != i:
            indices[i], indices[pos_max] = indices[pos_max], indices[i]
    return indices
