from selenium import webdriver

def get_driver():
    # Inicializa el navegador Chrome automáticamente (Selenium 4)
    driver = webdriver.Chrome()
    
    # Maximiza la ventana para ver todo bien
    driver.maximize_window()
    
    # Le da hasta 10 segundos al navegador para encontrar elementos lentos
    driver.implicitly_wait(10)
    
    return driver