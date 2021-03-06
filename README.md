<!--
# tet-lab1
First laboratory in "T贸picos Especiales en Telem谩tica" course. EAFIT 2021-2.
-->

# Laboratorio #1 (Aplicaci贸n Distribuida en Sockets TCP/UDP)

## Condiciones del reto 馃搱

**1.** Defina cualquier tipo de aplicaci贸n sencilla distribuida que desee dise帽ar e implementar (ej. calculadora distribuida, chat, CRUD, etc).
**2.** Utilizar Sockets TCP o UDP en cualquier lenguaje de programaci贸n de su preferencia.
**3.** Defina, dise帽e e implemente el protocolo de aplicaci贸n que requiera para implementar dicha aplicaci贸n.
**4.** Realice inicialmente todos los supuestos que requiera respecto a tipo de sistema: C/S o P2P, tipo de arquitectura, y aplique algunos de los conceptos fundamentales de los sistemas distribuidos que se ver谩n en esta Lectura: Introducci贸n a Sistemas Distribuidos.
**5.** Implem茅ntela en AWS Educate. Con el fin de probar la funcionalidad del sistema, se requiere que al menos instancie 3 m谩quinas EC2.

## Soluci贸n 馃懆鈥嶐煍?

Para este reto decidimos dise帽ar una **calculadora de tasas de inter茅s** de acuerdo con nuestros conocimientos adquiridos en el curso de *Ingenier铆a Econ贸mica* y que quer铆amos darle un valor agregado a este laboratorio.

Por facilidad y conocimientos previos de todos los participantes, decidimos usar **Python** como lenguaje general de la pr谩ctica a煤n conociendo la heterogeneidad de los sistemas distribuidos. Con este se ver谩n las implementaciones de las m谩quinas y los sockets utilizados.

La arquitectura de esta aplicaci贸n es **orientada a servicios (SOA)**, donde tenemos un servicio de conversi贸n de tasas de inter茅s manejado por un servidor y otro servicio de generaci贸n de tabla de pagos manejado por otro servidor. En este tipo de arquitectura llamamos a esos servicios los *proveedores* y al cliente al que nos conectaremos para usarlos el *consumidor*.

<!--[DIAGRAMA DE ARQUITECTURA EN AWS]-->

### Explicaci贸n de los sockets

Los sockets usados vienen de una implementaci贸n de la librer铆a `socket` de Python. La documentaci贸n consultada para usarlos la encontramos en [1].

Su comunicaci贸n se da por TCP dada la priorizaci贸n que le damos a que sea orientado a la conexi贸n pues se necesitan respuestas a las solicitudes del usuario (m谩s all谩 de que sean inmediatas) y son sockets no bloqueantes.

### Manejo de la concurrencia

Para permitir m煤ltiples usuarios en la aplicaci贸n decidimos usar hilos con la librer铆a `threading` de Python. Gracias a [este archivo](https://github.com/ST0263/st0263-20212/blob/main/LabSocketsMultiThread/ServerLab.py) que proporcion贸 el profesor pudimos orientarnos en la creaci贸n de los hilos en Python y desarrollar nuestra aplicaci贸n c贸modamente.

### Gu铆a de uso

Para conectarnos al cliente o consumidor de servicios necesitaremos acceder a la m谩quina EC2 correspondiente y ejecutar:

```bash
python3 client.py
```

Se podr谩 ver la siguiente interfaz:

![image](https://user-images.githubusercontent.com/52968530/129671118-07755708-ff60-4019-862f-1f4fbcc26a0e.png)


### C贸mo convertir tasas de inter茅s

Se escoge la opci贸n 1 del men煤 y se empiezan a agregar los datos interactivamente.

![image](https://user-images.githubusercontent.com/52968530/129674277-8c46cf55-792e-4950-a480-efdc4e342990.png)

**Datos necesarios.** Tipo de tasa inicial y valor, tipo de tasa final y valor.

Los tipos v谩lidos de momento son:
- Tasa efectiva mensual o mes vencido (E.M)
- Tasa efectiva anual (E.A)
- Tasa nominal mes vencido (N.M.V)
- Tasa nominal a帽o vencido (N.A.V)

Al final se obtendr谩 una respuesta y con cualquier tecla podremos regresar al men煤 principal.

### C贸mo generar tabla de pagos

Se escoge la opci贸n 2 del men煤 y se empiean a agregar los datos interactivamente.

![image](https://user-images.githubusercontent.com/52968530/129674444-a7b22455-0911-42ee-8cfa-51840e407b95.png)

**Datos necesarios.** Capital inicial, tasa de inter茅s efectiva mensual (E.M), cantidad de cuotas.

Al final se obtendr谩 una respuesta y con cualquier tecla podremos regresar al men煤 principal.

## Participantes

- David Calle Gonz谩lez <a href="https://github.com/dcalleg707"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Juan Sebasti谩n D铆az Osorio <a href="https://github.com/juansedo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Santiago Hidalgo Ocampo <a href="https://github.com/sanhidalgoo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>

## Referencias
[1] Python Software Foundation (2021, Aug 16). Socket Programming HOW TO. [Online] Disponible en [este enlace](https://docs.python.org/3/howto/sockets.html).
