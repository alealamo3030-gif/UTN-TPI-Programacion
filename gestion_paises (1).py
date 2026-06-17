import csv

# ============================================
# GESTIÓN DE DATOS DE PAÍSES EN PYTHON
# TPI - Programación 1 - UTN TUP 2026
# Alumnos: Peralta - Alamo
# ============================================

ruta_archivo = 'paises.csv'

# --- LECTURA Y ESCRITURA DEL CSV ---

def cargar_paises ():
    # Cargamos los países desde el CSV usando DictReader
    # para acceder a cada campo por nombre de columna
    paises = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        'nombre':     fila['nombre'].strip(),
                        'poblacion':  int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print(f'ERROR: Fila con formato invalido ignorada: {fila}')
    except FileNotFoundError:
        print(f"ERROR: El archivo '{ruta_archivo}' no se encontro en la carpeta.")

    except KeyError: 
        print('ERROR: El CSV no tiene una clave de una columna. Verifique los encabezados')

    except Exception as e:
        print(f'Ocurrio un error inesperado: {e}')

    return paises

def guardar_archivo_paises(paises):
    # Guardamos la lista de paises en el CSV usando DictWriter
    # con writeheader() para escribir los encabezados automáticamente
    columnas = ['nombre', 'poblacion', 'superficie', 'continente']
    with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(paises)

# --- MOSTRAR PAÍSES --- (funciones que usaremos en varias opciones)

def mostrar_pais(pais):
    # Muestra los datos de un país de forma formateada
    print(f"  Nombre:     {pais['nombre']}")
    print(f"  Poblacion:  {pais['poblacion']:,} habitantes")
    print(f"  Superficie: {pais['superficie']:,} km2")
    print(f"  Continente: {pais['continente']}")
    print()


def mostrar_lista(paises):
    # Muestra una lista de países numerada
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
        nombre = input('Ingrese el nombre del pais: ').strip().title()
        if not nombre.replace(" ", "").isdigit() or nombre == '':
            print('\nERROR: El nombre no puede estar vacio ni contener numeros.')
            return
        
        for p in paises:
            if p['nombre'] == nombre:
                print('ERROR: El pais ya se encuentra en la lista')
                return
        
        continente = input('Ingrese el continente del pais: ').strip().title()
        if not continente.replace(" ", "").isdigit() or continente == '':
            print('\nERROR: El continente no puede estar vacio ni contener numeros.')
            return
        
        poblacion = int(input('Ingrese poblacion del pais: '))
        if poblacion < 0:
            print('\nERROR: La poblacion no puede ser menor que 0.')
            return
        
        superficie = int(input('Ingrese la superficie del pais en km2: '))
        if superficie <= 0:
            print('\nERROR: La superficie no puede ser menopr o igual a 0.')
            return
        
        nuevo = {
            'nombre':     nombre,
            'poblacion':  poblacion,
            'superficie': superficie,
            'continente': continente
            }
        
        paises.append(nuevo)
        guardar_archivo_paises(paises)
        print(f'Los datos del pais {nombre} fueron cargados correctamente.')
    
    except ValueError:
        print('\nERROR: El valor ingresado debe ser un numero entero.')

# --- OPCION 2: ACTUALIZAR PAIS ---
def actualizar_pais(paises):
    print('\n--- ACTUALIZAR PAÍS ---')
    nombre = input('Ingrese el nombre exacto del pais a actualizar: ').strip().title()
    
    encontrado = False
    for i in range(len(paises)):
        if paises[i]['nombre'] == nombre:
            encontrado = True
            print(f'\nPais encontrado: {paises[i]["nombre"]}')
            print(f'Poblacion actual: {paises[i]["poblacion"]:,}')
            print(f'Superficie actual: {paises[i]["superficie"]:,}')
            try:
                nueva_pob = int(input('\nNueva poblacion (Enter para no modificar): ') or paises[i]['poblacion'])
                nueva_sup = int(input('Nueva superficie en km2 (Enter para no modificar): ') or paises[i]['superficie'])

                if nueva_pob < 0 or nueva_sup <= 0:
                    print('ERROR: Los valores deben ser enteros positivos.')
                    return

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
    termino = input('Ingrese nombre o parte del nombre: ').strip().lower()

    if termino == '':
        print('ERROR: Debe ingresar un termino de busqueda.')
        return

    # Buscamos coincidencias parciales (si el término está contenido en el nombre)
    resultados = []
    for p in paises:
        if termino in p['nombre'].lower():
            resultados.append(p)

    mostrar_lista(resultados)

# --- OPCION 4: FILTRAR PAISES ---

def filtrar_por_continente(paises):
    print('\n--- FILTRAR POR CONTINENTE ---')
    continente = input('\nIngrese el continente: ').strip().title()

    if continente == '':
        print('\nERROR: El continente a buscar no puede estar vacio')
        return
    
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

        if poblacion_min > poblacion_max:
            print('\nERROR: El minimo no puede ser un numero mayo al maximo.')
            return
        
        resultados = []
        for p in paises:
            if p['poblacion'] > poblacion_min and p['poblacion'] < poblacion_max:
                resultados.append(p)
        mostrar_lista(resultados)
    
    except ValueError:
        print('\nERROR: La poblacion debe ser un numero entero.')

def filtrar_por_superficie(paises):
    print('\n--- FILTRAR POR SUPERFICIE ---')
    try:
        superficie_min = int(input('\nIngrese el minimo de superficie en km2: '))
        superficie_max = int(input('\nIngrese el maximo de superficie en km2: '))

        if superficie_min > superficie_max:
            print('\nERROR: El minimo no puede ser una superficie mayor al maximo.')
            return
        
        resultados = []
        for p in paises:
            if p['superficie'] > superficie_min and p['superficie'] < superficie_max:
                resultados.append(p)
        mostrar_lista(resultados)
    
    except ValueError:
        print('\nERROR: La superficie debe ser un numero entero.')
    
def menu_filtros(paises):
    print('''
--- FILTROS ---
1. Por continente
2. Por rango de poblacion
3. Por rango de superficie
4. Salir
''')
    opcion = input('Ingrese opcion a filtrar: ').strip()
    if opcion == '1': filtrar_por_continente(paises)
    elif opcion == '2': filtrar_por_poblacion(paises)
    elif opcion == '3': filtrar_por_superficie(paises)
    elif opcion == '4': return
    else:
        print('ERROR: Opcion invalida')

# --- OPCION 5: ORDENAR PAISES ---

def ordenar_lista(copia, clave, orden=True):
    n = len(copia)

    for i in range(n):
        for j in range(0, n - i - 1):

            valor_actual   = copia[j][clave]
            valor_siguiente = copia[j + 1][clave]

            # Comparamos según el orden pedido y si están mal ubicados los intercambiamos
            if orden:
                if valor_actual > valor_siguiente:
                    # Intercambiamos los dos elementos de lugar
                    copia[j], copia[j + 1] = copia[j + 1], copia[j]
            else:
                if valor_actual < valor_siguiente:
                    # Intercambiamos los dos elementos de lugar
                    copia[j], copia[j + 1] = copia[j + 1], copia[j]

    return copia

def menu_ordenar(paises):
    print('''
--- FILTROS ---
1. Por nombre A-Z
2. Por nombre Z-A
3. Por poblacion ascendente
4. Por poblacion descendente
5. Por superficie ascendente
6. Por superficie descendente
7. Salir
''')
    opcion = input('Ingrese opcion a filtrar: ').strip()
    copia = paises

    if opcion == '1': ordenar_lista(copia,'nombre',True)
    elif opcion == '2': ordenar_lista(copia,'nombre',False)
    elif opcion == '3': ordenar_lista(copia,'poblacion',True)
    elif opcion == '4': ordenar_lista(copia,'poblacion',False)
    elif opcion == '5': ordenar_lista(copia,'superficie',True)
    elif opcion == '6': ordenar_lista(copia,'superficie',False)
    elif opcion == '7': return
    else:
        print('ERROR: Opcion invalida')

    mostrar_lista(copia)

# --- OPCION 6: MOSTRAR ESTADISTICAS ---

def mostrar_estadisticas(paises):
    acum_sup = 0
    acum_pob = 0
    pob_mayor = paises [0]
    pob_menor = paises [0]
    paises_por_continente = {}
    for p in paises:
        acum_sup += p['superficie']
        acum_pob += p['poblacion']
        if p['poblacion'] > pob_mayor['poblacion']:
            pob_mayor = p
        if p['poblacion'] < pob_menor['poblacion']:
            pob_menor = p
        cont = p['continente']
        if cont in paises_por_continente:
            paises_por_continente[cont] += 1
        else:
            paises_por_continente[cont] = 1
    
    print(f'\nTotal de paises cargados: {len(paises)}.')
    print(f'\nPais con mayor poblacion: {pob_mayor['nombre']} con {pob_mayor['poblacion']:,} habitantes.')
    print(f'Pais con menor poblacion: {pob_menor['nombre']} con {pob_menor['poblacion']:,} habitantes.')
    print(f'\nPromedio de poblacion: {(acum_pob//len(paises)):,} habitantes.')
    print(f'Promedio de superficie: {(acum_sup//len(paises)):,} km2.')
    print('\nCantidad de paises por continente:')
    for cont in paises_por_continente:
        print(f'{cont}: {paises_por_continente[cont]} pais/es') 



# --- MENÚ PRINCIPAL ---

def menu_principal():
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

        if opcion == '1':agregar_pais(paises)
        elif opcion == '2':actualizar_pais(paises)
        elif opcion == '3':buscar_pais(paises)
        elif opcion == '4':menu_filtros(paises)
        elif opcion == '5':menu_ordenar(paises)
        elif opcion == '6':mostrar_estadisticas(paises)
        elif opcion == '7':mostrar_lista(paises)
        elif opcion == '8':
            print('\nHasta luego!')
            break
        else:
            print('\nERROR: Opcion invalida. Ingrese un numero del 1 al 8.')


# Punto de entrada del programa
menu_principal()