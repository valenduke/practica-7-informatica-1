"""
Módulo archivos: lectura de los archivos CSV del programa.
"""


def cargar_notas(ruta):
    """
    Lee el archivo de notas y construye las estructuras del programa.

    Formato esperado:
        línea 1: códigos de los cursos
        línea 2: documentos de los estudiantes
        líneas siguientes: una fila de notas por estudiante

    Retorna una tupla (cursos, documentos, notas):
        cursos     -> lista de str
        documentos -> lista de str
        notas      -> matriz (lista de listas de float), notas[i][j]
    """
    cursos = []
    documentos = []
    notas = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip() != ""]

    cursos = [c.strip() for c in lineas[0].split(",")]
    documentos = [d.strip() for d in lineas[1].split(",")]
    for linea in lineas[2:]:
        fila = [float(valor) for valor in linea.split(",")]
        notas.append(fila)
    return cursos, documentos, notas


def cargar_historico(ruta):
    """
    Lee el archivo de matriculados históricos y lo carga en dos listas.
    Se asume una fila por año con el formato: año,matriculados
    Si la primera línea es un encabezado (no numérico), se ignora.

    Retorna (anios, matriculados), ambas listas de números.
    """
    anios = []
    matriculados = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) < 2:
                continue
            try:
                anio = int(partes[0])
                cantidad = float(partes[1])
            except ValueError:
                continue  # encabezado o línea inválida
            anios.append(anio)
            matriculados.append(cantidad)
    return anios, matriculados
