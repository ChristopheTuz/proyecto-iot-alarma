# Proyecto Alarma de Internet de las Cosas

## ELEMENTOS EN NUESTRO DIAGRAMA
<img width="1037" alt="image" src="https://github.com/ChristopheTuz/proyecto-iot-alarma/assets/60182870/038c80b2-aa72-446d-bd87-373e3d0711ea">

### Usuario
Físico

### Lector NFC
Físico

### Front-End
[formulario.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Front-End/formulario.py)
### Verificación de usuarios
código dentro de [alarm_project.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Cliente/alarm_project.py)


### Base de datos (No SQL)
Mediante Firebase

### Alarma (Simulación)
Código dentro de [alarma.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Server/alarma.py)

---
# CÓDIGO
Contamos con un Cliente y un servidor 

## Cliente [en Python]
[alarm_project.py](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Cliente/alarm_project.py)
Describir

## Server [en C#]
[Receive.cs](https://github.com/ChristopheTuz/proyecto-iot-alarma/blob/main/Server/Receive/Receive.cs)
Describir

### RabbitMQ 
Describir su interacción


# REQUERIMIENTOS

### Rabbit
[Sitio oficial](https://www.rabbitmq.com/download.html)
Recomendación de uso:
<code>docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management</code>
En caso de utilizar la instalación mediante docker es necesario instalar docker.

### Dockers
Verificar documentación [Sitio oficial](https://docs.docker.com/engine/install/)

### Librerias en Python
<code>import streamlit as st
from firebase import firebase # Firebase
import pika
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
