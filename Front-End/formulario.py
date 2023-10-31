import streamlit as st

from firebase import firebase # Firebase

firebase_instance = firebase.FirebaseApplication("LINK_BD", None)

st.title("Formulario de Registro")

id = st.text_input("ID")
# Recopila el nombre del usuario
nombre = st.text_input("Nombre")

st.title("Tipo de Credencial")

opciones = ["A", "B", "C"]

credential = st.selectbox("Credencial", opciones)

st.write(f"Seleccionaste la opción: {credential}")

# Recopila el apellido del usuario
apellido = st.text_input("Apellido")

# Recopila la edad del usuario
age = st.number_input("Edad", min_value=0, max_value=100)
#result = f"ID: {id}, Credential: {credential}, Name: {nombre}, Last Name: {apellido}, Age: {age}"

result = {
    "id": id,
    "credential": credential,
    "name": nombre,
    "last_name": apellido,
    "age": age
}

# Botón para enviar el formulario
if st.button("Registrar"):
    if nombre and apellido and age:
        st.success(f"Registro exitoso: Nombre: {nombre}, Apellido: {apellido}, Edad: {age}")
        tmp_post_user = firebase_instance.post("/data/users/", result)

    else:
        st.error("Por favor, complete todos los campos.")

st.title("Formulario de eliminacion de usuarios")

id_to_delete = st.text_input("ID to delete")
if st.button("Eliminar"):
    tmp_u = "/data/users"
    d_u = firebase_instance.delete(tmp_u,id_to_delete)
    st.success("Eliminado")



