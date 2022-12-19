# Prueba QA Automatización - BQ Educación
En este readme encontrarás:

- Una breve descripción sobre la estructura del proyecto
- Instalaciones necesarias
- Cómo lanzar el proyecto

### Descripción del proyecto

- He dividido la prueba en dos test. Testeando las funcionalidades básicas que ya hemos sometido a pruebas manuales pero en las que podrían aparecer bugs en el futuro, por nuevas funcionalidades o cambios que afecten a los componentes usados.
  - "test_end2end.py" Que se centra en realizar un end2end completo a la aplicación. Simulando que nuestra aplicación funciona y queremos lanzar un test de regresión de principio a fin.
  - "test_alerts.py" Que realiza una comprobación de las alertas de usuario y contraseña
- He añadido segundos entre cada paso para que se pueda apreciar mejor la prueba, pero normalmente al lanzar un test de automatización primaría la velocidad. Por lo que esos segundos de espera no estarían implementados.
- Prioricé estructurar el proyecto de la forma más básica y eficaz para que se pueda diferenciar cada paso y no resulte complicado entender el funcionamiento

### Instalaciones necesarias
  Para poder lanzar los test correctamente es necesario tener instalado lo siguiente:
  - Descargar e instalar Python https://www.python.org/downloads/
  - Comprobar que lo tenemos instalado y que versión con: `python` en cmd
  - Instalar Selenium con `pip install selenium`
  - Actualizar Selenium en su directorio raiz con `python -m pip install --upgrade pip`
  - Instalar Visual Studio Code y añadir los siguientes pluggins:
    - Katalium Selenium
    - WebDriverIO snippets
  - Yo he añadido un archivo de Chromedriver a la carpeta "path" dentro del proyecto acorde a mi versión de Chrome. Yo tengo la "Versión 108.0.5359.125 (Build oficial) (64 bits)" En caso de que no funcione, comprobar la versión de chrome y descargar (no aparece la de x64, así que descargar la de win32
     ![image](https://user-images.githubusercontent.com/50373485/208441214-963e0fc3-76ee-4fce-aa8d-f92daf4849ed.png)
   ![image](https://user-images.githubusercontent.com/50373485/208441743-9b3ae51a-5043-4eb4-a70d-751f917fc452.png)
   - Instalamos Pycharm y creamos un nuevo proyecto 
   - Vamos a settings y añadimos los siguientes interpretes: "selenium", "pytest", "pytest-thml"
![image](https://user-images.githubusercontent.com/50373485/208442350-cfe9b4b1-2a5c-4396-9bb0-af80745c2106.png)

### Lanzar el proyecto
Con Pytest Html he añadido una funcionalidad para que cada vez que se ejecute un test se genere un archivo html que se puede abrir con Chrome o Firefox para ver el resultado de los test. Y en caso de que un test hubiese fallado podríamos ver el punto exacto y el motivo detallado.

![html](https://user-images.githubusercontent.com/50373485/208444724-eebca571-0e93-47d3-89c0-883d2a446a3e.jpg)
- test_end2end.py
  - Para lanzar "test_end2end.py" debemos tener abierto el proyecto y en el ternimal escribimos `pytest .\test_end2end.py  --html=Reporte_end2end` y se lanzará el test. Cuando finalice tendremos un reporte en el terminal y también se creará un archivo html llamado "Reporte_end2end". Además tendremos otra evidencia, un Screenshot que se guardará en la carpeta "Screenshots" llamado "welcome.png"
  - Otra opción para lanzar "test_end2end.py" es hacer click en el botón verde de RUN en Pycharm con el test seleccionado, pero no obtendremos el html de resultados
  - ¿Que hace exactamente este test? 
    - Abrimos el navegador en la ventana de Login
    - Vamos a Sign Up
    - Rellenamos todos los datos requeridos (algunos de ellos erróneos)
    - Hacemos click en el botón de Sign Up, comprobamos que está bloqueado
    - Corregimos los datos erróneos y creamos usuario
- test_alerts.py
  - Para lanzar "test_alerts.py" debemos tener abierto el proyecto y en el ternimal escribimos `pytest .\test_alerts.py  --html=Reporte_alerts` y se lanzará el test. Cuando finalice tendremos un reporte en el terminal y también se creará un archivo html llamado "Reporte_alerts". 
  - Otra opción para lanzar "test_alerts.py" es hacer click en el botón verde de RUN en Pycharm con el test seleccionado, pero no obtendremos el html de resultados
  - ¿Que hace exactamente este test? 
    - Abrimos el navegador en la ventana de Login
    - Vamos a Sign Up
    - Rellenamos el input de Username con un usuario ya exitente y comprobamos que el texto de advertencia es correcto
    - Rellenamos el input de Password con una contraseña demasiado simple y comprobamos que el texto de advertencia es correcto
    - Rellenamos el segundo input de Password con una contraseña distinta a la primera contraseña y comprobamos que el texto de advertencia es correcto


 

