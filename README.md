# Proyecto de Pre-Entrega: Automation Testing QA

## Propósito del proyecto
Este proyecto es la pre-entrega del curso de QA. Su objetivo es automatizar flujos básicos de navegación web en la página `saucedemo.com` utilizando Selenium WebDriver y Python, validando el login, el catálogo y el carrito de compras.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest y Pytest-html
- Git y GitHub

## Instrucciones de instalación de dependencias
Para que el proyecto funcione, necesitas instalar las siguientes librerías ejecutando este comando en la terminal:
`python -m pip install pytest selenium pytest-html`

## Comando para ejecutar las pruebas
Para correr los tests y generar el reporte HTML, ejecuta el siguiente comando en la terminal:
`python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html`