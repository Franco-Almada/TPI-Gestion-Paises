import csv  # importa csv para leer y escribir archivos csv

# Funcion para cargar los países desde un archivo csv
def cargar_paises_desde_csv(nombre_archivo):
    paises = []  # Lista donde se almacenan los países

    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:

            lector = csv.DictReader(archivo)

            # Recorre todas las filas del archivo
            for fila in lector:
                try:
                    # Limpia los datos de cada campo
                    nombre = fila['nombre'].strip().lower()
                    poblacion = int(fila['poblacion'])
                    superficie = int(fila['superficie'])
                    continente = fila['continente'].strip()

                    # Si el nombre o continente estan vacios ignora el registro
                    if nombre == '' or continente == '':
                        continue

                    # Se crea el diccionario con los datos del país
                    pais = {
                        'nombre': nombre,
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': continente
                    }

                    # Verifica que el país no exista previamente en la lista
                    if not any(p['nombre'] == nombre for p in paises):
                        paises.append(pais)

                except (ValueError, KeyError):
                    print(f"Advertencia: Línea inválida o mal formateada: {fila}")
    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se iniciará con lista vacía.")

    # Devuelve la lista de países cargados
    return paises

# Funcion para guardar la lista de países en un archivo csv
def guardar_paises_en_csv(nombre_archivo, lista_paises):

    # Abre el archivo en modo escritura
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:

        # Define las columnas del archivo
        campos = ['nombre', 'poblacion', 'superficie', 'continente']

        # Crea el escritor del archivo
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        # Escribe cada país en una fila
        for pais in lista_paises:
            escritor.writerow(pais)

# Funcion para agregar un pais nuevo
def agregar_pais(lista):
    nombre = input("Ingrese nombre del país: ").strip().lower()

    # Se verifica que el nombre no este vacío
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    # Se verifica que el pais no exista
    if any(p['nombre'] == nombre for p in lista):
        print("El país ya existe en la lista.")
        return

    # Se pide el continente
    continente = input("Ingrese continente: ").strip()

    if not continente:
        print("El continente no puede estar vacío.")
        return

    try:
        # Solicita poblacion y superficie
        poblacion = int(input("Ingrese población: "))
        superficie = int(input("Ingrese superficie (km²): "))

    except ValueError:
        print("Población y superficie deben ser números enteros válidos.")
        return

    # Crea el nuevo pais
    pais = {'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente}

    # Lo añade a la lista
    lista.append(pais)

    print(f"País {nombre.capitalize()} agregado exitosamente.")

# Funcion para actualizar un pais que ya existe
def actualizar_pais(lista):

    # Solicita el nombre del país
    nombre = input("Ingrese nombre del país a actualizar: ").strip().lower()

    # Busca el país en la lista
    pais_encontrado = next((p for p in lista if p['nombre'] == nombre), None)

    # Si no existe finaliza la función
    if not pais_encontrado:
        print("País no encontrado.")
        return

    try:
        # Solicita los nuevos datos
        poblacion = int(input("Nueva población: "))
        superficie = int(input("Nueva superficie: "))

    except ValueError:
        print("Población y superficie deben ser números enteros válidos.")
        return

    # Actualiza los valores
    pais_encontrado['poblacion'] = poblacion
    pais_encontrado['superficie'] = superficie

    print(f"Datos de {nombre.capitalize()} actualizados correctamente.")

# Funcion para buscar países
def buscar_pais(lista):
    busqueda = input("Ingrese nombre o parte del nombre para buscar: ").strip().lower()

    # Busca coincidencias parciales
    resultados = [p for p in lista if busqueda in p['nombre']]

    # Si existen resultados, los muestra
    if resultados:

        print(f"Se encontraron {len(resultados)} resultados:")

        for p in resultados:

            print(f"{p['nombre'].capitalize()} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")

    else:

        print("No se encontraron países que coincidan con la búsqueda.")

# Funcion para filtrar por continente
def filtrar_por_continente(lista):
    continente = input("Ingrese el continente para filtrar: ").strip().lower()

    filtrados = [p for p in lista if p['continente'].lower() == continente]
    if filtrados:
        mostrar_paises(filtrados)
    else:
        print("No se encontraron países en ese continente.")

# Funcion para filtrar por población
def filtrar_por_poblacion(lista):
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
    except ValueError:
        print("Valores inválidos. Deben ser números enteros.")
        return
    filtrados = [p for p in lista if minimo <= p['poblacion'] <= maximo]
    if filtrados:
        mostrar_paises(filtrados)
    else:
        print("No se encontraron países en el rango de población indicado.")

# Funcion para filtrar por superficie
def filtrar_por_superficie(lista):
    try:
        minimo = int(input("Superficie mínima (km²): "))
        maximo = int(input("Superficie máxima (km²): "))
    except ValueError:
        print("Valores inválidos. Deben ser números enteros.")
        return
    filtrados = [p for p in lista if minimo <= p['superficie'] <= maximo]
    if filtrados:
        mostrar_paises(filtrados)
    else:
        print("No se encontraron países en el rango de superficie indicado.")

# Funcion para mostrar países
def mostrar_paises(lista):
    for p in lista:
        print(f"{p['nombre'].capitalize()} - Población: {p['poblacion']} - Superficie: {p['superficie']} km² - Continente: {p['continente']}")

# Funcion para ordenar los países
def ordenar_paises(lista):
    print("Ordenar por: 1-Nombre 2-Población 3-Superficie")
    opcion = input("Seleccione opción: ")
    if opcion not in ['1', '2', '3']:
        print("Opción inválida.")
        return
    
    # Se elige como ordenar
    campo = {'1': 'nombre', '2': 'poblacion', '3': 'superficie'}[opcion]

    # Se solicita el tipo de orden
    orden = input("Orden ascendente (A) o descendente (D)? ").strip().upper()
    reverse = True if orden == 'D' else False
    lista_ordenada = sorted(lista, key=lambda x: x[campo], reverse=reverse)

    # Muestra la lista ordenada
    mostrar_paises(lista_ordenada)

# Funcion para mostrar estadísticas
def mostrar_estadisticas(lista):
    # Verifica que existan datos
    if not lista:
        print("No hay datos para mostrar estadísticas.")
        return

    # Obtiene el país con mayor población
    max_pob = max(lista, key=lambda x: x['poblacion'])

    # Obtiene el país con menor población
    min_pob = min(lista, key=lambda x: x['poblacion'])

    # Calcula el promedio de población
    promedio_pob = sum(p['poblacion'] for p in lista) / len(lista)

    # Calcula el promedio de superficie
    promedio_sup = sum(p['superficie'] for p in lista) / len(lista)


    # Diccionario para contar países por continente
    continentes = {}
    for p in lista:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    # Muestra las estadísticas
    print(f"País con mayor población: {max_pob['nombre'].capitalize()} ({max_pob['poblacion']})")
    print(f"País con menor población: {min_pob['nombre'].capitalize()} ({min_pob['poblacion']})")
    print(f"Promedio de población: {promedio_pob:.2f}")
    print(f"Promedio de superficie: {promedio_sup:.2f} km²")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")

    # Pregunta si desea exportar las estadísticas
    exportar = input("¿Desea exportar estas estadísticas a CSV? (S/N): ").strip().lower()
    if exportar == 's':
        nombre_archivo = 'estadisticas_paises.csv'
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['Indicador', 'Valor']
            escritor = csv.writer(archivo)
            escritor.writerow(campos)
            escritor.writerow(['País con mayor población', f"{max_pob['nombre'].capitalize()} ({max_pob['poblacion']})"])
            escritor.writerow(['País con menor población', f"{min_pob['nombre'].capitalize()} ({min_pob['poblacion']})"])
            escritor.writerow(['Promedio de población', f"{promedio_pob:.2f}"])
            escritor.writerow(['Promedio de superficie', f"{promedio_sup:.2f} km²"])
            escritor.writerow([])
            escritor.writerow(['Continente', 'Cantidad de países'])
            for cont, cant in continentes.items():
                escritor.writerow([cont, cant])
        print(f"Estadísticas exportadas a {nombre_archivo}")

# Funcion principal que muestra el menú
def menu():
    nombre_archivo = 'paises.csv'

    # Carga los datos al iniciar el programa
    paises = cargar_paises_desde_csv(nombre_archivo)

    while True:
        # Muestra el menú principal
        print("\n--- Menú Gestión de Países ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Guardar y salir")

        opcion = input("Seleccione opción: ")

        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            actualizar_pais(paises)
        elif opcion == '3':
            buscar_pais(paises)
        elif opcion == '4':
            print("Filtros: a) Continente b) Población c) Superficie")
            filtro = input("Seleccione filtro: ").strip().lower()
            if filtro == 'a':
                filtrar_por_continente(paises)
            elif filtro == 'b':
                filtrar_por_poblacion(paises)
            elif filtro == 'c':
                filtrar_por_superficie(paises)
            else:
                print("Filtro inválido.")
        elif opcion == '5':
            ordenar_paises(paises)
        elif opcion == '6':
            mostrar_estadisticas(paises)
        elif opcion == '7':
            # Guarda los datos antes de salir
            guardar_paises_en_csv(nombre_archivo, paises)
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":

    menu()
