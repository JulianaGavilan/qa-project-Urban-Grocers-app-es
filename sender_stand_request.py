
import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
authToken=response.json()
print(response.status_code)
print(response.json())

def post_new_kit():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT,
                         headers=data.headers + data.Authorization + {authToken})
response = post_new_kit()
print(response.status_code)