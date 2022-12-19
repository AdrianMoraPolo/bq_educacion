import time
import unittest
import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from functions.global_functions import globalfunctions





class testalert(unittest.TestCase):

    @pytest.mark.reports

    # Importamos chromedriver para poder realizar los test en Chrome
    def setUp(self):
        driver_service = Service(executable_path="\path\chromedriver.exe")
        self.driver = webdriver.Chrome(service=driver_service)

    def test1(self):
        driver = self.driver
        f = globalfunctions(driver)
        # Link de la página y expandimos la ventana a pantalla completa
        f.route("http://localhost:8000/login")
        # Esperamos 1 segundo (importado arriba en time)
        time.sleep(1)

        # Hacemos click en el botón "Sign Up" del menú superior derecho
        driver.find_element(By.XPATH, "//a[contains(text(),'Sign Up')]").click()
        time.sleep(1)
        # Buscamos el elemento por ID
        username=driver.find_element(By.ID, "signup-username")
        # Introducimos Username en el input
        username.send_keys("Username")
        time.sleep(1)
        # Repetimos el proceso con la contraseña, usamos el selector por ID para mayor exactitud
        password1=driver.find_element(By.ID, "signup-password")
        password1.send_keys("Password")
        time.sleep(1)
        # Hacemos click en el icono de ver mostrar contraseña
        driver.find_element(By.ID, "signup-password-icon").click()
        time.sleep(1)
        # Continuamos con el segundo input de password
        password2=driver.find_element(By.ID, "signup-password2")
        password2.send_keys("Password2")
        time.sleep(1)
        driver.find_element(By.ID, "signup-password2-icon").click()
        time.sleep(1)
        # Introducimos un nombre
        name=driver.find_element(By.ID, "signup-name")
        name.send_keys("John Johnson")
        time.sleep(1)
        # Introducimos un email valido
        email=driver.find_element(By.ID, "signup-email")
        email.send_keys("username@gmail.com")
        time.sleep(1)
        # Hacemos click en el botón de "Sign Up" para comprobar que no podemos continuar con el registro porque está bloqueado
        driver.find_element(By.XPATH, "//button[contains(@id,'signup-submit')]").click()

        # Corregimos los errores que intencionadamente hemos introducido antes, borrando las contraseñas e introduciendo nuevas
        password1.clear()
        time.sleep(1)
        password2.clear()
        time.sleep(1)
        password1.send_keys("Password2-!")
        time.sleep(1)
        password2.send_keys("Password2-!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@id,'signup-submit')]").click()
        time.sleep(1)
        # Corregimos el input "Username" y añadimos un nombre de usuario que aún no esté registrado
        # Por ejemplo añadiendo un numero adicional al usuario
        time.sleep(1)
        username.send_keys("12345")
        time.sleep(1)
        # Hacemos click en el exterior del input para comprobar que está correcto y para que el botón "Sign Up" se desboquee
        driver.find_element(By.XPATH, "//img[contains(@class,'w-44')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@id,'signup-submit')]").click()
        time.sleep(1)
        # Obtenemos una evidencia de que nuestro registro se ha completado y hemos llegado a la ventana Home con nuestro usuario
        element=driver.find_element(By.XPATH, "//div[contains(@id,'welcome')]")
        location = element.location
        size = element.size
        driver.save_screenshot("Screenshots\welcome.png")
        # Desconectamos nuestro usuario para volver a la ventana de Login
        driver.find_element(By.XPATH, "//a[@href='/signout'][contains(.,'Sign Out')]").click()
        time.sleep(1)

        # Rellenamos el nombre de usuario y contraseña con los datos del usuario que hemos creado
        userlogin=driver.find_element(By.XPATH, "//input[contains(@id,'login-username')]")
        userlogin.send_keys("Username12345")
        time.sleep(1)
        passwordlogin=driver.find_element(By.XPATH, "//input[contains(@id,'login-password')]")
        passwordlogin.send_keys("Password2-!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@id,'login-submit')]").click()
        time.sleep(1)
        element = driver.find_element(By.XPATH, "// div[contains( @ id, 'welcome')]")
        location = element.location
        size = element.size
        driver.save_screenshot("Screenshots\welcome2.png")

        time.sleep(1)

        driver.close()