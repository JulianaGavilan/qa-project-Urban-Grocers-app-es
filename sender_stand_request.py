
import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_client_kit(kit_body):
    create_user = post_new_user(data.user_body)
    token = create_user.json()['authToken']
    headers = {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT,
                         json=kit_body,
                         headers=data.headers)  # Pasa los encabezados con el token
