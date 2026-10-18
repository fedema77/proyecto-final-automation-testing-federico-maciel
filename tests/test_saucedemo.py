import pytest
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Esto ayuda a que Python encuentre nuestra carpeta 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.driver_setup import get_driver

# Configuración inicial y final para cada test (abre y cierra el navegador)
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# --- CASO 1: LOGIN EXITOSO ---
def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Espera explícita y validación de URL
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/inventory.html"))
    
    assert "inventory.html" in driver.current_url
    
    # Validar textos importantes
    titulo_sitio = driver.find_element(By.CLASS_NAME, "app_logo").text
    titulo_seccion = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_sitio == "Swag Labs"
    assert titulo_seccion == "Products"

# --- CASO 2: CATÁLOGO ---
def test_verificacion_catalogo(driver):
    # Login rápido
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Validar título de pestaña
    assert driver.title == "Swag Labs"
    
    # Validar menú y filtros presentes
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    
    # Validar que hay productos y obtener el primero
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0 
    
    primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n[INFO] Primer producto: {primer_nombre} - Precio: {primer_precio}")

# --- CASO 3: CARRITO ---
def test_interaccion_carrito(driver):
    # Login rápido
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Agregar el primer producto (Mochila)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # Verificar contador en 1
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"
    
    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Comprobar que el producto está en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_carrito) == 1
    
    nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == "Sauce Labs Backpack"