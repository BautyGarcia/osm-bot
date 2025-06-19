#!/usr/bin/env python3
"""
OSM Bot - Automatización para Online Soccer Manager

Este script automatiza el login en Online Soccer Manager.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ========== CONFIGURACIÓN ==========
# Cambiar estos valores por tus credenciales
USERNAME = "Crocoo"  # Cambiar por tu nombre de usuario
PASSWORD = "Bauty2005!"  # Cambiar por tu contraseña

OSM_URL = "https://en.onlinesoccermanager.com/ChooseLeague"

def wait_for_element(driver, by, value, timeout=10, condition="presence"):
    """
    Espera hasta que aparezca un elemento en la página
    
    Args:
        driver: WebDriver instance
        by: Tipo de selector (By.ID, By.XPATH, etc.)
        value: Valor del selector
        timeout: Tiempo máximo de espera en segundos (default: 10)
        condition: Tipo de condición a esperar (default: "presence")
                  - "presence": elemento presente en DOM
                  - "visible": elemento visible
                  - "clickable": elemento clickeable
    
    Returns:
        WebElement si se encuentra, None si no se encuentra
    """
    try:
        wait = WebDriverWait(driver, timeout)
        
        if condition == "presence":
            element = wait.until(EC.presence_of_element_located((by, value)))
        elif condition == "visible":
            element = wait.until(EC.visibility_of_element_located((by, value)))
        elif condition == "clickable":
            element = wait.until(EC.element_to_be_clickable((by, value)))
        else:
            print(f"⚠️ Condición '{condition}' no reconocida, usando 'presence'")
            element = wait.until(EC.presence_of_element_located((by, value)))
        
        return element
    except Exception as e:
        print(f"❌ Timeout esperando elemento {by}='{value}': {e}")
        return None

def main():
    print("🚀 Iniciando OSM Bot...")
    
    # Configurar Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--mute-audio")  # Iniciar sin sonido
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Crear driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # PASO 1: Entrar a la URL
        print("🌐 Navegando a Online Soccer Manager...")
        driver.get(OSM_URL)
        
        # PASO 2: Esperar a que se cargue la página (buscar el botón Accept)
        print("⏳ Esperando a que cargue la página...")
        if not wait_for_element(driver, By.XPATH, "//span[contains(text(), 'Accept')]", timeout=15):
            print("❌ La página no cargó correctamente")
            return
        
        # PASO 3: Apretar el botón "Accept"
        print("✅ Buscando y clickeando botón 'Accept'...")
        accept_button = wait_for_element(driver, By.XPATH, "//span[contains(text(), 'Accept')]", condition="clickable")
        if accept_button:
            accept_button.click()
            print("✅ Botón 'Accept' clickeado")
        else:
            print("⚠️ No se encontró el botón 'Accept'")
            return
        
        # PASO 4: Apretar el botón "Log in"
        print("🔑 Buscando y clickeando botón 'Log in'...")
        login_button = wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Log in')] | //a[contains(text(), 'Log in')] | //input[@value='Log in']", condition="clickable")
        if login_button:
            login_button.click()
            print("✅ Botón 'Log in' clickeado")
        else:
            print("❌ Error al buscar botón 'Log in'")
            return
        
        # PASO 5: Esperar y buscar el campo de usuario
        print("👤 Esperando campo de usuario...")
        username_field = wait_for_element(driver, By.ID, "manager-name", condition="visible")
        if username_field:
            username_field.clear()
            username_field.send_keys(USERNAME)
            print("✅ Nombre de usuario ingresado")
        else:
            print("❌ Error al encontrar campo de usuario")
            return
        
        # PASO 6: Ingresar contraseña
        print("🔒 Ingresando contraseña...")
        password_field = wait_for_element(driver, By.ID, "password", condition="visible")
        if password_field:
            password_field.clear()
            password_field.send_keys(PASSWORD)
            print("✅ Contraseña ingresada")
        else:
            print("❌ Error al encontrar campo de contraseña")
            return
        
        # PASO 7: Apretar el botón de login
        print("🚪 Clickeando botón de login...")
        final_login_button = wait_for_element(driver, By.ID, "login", condition="clickable")
        if final_login_button:
            final_login_button.click()
            print("✅ Botón de login clickeado")
        else:
            print("❌ Error al encontrar botón de login")
            return
        
        # Función para ejecutar pasos 8-10 (balances, scroll, anuncios)
        def execute_balances_and_ads():
            # PASO 8: Esperar y clickear el div con id "balances"
            print("💰 Esperando y buscando div 'balances'...")
            balances_div = wait_for_element(driver, By.ID, "balances", timeout=15, condition="clickable")
            if balances_div:
                balances_div.click()
                print("✅ Div 'balances' clickeado")
            else:
                print("❌ Error al encontrar div 'balances'")
                return False
            
            # PASO 9: Esperar modal store y elemento bcdeals, luego hacer scroll horizontal
            print("🛒 Esperando modal store...")
            modal_store = wait_for_element(driver, By.ID, "modal-dialog-store", timeout=15, condition="visible")
            if modal_store:
                print("✅ Modal store encontrado")
                print("🎯 Esperando elemento 'product-category-bcdeals'...")
                bcdeals_element = wait_for_element(driver, By.ID, "product-category-bcdeals", timeout=15, condition="presence")
                if bcdeals_element:
                    print("✅ Elemento 'bcdeals' encontrado")
                    print("📦 Buscando contenedor scrolleable...")
                    scrollable_container = wait_for_element(driver, By.CLASS_NAME, "scrollable-products-container", timeout=10, condition="presence")
                    if scrollable_container:
                        print("✅ Contenedor scrolleable encontrado, haciendo scroll a la derecha...")
                        # Hacer scroll horizontal a la derecha (3000px) en el contenedor específico
                        driver.execute_script("arguments[0].scrollLeft += 3000;", scrollable_container)
                        print("✅ Scroll a la derecha completado en contenedor de productos")
                    else:
                        print("❌ Error al encontrar contenedor 'scrollable-products-container'")
                        return False
                else:
                    print("❌ Error al encontrar elemento 'product-category-bcdeals'")
                    return False
            else:
                print("❌ Error al encontrar modal 'modal-dialog-store'")
                return False
            
            return True
        
        # Ejecutar pasos 8-9 por primera vez
        if not execute_balances_and_ads():
            return
        
        # PASO 10: Loop infinito para ver anuncios
        print("📺 Iniciando loop infinito para ver anuncios...")
        print("🔄 Presiona Ctrl+C para detener el loop de anuncios")
        
        ad_counter = 0
        while True:
            try:
                # Primero verificar si hay mensaje de límite
                print(f"🔍 Verificando límite de videos...")
                limit_message = wait_for_element(driver, By.XPATH, "//h3[contains(text(), \"Can't show video\")]", timeout=3, condition="presence")
                
                if limit_message:
                    print("⏰ ¡Límite de videos alcanzado!")
                    print("📝 Mensaje: 'Can't show video' detectado")
                    
                    # Buscar también el mensaje con los minutos específicos
                    detail_message = wait_for_element(driver, By.XPATH, "//p[contains(text(), 'You have reached the maximum of videos you can watch here')]", timeout=2, condition="presence")
                    if detail_message:
                        detail_text = detail_message.text
                        print(f"📝 Detalle: {detail_text}")
                    
                    print("⏳ Esperando 5 minutos antes de volver a intentar...")
                    
                    # Esperar 5 minutos (300 segundos) con countdown
                    for remaining in range(300, 0, -30):
                        minutes = remaining // 60
                        seconds = remaining % 60
                        print(f"⏰ Tiempo restante: {minutes}:{seconds:02d} minutos")
                        time.sleep(30)  # Esperar 30 segundos y mostrar update
                    
                    print("✅ Espera completada")
                    print("🔄 Refrescando página...")
                    driver.refresh()
                    
                    print("🔄 Reejecutando desde paso 8...")
                    if not execute_balances_and_ads():
                        print("❌ Error al reejecutar pasos después del refresh")
                        return
                    
                    print("✅ Página refrescada, continuando con anuncios...")
                    continue
                
                # Buscar botón "Watch ad"
                print(f"🔍 Buscando botón 'Watch ad' (Anuncio #{ad_counter + 1})...")
                watch_ad_button = wait_for_element(driver, By.XPATH, "//div[contains(text(), 'Watch ad')]", timeout=10, condition="clickable")
                
                if watch_ad_button:
                    print(f"📺 Anuncio #{ad_counter + 1} - Clickeando 'Watch ad'...")
                    watch_ad_button.click()
                    ad_counter += 1
                    
                    # Esperar a que el anuncio termine (el botón vuelva a aparecer)
                    print("⏳ Esperando a que termine el anuncio...")
                    
                    # Esperar un poco para que el anuncio se abra
                    time.sleep(2)
                    
                    # Esperar a que el botón "Watch ad" vuelva a estar disponible
                    print("🔄 Esperando a que el anuncio termine y el botón vuelva a aparecer...")
                    next_ad_button = wait_for_element(driver, By.XPATH, "//div[contains(text(), 'Watch ad')]", timeout=60, condition="clickable")
                    
                    if next_ad_button:
                        print(f"✅ Anuncio #{ad_counter} completado. Preparando siguiente anuncio...")
                        time.sleep(1)  # Pequeña pausa antes del siguiente anuncio
                    else:
                        print("⚠️ El botón 'Watch ad' no volvió a aparecer, continuando...")
                
                else:
                    print("⚠️ No se encontró botón 'Watch ad', esperando...")
                    time.sleep(5)  # Esperar 5 segundos antes de intentar de nuevo
                    
            except KeyboardInterrupt:
                print(f"\n🛑 Loop de anuncios detenido por el usuario")
                print(f"📊 Total de anuncios vistos: {ad_counter}")
                break
            except Exception as e:
                print(f"❌ Error en loop de anuncios: {e}")
                print("🔄 Continuando con el siguiente intento...")
                time.sleep(3)
        
        print("🎉 ¡Todos los pasos completados!")
        print("🔄 El navegador se mantendrá abierto...")
        
        # Mantener el navegador abierto
        input("Presiona Enter para cerrar el navegador...")
        
    except Exception as e:
        print(f"❌ Error general: {e}")
    
    finally:
        print("🔄 Cerrando navegador...")
        driver.quit()
        print("👋 Bot terminado")

if __name__ == "__main__":
    # Verificar que las credenciales estén configuradas
    if USERNAME == "tu_usuario_aqui" or PASSWORD == "tu_contraseña_aqui":
        print("⚠️  ADVERTENCIA: Debes cambiar USERNAME y PASSWORD en el script")
        print("📝 Edita las líneas 14-15 con tus credenciales reales")
        print()
        
        # Preguntar si quiere continuar para hacer pruebas
        respuesta = input("¿Quieres continuar para hacer pruebas? (y/N): ")
        if respuesta.lower() != 'y':
            print("👋 Configurar credenciales y ejecutar nuevamente")
            exit()
    
    main() 