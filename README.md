# Proyecto Urban Grocers

Presentado por Juliana Gavilan, Sprint 7 

Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. Se han creado varias listas de comprobación,
una de ellas es para el campo name en la solicitud de creación de un kit de productos.

Este proyecto consiste en automatizar las pruebas de la siguiente lista de comprobación, cargando el código en GitHub y enviando el repositorio a revisión.

## **Lista de comprobación de pruebas**

| № |  Description |   ER:|
|---|---|---|
| 1 | El número permitido de caracteres (1): kit_body = { "name": "a"}  | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud  |
| 2 | 	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}  |  Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3 | 	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }  | Código de respuesta: 400  |
| 4 |  	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } |  Código de respuesta: 400 |
| 5 | 	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }  |  Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6 |  	Se permiten espacios: kit_body = { "name": " A Aaa " } |  Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7 | 	Se permiten números: kit_body = { "name": "123" }  | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud  |
| 8 | 	El parámetro no se pasa en la solicitud: kit_body = { }  |  solicitud: kit_body = { }	Código de respuesta: 400  |
| 9 |   	Se ha pasado un ti
po de parámetro diferente (número): kit_body = { "name": 123 }|   solicitud: kit_body = { }	Código de respuesta: 400 |

## Bibliotecas

Antes de iniciar con el proyecto no podemos olvidar instalar las diferentes bibliotecas que nos ayudaran a ejecutar las pruebas estas bibliotecas son

### Request
Para trabajar con solicitudes HTTP en Python, necesitarás el paquet requests. Recuerda que cuentas con dos formas de instalarlo:

1️⃣ Usando "pip", el gestor de paquetes de Python

Abre la terminal o consola.
Ingresa el comando pip install requests.
Recuerda: pip significa administrador de paquetes. En otras palabras, este es un programa para instalar varios paquetes, ya está integrado en Python.

2️⃣ Mediante la pestaña "Python Packages" (Paquetes de Python)

En PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages” (Paquetes de Python).
En la barra de búsqueda, escribe "requests" (solicitudes).
Localiza y selecciona el paquete "requests" de la lista.
Finalmente, haz clic en el botón "Install" (instalar).
### Pytest
Existen dos métodos para instalar Pytest. Elige el que te resulte más conveniente.

1️⃣ Usando el comando "pip" en la terminal:

Abre la terminal o consola

Ingresa el comando _pip install_ pytest pip es el gestor de paquetes de Python. Te permite instalar y gestionar bibliotecas, así como herramientas adicionales.

2️⃣ A través de la interfaz de PyCharm en "Python Packages":

En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
En el campo de búsqueda, introduce "Pytest".
Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".

### Para ejecutar las pruebas en la terminal
Tienes dos opciones para ejecutar tus pruebas: directamente desde la consola de PyCharm o utilizando su interfaz gráfica.

1️⃣ Desde la terminal de PyCharm

Dirígete a la pestaña "Terminal" en la parte inferior de PyCharm. Por defecto, esta terminal se ubica en el directorio de tu proyecto. 

Para ejecutar todas las pruebas de tu proyecto, simplemente escribe:

_**pytest**_

Luego ejecuta las pruebas desde el archivo calc_test.py:

**_pytest Create_kits.py_**
