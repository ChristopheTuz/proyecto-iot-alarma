# Proyecto Alarma de Internet de las Cosas

## ELEMENTOS EN NUESTRO DIAGRAMA
<img width="1037" alt="image" src="https://github.com/ChristopheTuz/proyecto-iot-alarma/assets/60182870/038c80b2-aa72-446d-bd87-373e3d0711ea">

- ### Usuario
Físico

- ### Lector NFC
Físico

- ### Front-End
[formulario.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Front-End/formulario.py)

- ### Verificación de usuarios
código dentro de [alarm_project.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Cliente/alarm_project.py)

- ### Base de datos (No SQL)
Mediante Firebase

- ### Alarma (Simulación)
Código dentro de [alarma.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Server/alarma.py)

---
# CÓDIGO
Contamos con un Cliente y un servidor 

## Cliente [en Python]
[alarm_project.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Cliente/alarm_project.py)

<h5> El código proporciona una implementación para vincular la comunicación entre un servidor RabbitMQ y una base de datos alojada en Firebase. En la construcción de esta solución, se han empleado varias bibliotecas fundamentales. En primer lugar, Pika se utiliza para facilitar la interacción con RabbitMQ, lo que garantiza una transferencia de mensajes confiable y eficiente. Además, se ha incorporado el módulo 'getpass' para garantizar la seguridad en la entrada de contraseñas, lo cual es esencial para salvaguardar la información confidencial del usuario.
La integración con Firebase se logra mediante la utilización de la biblioteca 'firebase'. Esto permite una interacción fluida y sencilla con la base de datos de Firebase, lo que resulta crucial para la gestión de datos en tiempo real y la integración con el ecosistema de la nube de Firebase. Para la manipulación de las marcas de tiempo y la gestión de fechas, se ha empleado la biblioteca 'datetime', lo que garantiza una precisión en el registro de eventos y acciones relacionadas con el tiempo.</h5>

<h5> El script comienza por definir algunas variables esenciales para el funcionamiento del sistema. Entre ellas, 'data_base_link' representa la conexión a la base de datos y 'ip_to_connect' alude a la dirección a la cual se establecerá la conexión. La instancia 'firebase_instance' se crea para facilitar las operaciones de lectura y escritura en la base de datos de Firebase a lo largo del script.
Posteriormente, se establece la conexión con el servidor RabbitMQ, utilizando la dirección IP proporcionada por el servicio. Se crea un canal de comunicación para la transmisión de mensajes y se declara una cola llamada 'Hello' que servirá como punto de encuentro para los mensajes entrantes y salientes.
Durante la ejecución del programa, se solicita al usuario que proporcione su ID, asegurando la privacidad y la seguridad con 'getpass'. La función 'buscar_id' busca este ID en la base de datos correspondiente y, en función de si se encuentra o no, ejecuta una serie de acciones específicas. Si el ID no se encuentra, se notifica al usuario que no está registrado en la base de datos. En el caso de que el ID se encuentre, la función 'status_alarm' se utiliza para obtener el estado actual de la alarma, es decir, si está activada o desactivada. Dependiendo del estado, la función 'info' muestra en pantalla el estado de la alarma y la función 'log_data' registra el nuevo estado en la base de datos.</h5>

## Server [en C#]
[Receive.cs](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Server/Receive/Receive.cs)
<h5> La aplicación C# utiliza la biblioteca RabbitMQ.Client para establecer la conexión con un servidor RabbitMQ local. Se define un objeto 'factory' de la clase 'ConnectionFactory', donde se especifica el nombre del host de conexión, en este caso, "localhost", Luego, se especifica la ruta del script Python que se ejecutará, que se encuentra en la ubicación relativa "../alarma.py", se utiliza la interfaz 'IConnection' para crear la conexión con el servidor RabbitMQ y, dentro de un bloque 'using', se crea un canal de comunicación utilizando 'connection.CreateModel()', se declara una cola llamada "hello" utilizando el método 'QueueDeclare' en el canal recién creado. Los parámetros 'durable', 'exclusive' y 'autoDelete' se establecen en 'false' y 'arguments' se establece en 'null', se define un consumidor de eventos ('consumer') utilizando la clase 'EventingBasicConsumer' y se suscribe al evento 'Received'. Cuando se recibe un mensaje, se decodifica y se comprueba su contenido.
Si el mensaje no está vacío, se realiza una verificación adicional. Si el mensaje es "1", se muestra el mensaje "Alarma desactivada" y se inicia el script Python utilizando el método 'Process.Start("python", scriptPath)'. En caso contrario, se muestra "Alarma activada" y también se inicia el script Python.Si el mensaje está vacío, se imprime "Error: Usuario no válido", la aplicación C# consume los mensajes de la cola "hello" utilizando el método 'BasicConsume' y, después de iniciar el proceso de escucha, muestra "Listening..." en la consola. la aplicación espera a que el usuario presione cualquier tecla para salir. Una vez que se presiona una tecla, la aplicación se detiene y sale del bucle.
</h5>

### RabbitMQ 
Describir su interacción

---

# REQUERIMIENTOS

### Rabbit
[Sitio oficial](https://www.rabbitmq.com/download.html)
Recomendación de uso:
<code>docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management</code>
En caso de utilizar la instalación mediante docker es necesario instalar docker.

### Dockers
Verificar documentación [Sitio oficial](https://docs.docker.com/engine/install/)

### Librerias en Python
<code>
python: 3.9.7
pip: 23.2.1
import streamlit as st: 1.27.2
from firebase import firebase: 3.0.1
import pika: 1.3.2
import getpass
from datetime import datetime
import tkinter as tk
</code>

### Librerias en C#
<code>using System.Text;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Diagnostics;
</code>
