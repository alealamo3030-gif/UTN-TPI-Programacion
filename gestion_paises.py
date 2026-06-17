import csv

# ============================================
# GESTIÓN DE DATOS DE PAÍSES EN PYTHON
# TPI - Programación 1 - UTN TUP 2026
# Alumnos: Peralta - Alamo
# ============================================

# Ruta del archivo CSV donde se almacenan los datos de los países
ruta_archivo = 'paises.csv'

# --- LECTURA Y ESCRITURA DEL CSV ---

def cargar_paises():
    # Inicializamos la lista vacía que va a contener los países
    paises = []
    try:
        # Abrimos el archivo en modo lectura con codificación UTF-8
        # para soportar caracteres especiales como tildes y eñes
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:

            # DictReader lee cada fila como un diccionario
            # usando la primera línea del CSV como encabezados (claves)
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    # Construimos el diccionario de cada país
                    # strip() elimina espacios al inicio y al final
                    # title() capitaliza la primera letra de cada palabra
                    # int() convierte el string a número entero
                    pais = {
                        'nombre':     fila['nombre'].strip().title(),
                        'poblacion':  int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip().title()
                    }
                    paises.append(pais)

                except ValueError:
                    # Si población o superficie no son números, avisamos y saltamos esa fila
                    print(f'ERROR: Fila con formato invalido ignorada: {fila}')

    except FileNotFoundError:
        # El archivo CSV no existe en la carpeta indicada
        print(f"ERROR: El archivo '{ruta_archivo}' no se encontro en la carpeta.")

    except KeyError:
        # El CSV existe pero le falta alguna columna esperada
        print('ERROR: El CSV no tiene una clave de una columna. Verifique los encabezados')

    except Exception as e:
        # Capturamos cualquier otro error inesperado y mostramos el detalle
        print(f'Ocurrio un error inesperado: {e}')

    return paises


def guardar_archivo_paises(paises):
    # Definimos el orden de las columnas que va a tener el CSV
    columnas = ['nombre', 'poblacion', 'superficie', 'continente']

    # Abrimos el archivo en modo escritura
    # newline='' evita que se agreguen líneas vacías entre cada fila en Windows
    with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo:

        # DictWriter escribe diccionarios como filas del CSV
        escritor = csv.DictWriter(archivo, fieldnames=columnas)

        # writeheader() escribe la primera fila con los nombres de las columnas
        escritor.writeheader()

        # writerows() escribe toda la lista de diccionarios de una sola vez
        escritor.writerows(paises)


# --- MOSTRAR PAÍSES ---
# Estas funciones se reutilizan en varias opciones del menú

def mostrar_pais(pais):
    # Muestra los datos de un único país con formato legible
    # :, agrega separador de miles en los números (ej: 1,000,000)
    print(f"  Nombre:     {pais['nombre']}")
    print(f"  Poblacion:  {pais['poblacion']:,} habitantes")
    print(f"  Superficie: {pais['superficie']:,} km2")
    print(f"  Continente: {pais['continente']}")
    print()


def mostrar_lista(paises):
    # Muestra una lista completa de países numerada
    # Si la lista está vacía informamos y salimos sin error
    if len(paises) == 0:
        print('\nNo se encontraron paises.')
        return

    print(f'\nSe encontraron {len(paises)} pais/es:\n')
    for i in range(len(paises)):
        print(f'--- Pais {i + 1} ---')
        mostrar_pais(paises[i])


# --- OPCION 1: AGREGAR PAÍS ---

def agregar_pais(paises):
    print('\n--- AGREGAR PAÍS ---')
    try:
        # Pedimos el nombre y lo normalizamos con strip() y title()
        nombre = input('Ingrese el nombre del pais: ').strip().title()

        # isalpha() verifica que solo tenga letras (reemplazamos espacios antes
        # para que nombres como "Nueva Zelanda" pasen la validación)
        if not nombre.replace(" ", "").isalpha() or nombre == '':
            print('\nERROR: El nombre no puede estar vacio ni contener numeros.')
            return

        # Verificamos que el país no esté ya cargado en la lista
        for p in paises:
            if p['nombre'] == nombre:
                print('ERROR: El pais ya se encuentra en la lista')
                return

        continente = input('Ingrese el continente del pais: ').strip().title()

        # Misma validación que para el nombre
        if not continente.replace(" ", "").isalpha() or continente == '':
            print('\nERROR: El continente no puede estar vacio ni contener numeros.')
            return

        poblacion = int(input('Ingrese poblacion del pais: '))

        # La población puede ser 0 (país deshabitado) pero no negativa
        if poblacion < 0:
            print('\nERROR: La poblacion no puede ser menor que 0.')
            return

        superficie = int(input('Ingrese la superficie del pais en km2: '))

        # La superficie siempre debe ser mayor a 0
        if superficie <= 0:
            print('\nERROR: La superficie no puede ser menor o igual a 0.')
            return

        # Armamos el diccionario del nuevo país con los datos validados
        nuevo = {
            'nombre':     nombre,
            'poblacion':  poblacion,
            'superficie': superficie,
            'continente': continente
        }

        # Agregamos el país a la lista en memoria y guardamos en el CSV
        paises.append(nuevo)
        guardar_archivo_paises(paises)
        print(f'Los datos del pais {nombre} fueron cargados correctamente.')

    except ValueError:
        # Si el usuario ingresa texto donde se esperaba un número entero
        print('\nERROR: El valor ingresado debe ser un numero entero.')


# --- OPCION 2: ACTUALIZAR PAIS ---

def actualizar_pais(paises):
    print('\n--- ACTUALIZAR PAÍS ---')

    # Normalizamos el nombre ingresado para que coincida con el formato guardado
    nombre = input('Ingrese el nombre exacto del pais a actualizar: ').strip().title()

    encontrado = False
    for i in range(len(paises)):
        if paises[i]['nombre'] == nombre:
            encontrado = True

            # Mostramos los valores actuales antes de pedir los nuevos
            print(f'\nPais encontrado: {paises[i]["nombre"]}')
            print(f'Poblacion actual: {paises[i]["poblacion"]:,}')
            print(f'Superficie actual: {paises[i]["superficie"]:,}')

            try:
                # Si el usuario presiona Enter sin escribir nada, el or mantiene
                # el valor actual del campo (no lo modifica)
                nueva_pob = int(input('\nNueva poblacion (Enter para no modificar): ') or paises[i]['poblacion'])
                nueva_sup = int(input('Nueva superficie en km2 (Enter para no modificar): ') or paises[i]['superficie'])

                # Validamos que los nuevos valores sean coherentes
                if nueva_pob < 0 or nueva_sup <= 0:
                    print('ERROR: Los valores deben ser enteros positivos.')
                    return

                # Actualizamos los valores en la lista y guardamos en el CSV
                paises[i]['poblacion'] = nueva_pob
                paises[i]['superficie'] = nueva_sup
                guardar_archivo_paises(paises)
                print(f'\nPais "{paises[i]["nombre"]}" actualizado correctamente.')

            except ValueError:
                print('ERROR: Debe ingresar un numero entero valido.')
            break

    if not encontrado:
        print(f'\nNo se encontro ningun pais con el nombre "{nombre}".')


# --- OPCION 3: BUSCAR PAÍS ---

def buscar_pais(paises):
    print('\n--- BUSCAR PAÍS ---')

    # Convertimos a minúsculas para que la búsqueda no distinga mayúsculas
    termino = input('Ingrese nombre o parte del nombre: ').strip().lower()

    if termino == '':
        print('ERROR: Debe ingresar un termino de busqueda.')
        return

    # Recorremos todos los países buscando coincidencias parciales
    # convirtiendo también el nombre del país a minúsculas para comparar
    resultados = []
    for p in paises:
        if termino in p['nombre'].lower():
            resultados.append(p)

    mostrar_lista(resultados)


# --- OPCION 4: FILTRAR PAISES ---

def filtrar_por_continente(paises):
    print('\n--- FILTRAR POR CONTINENTE ---')

    # title() garantiza que la comparación sea consistente con cómo están guardados
    continente = input('\nIngrese el continente: ').strip().title()

    if continente == '':
        print('\nERROR: El continente a buscar no puede estar vacio')
        return

    # Buscamos todos los países cuyo continente coincida exactamente
    resultados = []
    for p in paises:
        if p['continente'] == continente:
            resultados.append(p)

    mostrar_lista(resultados)


def filtrar_por_poblacion(paises):
    print('\n--- FILTRAR POR POBLACION ---')
    try:
        poblacion_min = int(input('\nIngrese el minimo de poblacion: '))
        poblacion_max = int(input('\nIngrese el maximo de poblacion: '))

        # Validamos que el rango sea coherente
        if poblacion_min > poblacion_max:
            print('\nERROR: El minimo no puede ser mayor al maximo.')
            return

        # Usamos >= y <= para incluir los valores exactos del rango
        resultados = []
        for p in paises:
            if p['poblacion'] >= poblacion_min and p['poblacion'] <= poblacion_max:
                resultados.append(p)

        mostrar_lista(resultados)

    except ValueError:
        print('\nERROR: La poblacion debe ser un numero entero.')


def filtrar_por_superficie(paises):
    print('\n--- FILTRAR POR SUPERFICIE ---')
    try:
        superficie_min = int(input('\nIngrese el minimo de superficie en km2: '))
        superficie_max = int(input('\nIngrese el maximo de superficie en km2: '))

        # Validamos que el rango sea coherente
        if superficie_min > superficie_max:
            print('\nERROR: El minimo no puede ser mayor al maximo.')
            return

        # Usamos >= y <= para incluir los valores exactos del rango
        resultados = []
        for p in paises:
            if p['superficie'] >= superficie_min and p['superficie'] <= superficie_max:
                resultados.append(p)

        mostrar_lista(resultados)

    except ValueError:
        print('\nERROR: La superficie debe ser un numero entero.')


def menu_filtros(paises):
    # Submenú que deriva al filtro correspondiente según la opción elegida
    print('''
--- FILTROS ---
1. Por continente
2. Por rango de poblacion
3. Por rango de superficie
4. Salir
''')
    opcion = input('Ingrese opcion a filtrar: ').strip()

    if opcion == '1':   filtrar_por_continente(paises)
    elif opcion == '2': filtrar_por_poblacion(paises)
    elif opcion == '3': filtrar_por_superficie(paises)
    elif opcion == '4': return
    else:
        print('ERROR: Opcion invalida')


# --- OPCION 5: ORDENAR PAISES ---

def ordenar_lista(copia, clave, orden=True):
    # Ordenamiento Bubble Sort para lista de diccionarios
    # Bubble Sort compara pares de elementos adyacentes e intercambia
    # los que estén en el orden incorrecto, repitiendo hasta ordenar todo
    n = len(copia)

    for i in range(n):
        # Cada pasada del bucle externo coloca el elemento más grande
        # (o más pequeño) en su posición final al final de la lista
        for j in range(0, n - i - 1):

            # Obtenemos los valores a comparar accediendo por la clave del diccionario
            valor_actual    = copia[j][clave]
            valor_siguiente = copia[j + 1][clave]

            if orden:
                # Orden ascendente: si el actual es mayor al siguiente, los intercambiamos
                if valor_actual > valor_siguiente:
                    copia[j], copia[j + 1] = copia[j + 1], copia[j]
            else:
                # Orden descendente: si el actual es menor al siguiente, los intercambiamos
                if valor_actual < valor_siguiente:
                    copia[j], copia[j + 1] = copia[j + 1], copia[j]

    return copia


def menu_ordenar(paises):
    print('''
--- ORDENAR ---
1. Por nombre A-Z
2. Por nombre Z-A
3. Por poblacion ascendente
4. Por poblacion descendente
5. Por superficie ascendente
6. Por superficie descendente
7. Salir
''')
    opcion = input('Ingrese opcion: ').strip()

    # Hacemos una copia de la lista para no modificar el orden original
    # list() crea una nueva lista independiente con los mismos elementos
    copia = list(paises)

    if opcion == '1':   ordenar_lista(copia, 'nombre', True)
    elif opcion == '2': ordenar_lista(copia, 'nombre', False)
    elif opcion == '3': ordenar_lista(copia, 'poblacion', True)
    elif opcion == '4': ordenar_lista(copia, 'poblacion', False)
    elif opcion == '5': ordenar_lista(copia, 'superficie', True)
    elif opcion == '6': ordenar_lista(copia, 'superficie', False)
    elif opcion == '7': return
    else:
        print('ERROR: Opcion invalida')

    mostrar_lista(copia)


# --- OPCION 6: MOSTRAR ESTADISTICAS ---

def mostrar_estadisticas(paises):
    # Inicializamos acumuladores para calcular promedios
    acum_sup = 0
    acum_pob = 0

    # Tomamos el primer país como referencia inicial para mayor y menor
    pob_mayor = paises[0]
    pob_menor = paises[0]

    # Diccionario para contar cuántos países hay por continente
    paises_por_continente = {}

    for p in paises:
        # Acumulamos superficie y población para calcular promedios al final
        acum_sup += p['superficie']
        acum_pob += p['poblacion']

        # Actualizamos el país con mayor población si encontramos uno más grande
        if p['poblacion'] > pob_mayor['poblacion']:
            pob_mayor = p

        # Actualizamos el país con menor población si encontramos uno más chico
        if p['poblacion'] < pob_menor['poblacion']:
            pob_menor = p

        # Contamos países por continente usando el continente como clave del diccionario
        cont = p['continente']
        if cont in paises_por_continente:
            paises_por_continente[cont] += 1
        else:
            # Primera vez que aparece este continente, lo inicializamos en 1
            paises_por_continente[cont] = 1

    # Mostramos todos los indicadores calculados
    # // es división entera para obtener el promedio sin decimales
    print(f'\nTotal de paises cargados: {len(paises)}.')
    print(f'\nPais con mayor poblacion: {pob_mayor["nombre"]} con {pob_mayor["poblacion"]:,} habitantes.')
    print(f'Pais con menor poblacion: {pob_menor["nombre"]} con {pob_menor["poblacion"]:,} habitantes.')
    print(f'\nPromedio de poblacion: {(acum_pob // len(paises)):,} habitantes.')
    print(f'Promedio de superficie: {(acum_sup // len(paises)):,} km2.')
    print('\nCantidad de paises por continente:')
    for cont in paises_por_continente:
        print(f'{cont}: {paises_por_continente[cont]} pais/es')


# --- MENÚ PRINCIPAL ---

def menu_principal():
    # Cargamos los países desde el CSV al iniciar el programa
    paises = cargar_paises()
    print(f'\nSistema iniciado. {len(paises)} paises cargados desde {ruta_archivo}.')

    while True:
        print('''
========================================
  GESTIÓN DE DATOS DE PAÍSES - UTN TUP
========================================
1. Agregar pais
2. Actualizar pais
3. Buscar pais por nombre
4. Filtrar paises
5. Ordenar paises
6. Mostrar estadisticas
7. Mostrar todos los paises
8. Salir
========================================''')

        opcion = input('Seleccione una opcion: ').strip()

        if opcion == '1':   agregar_pais(paises)
        elif opcion == '2': actualizar_pais(paises)
        elif opcion == '3': buscar_pais(paises)
        elif opcion == '4': menu_filtros(paises)
        elif opcion == '5': menu_ordenar(paises)
        elif opcion == '6': mostrar_estadisticas(paises)
        elif opcion == '7': mostrar_lista(paises)
        elif opcion == '8':
            print('\nHasta luego!')
            break
        else:
            print('\nERROR: Opcion invalida. Ingrese un numero del 1 al 8.')


# Punto de entrada del programa
menu_principal()
