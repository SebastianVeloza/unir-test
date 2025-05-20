# Repo para EIEC - DevOps - UNIR

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio o de API y pruebas E2E o de GUI. El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.

El Makefile ofrece comandos para facilitar la creación de imágenes de Docker y la ejecución de las pruebas. El único requisito es tener Docker instalado. Los comandos funcionarán en MacOS y Linux. En caso de usar Windows, será necesario adaptarlos o ejecutarlos en una máquina virtual Linux con Docker instalado.

# Calculadora REST con Python y Flask

Este proyecto es una calculadora web desarrollada en Python utilizando Flask. Expone una API REST que permite realizar operaciones matemáticas básicas y avanzadas, con una cobertura completa de pruebas unitarias y de integración.

## Funcionalidades implementadas

- Suma: `/calc/add/<a>/<b>`
- Resta: `/calc/substract/<a>/<b>`
- Multiplicación: `/calc/multiply/<a>/<b>` _(requiere permiso válido)_
- División: `/calc/divide/<a>/<b>` _(valida división por cero)_
- Potenciación: `/calc/power/<a>/<b>`
- Raíz cuadrada: `/calc/sqrt/<a>`
- Logaritmo base 10: `/calc/log10/<a>`

---

## Requisitos

- Python 3.9 o superior
- Flask
- Pytest

### Instalar dependencias

```
pip install Flask pytest
```

### Ejecutar el servidor

Desde la raíz del proyecto:

```
python -m app.api
```

### Pruebas unitarias

```
pytest test/unit
```

### Pruebas REST (API)

Asegúrate de que el servidor esté corriendo (python -m app.api)

Ejecuta las pruebas con:

```
# PowerShell
$env:BASE_URL="http://127.0.0.1:5000"
pytest test/rest

# CMD
set BASE_URL=http://127.0.0.1:5000
pytest test/rest
```
