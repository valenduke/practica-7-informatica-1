"""
Práctica 7 - Informática I
Ordenamiento, búsqueda y predicción.

Programa principal: muestra el menú y llama a los módulos.
"""

import archivos
import estadisticas
import prediccion
import plots

RUTA_NOTAS = "notas_estudiantes.csv"
RUTA_HISTORICO = "hist_matriculados.csv"
ARCHIVO_GRAFICA = "prediccion.png"


def mostrar_menu():
    print("\n MENÚ PRINCIPAL ")
    print("1. Cargar datos desde archivo")
    print("2. Eliminar estudiante")
    print("3. Mayor nota de estudiante")
    print("4. Ordenar promedios estudiantes (burbuja)")
    print("5. Ordenar estudiantes por cantidad de cursos (selección)")
    print("6. Predecir estudiantes matriculados")
    print("0. Salir")


def opcion_predecir():
    """
    Pide un año futuro, estima los matriculados con la regresión lineal,
    muestra el error (MAE) y genera la gráfica en 'prediccion.png'.
    """
    anios, matriculados = archivos.cargar_historico(RUTA_HISTORICO)
    anio = int(input("Año a predecir: "))
    a, b = prediccion.A, prediccion.B

    estimados = prediccion.calcular_y(anios, a, b)
    error = prediccion.calcular_mae(matriculados, estimados)
    estimado = prediccion.predecir(anio, a, b)

    print(f"Matriculados estimados para {anio}: {estimado:.0f}")
    print(f"Error del modelo (MAE): {error:.2f}")

    # Datos en el formato que pide plot_data(): [[año, estudiantes], ...]
    data = [[anios[i], matriculados[i]] for i in range(len(anios))]
    # La recta se extiende desde el primer año hasta el año pedido
    years = list(range(anios[0], max(anio, anios[-1]) + 1))
    regression_line = prediccion.calcular_y(years, a, b)

    # plot_data() termina con plt.show(). Para agregar el punto estimado y
    # guardar el archivo sin modificar plots.py, se reemplaza plt.show
    # temporalmente por una función que hace eso antes de mostrar.
    show_original = plots.plt.show

    def agregar_punto_y_guardar():
        plots.plt.plot(anio, estimado, "g*", markersize=15,
                       label=f"Estimado {anio}: {estimado:.0f}")
        plots.plt.legend()
        plots.plt.savefig(ARCHIVO_GRAFICA)
        print(f"Gráfica guardada en {ARCHIVO_GRAFICA}")
        show_original()

    plots.plt.show = agregar_punto_y_guardar
    try:
        plots.plot_data(data, regression_line, years)
    finally:
        plots.plt.show = show_original


def main():
    cursos, documentos, notas = [], [], []
    cargados = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Hasta luego.")
            break

        if opcion in ("2", "3", "4", "5") and not cargados:
            print("Primero cargue los datos (opción 1).")
            continue

        if opcion == "1":
            cursos, documentos, notas = archivos.cargar_notas(RUTA_NOTAS)
            cargados = True
            print(f"Datos cargados: {len(documentos)} estudiantes, {len(cursos)} cursos.")

        elif opcion == "2":
            doc = input("Documento del estudiante: ").strip()
            if estadisticas.eliminar_estudiante(documentos, notas, doc):
                print("Estudiante eliminado.")
            else:
                print("No existe un estudiante con ese documento.")

        elif opcion == "3":
            doc = input("Documento del estudiante: ").strip()
            pos = estadisticas.buscar_estudiante(documentos, doc)
            if pos == -1:
                print("No existe un estudiante con ese documento.")
            else:
                nota, curso = estadisticas.mayor_nota(cursos, notas, pos)
                if nota is None:
                    print("El estudiante no tiene notas válidas.")
                else:
                    print(f"Mayor nota: {nota} en el curso {curso}")

        elif opcion == "4":
            promedios, _ = estadisticas.calcular_resumenes(notas)
            orden = estadisticas.ordenar_burbuja_desc(promedios)
            print("\nEstudiantes por promedio (mayor a menor):")
            for i in orden:
                print(f"  {documentos[i]}: {promedios[i]:.2f}")

        elif opcion == "5":
            _, cantidades = estadisticas.calcular_resumenes(notas)
            orden = estadisticas.ordenar_seleccion_desc(cantidades)
            print("\nEstudiantes por cantidad de cursos (mayor a menor):")
            for i in orden:
                print(f"  {documentos[i]}: {cantidades[i]} cursos")

        elif opcion == "6":
            opcion_predecir()

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
