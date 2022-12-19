import time
import unittest
import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from functions.global_functions import globalfunctions



class testalert(unittest.TestCase):

    @pytest.mark.validar
    # Importamos chromedriver para poder realizar los test en Chrome
    def setUp(self):
        driver_service = Service(executable_path="\path\chromedriver.exe")
        self.driver = webdriver.Chrome(service=driver_service)

    def test1(self):
        driver=self.driver
        f=globalfunctions(driver)
        # Link de la página y expandimos la ventana a pantalla completa
        f.route("http://localhost:8000/login")
        # Esperamos 1 segundo (importado arriba en time)
        time.sleep(1)

        # Hacemos click en el botón "Sign Up" del menú superior derecho
        driver.find_element(By.XPATH, "//a[contains(text(),'Sign Up')]").click()
        time.sleep(1)
        # Buscamos el elemento por ID
        username = driver.find_element(By.ID, "signup-username")
        # Introducimos Username en el input
        username.send_keys("Username")
        time.sleep(1)
        # Hacemos click en el exterior del input para comprobar que está correcto y para que el botón "Sign Up" se desboquee
        driver.find_element(By.XPATH, "//img[contains(@class,'w-44')]").click()
        alertuser1=driver.find_element(By.XPATH, "//span[@class='block sm:inline'][contains(.,'Username already exists')]").text
        alertuser2="Username already exists"
        # Comparamos el texto de la advertencia de usuario y el texto que debería mostrar para ver si es correcto
        assert alertuser1==alertuser2
        time.sleep(1)
        # Repetimos el proceso con la contraseña, usamos el selector por ID para mayor exactitud
        password1 = driver.find_element(By.ID, "signup-password")
        password1.send_keys("Password")
        time.sleep(1)
        # Hacemos click en el exterior del input para comprobar que está correcto y para que el botón "Sign Up" se desboquee
        driver.find_element(By.XPATH, "//img[contains(@class,'w-44')]").click()
        alertpass1 = driver.find_element(By.XPATH,"//span[@class='block sm:inline'][contains(.,'Password must contain at least 1 number')]").text
        alertpass2 = "Password must contain at least 1 number"
        assert alertpass1 == alertpass2
        time.sleep(1)
        # Hacemos click en el icono de ver mostrar contraseña
        driver.find_element(By.ID, "signup-password-icon").click()
        time.sleep(1)
        # Continuamos con el segundo input de password
        password2 = driver.find_element(By.ID, "signup-password2")
        password2.send_keys("Password2")
        # Hacemos click en el exterior del input para comprobar que está correcto y para que el botón "Sign Up" se desboquee
        driver.find_element(By.XPATH, "//img[contains(@class,'w-44')]").click()
        time.sleep(1)
        alertpassw1 = driver.find_element(By.XPATH,"//span[@class='block sm:inline'][contains(.,'Passwords do not match')]").text
        alertpassw2 = "Passwords do not match"
        assert alertpassw1 == alertpassw2
        time.sleep(1)
        driver.find_element(By.ID, "signup-password2-icon").click()
        time.sleep(1)




        driver.close()