import pika
import getpass
from firebase import firebase
from datetime import datetime

# Data to connect
data_base_link = "LINK_DB"
ip_to_connect = "IP_HERE"

# Instancia del objeto firebase
firebase_instance = firebase.FirebaseApplication(data_base_link, None)

# Instancia del RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(ip_to_connect)) #Creación de la conexion
channel = connection.channel() #Creación del canal
channel.queue_declare(queue='hello') #Creación de la cola

def info(flag, message):
	if(flag == 0): print(f" [x] Enviado '{message}'")

def status_alarm():
	# Obtener los valores
	g_ah = firebase_instance.get("/data/alarm-history","")

	# Convierte el diccionario anidado en una lista de diccionarios
	tmp_status = [{'key': k, **v} for k, v in g_ah.items()]

	# Obtener el último valor de la alarma
	last_status_alarm = int(tmp_status[-1]['status'])

	return last_status_alarm

def log_data(id, level, status, flag):
	# level: Bajo, Normal, Critico | date: Fecha actual | user_id: Id usuario de data_user
	data_log = {"level":str(level),"date":str(datetime.now()), "user_id":str(id)}

	# status: 0, 1 | date: Fecha actual | user_id: Id usurio de data user
	data_history = {"status":str(status),"date":str(datetime.now()),"user_id":str(id)}

	if(flag == 0):
		tmp_post_gl = firebase_instance.post("/data/general-log", data_log)
		tmp_alarm_h = firebase_instance.post("/data/alarm-history", data_history)
	elif(flag == 1):
		tmp_post_gl = firebase_instance.post("/data/general-log", data_log)

def buscar_id(id):
	flag = 0
	g = firebase_instance.get("/data/users","")
	for key, inner_dict in g.items():
		for inner_key, value in inner_dict.items():
			if(inner_key == "id" and value == id):
				flag = 1

	#print(inner_dict)

	status = status_alarm()
	# Usuario valido
	if(flag == 1):
		print("[O] Usuario valido")

		if(status == 0):
			print("[O] Alarma encendida")
			log_data(id, "Baja", "1", 0)

		elif(status == 1):
			print("[X] Alarma apagada")
			log_data(id, "Normal", "0", 0)

		return [inner_dict, status]
	
	# Usuario no valido
	elif(flag == 0):
		print("[X] Usuario NO valido")
		log_data(id, "Critica", "", 1)		

		return ["", ""]

# Función main
if __name__ == '__main__':
	while(True):
		#id = str(input("[O] Lectura del NCF: "))
		id = str(getpass.getpass("[O] Lectura del NCF: "))
		message = buscar_id(id)
		#channel.basic_publish(exchange='', routing_key='hello', body=str(message)) #Envio del mensake
		channel.basic_publish(exchange='', routing_key='hello', body=str(message[1])) #Envio del mensake
		#info(0, message)
	connection.close()