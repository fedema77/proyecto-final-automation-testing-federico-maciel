# Proyecto Final de Automation Testing

## Propósito del proyecto
Este proyecto implementa un framework completo de automatización de pruebas para aplicaciones web y APIs, utilizando Python, Selenium WebDriver, Pytest y Requests. El objetivo es validar escenarios críticos de negocio, aplicar buenas prácticas de automatización y generar reportes visuales claros para análisis y auditoría.

## Tecnologías utilizadas
- Python 3
- Selenium WebDriver
- Pytest
- pytest-html
- Requests
- Git y GitHub
- Page Object Model (POM)

## Estructura del proyecto

```text
proyecto-final-automation-testing/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── data/
│   └── users.json
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_ui.py
│   └── test_api.py
├── utils/
│   ├── __init__.py
│   ├── driver_setup.py
│   ├── file_reader.py
│   ├── logger_config.py
│   └── screenshot_utils.py
├── reports/
│   └── html/
├── screenshots/
│   └── failures/
├── logs/
│   └── automation.log
├── .github/
│   └── workflows/
│       └── ci.yml
└── .pytest_cache/
```

## Casos de prueba incluidos
### Pruebas de UI
- Login exitoso
- Login con credenciales inválidas
- Login con usuario bloqueado
- Verificación de catálogo de productos
- Agregar producto al carrito
- Checkout completo

### Pruebas de API
- GET listado de usuarios
- POST crear usuario
- DELETE eliminar usuario

## Instalación de dependencias
Desde la raíz del proyecto, ejecutar:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar las pruebas
Para ejecutar toda la suite:

```bash
pytest -q
```

Para generar y revisar el reporte HTML:

```bash
pytest
```

El reporte se genera en:

```text
reports/html/report.html
```

## Capturas de pantalla
Cuando una prueba falla, el framework guarda automáticamente una captura en la carpeta:

```text
screenshots/failures/
```

## Logging
El proyecto registra eventos importantes en:

```text
logs/automation.log
```

## Cómo interpretar los reportes
- Los reportes HTML muestran cada caso ejecutado
- Se indica si pasó o falló
- Se incluye duración del test
- En fallos, se adjuntan capturas de pantalla relevantes para facilitar la depuración

## Repositorio y CI/CD
También se incluye una configuración de GitHub Actions para ejecutar la suite con cada push o pull request.

## Recomendación de nombre de repositorio
```text
proyecto-final-automation-testing-[nombre-apellido]
```

## Conclusión
Este framework está preparado para automatizar pruebas UI y API de forma modular, reutilizable y mantenible, cumpliendo los lineamientos de un proyecto final de automatización de QA.
