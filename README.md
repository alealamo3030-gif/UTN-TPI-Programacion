Trabajo Práctico Integrador — Programación 1
Tecnicatura Universitaria en Programación a Distancia (UTN)

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar un dataset de países (nombre, población, superficie y continente). El sistema permite agregar, actualizar, buscar, filtrar, ordenar y obtener estadísticas sobre los países cargados, persistiendo la información en un archivo CSV.

## Estructura del repositorio

- `gestion_paises.py` — Código fuente del programa.
- `paises.csv` — Dataset base de países.
- `README.md` — Este archivo.

## Requisitos

- Python 3.x (no requiere instalar librerías externas).

## Cómo ejecutar el programa

1. Descargar o clonar este repositorio.
2. Verificar que `paises.csv` esté en la misma carpeta que `gestion_paises.py`.
3. Ejecutar desde la terminal:

```
python gestion_paises.py
```

4. Se mostrará el menú principal:

```
========================================
  GESTION DE DATOS DE PAISES - UTN TUP
========================================
1. Agregar país
2. Actualizar país
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los países
8. Salir
========================================
```

## Ejemplos de uso

### Agregar un país (opción 1)

**Entrada:**
```
Ingrese el nombre del país: Uruguay
Ingrese el continente del país: America
Ingrese población del país: 3500000
Ingrese la superficie del país en km2: 176215
```

**Salida:**
```
Los datos del país Uruguay fueron cargados correctamente.
```

### Buscar un país por nombre (opción 3)

**Entrada:**
```
Ingrese nombre o parte del nombre: arg
```

**Salida:**
```
Se encontraron 1 país/es:

--- País 1 ---
  Nombre:     Argentina
  Población:  45,376,763 habitantes
  Superficie: 2,780,400 km2
  Continente: America
```

### Mostrar estadísticas (opción 6)

**Salida:**
```
Total de países cargados: 4.

País con mayor población: Brasil con 213,993,437 habitantes.
País con menor población: Alemania con 83,149,300 habitantes.

Promedio de población: 117,079,875 habitantes.
Promedio de superficie: 3,008,396 km2.

Cantidad de países por continente:
America: 2 país/es
Asia: 1 país/es
Europa: 1 país/es
```

## Participación de los integrantes

| Integrante | Usuario GitHub | Funcionalidades desarrolladas |
|---|---|---|
| Alejandro Alamo | [alealamo3030-gif](https://github.com/alealamo3030-gif) | Agregar país, Buscar país, Mostrar países, Lectura/escritura de CSV |
| Santiago Peralta | [santiperalta78-sys](https://github.com/santiperalta78-sys) | Actualizar país, Filtrar países, Ordenar países, Estadísticas |

Ambos integrantes participaron en el diseño general del sistema, las pruebas de robustez y la redacción de la documentación.

## Documentación y video

- 📄 Documentación PDF: https://drive.google.com/file/d/13PLBpEPWQpq7R8Vv0f-7h-byGwrHUCxH/view?usp=sharing
- 🎥 Video explicativo: https://drive.google.com/file/d/1yhEHHBX-vnWf0XB46pcK9pM6mFlodWKd/view
