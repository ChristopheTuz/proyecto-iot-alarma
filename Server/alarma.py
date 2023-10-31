from firebase import firebase
import tkinter as tk

data_base_link = "LINK_DB"

# Instancia del objeto firebase
firebase_instance = firebase.FirebaseApplication(data_base_link, None)

def status_alarm():
    # Obtener los valores
    g_ah = firebase_instance.get("/data/alarm-history", "")

    # Convierte el diccionario anidado en una lista de diccionarios
    tmp_status = [{'key': k, **v} for k, v in g_ah.items()]

    # Obtener el último valor de la alarma
    last_status_alarm = int(tmp_status[-1]['status'])

    return last_status_alarm

def update_color():
    s = status_alarm()
    if s == 1:
        root.configure(background='green')
        label.config(text="Alarma activada", fg="green")
    elif s == 0:
        root.configure(background='red')
        label.config(text="Alarma desactivada", fg="red")
    root.after(1000, update_color)

def close_window():
    root.quit()

root = tk.Tk()
root.geometry("400x100")

label = tk.Label(root, font=("Arial", 20))
label.pack(fill="both", expand=1)

update_color()

# Cierra la ventana después de 5 segundos (5000 ms)
root.after(3000, close_window)

root.mainloop()
