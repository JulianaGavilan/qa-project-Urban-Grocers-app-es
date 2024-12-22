import sender_stand_request
import data

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_name

#Pruebas negativas: Preparación
def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
# prueba 8  kit_body vacio
def negative_assert_no_name(kit_body):
        response = sender_stand_request.post_new_client_kit(kit_body)

        assert response.status_code == 400

# Prueba 1 	El número permitido de caracteres (1)
def test_1_create_kit_with_1_letter():
    positive_assert(data.kit_body_1)

# Prueba 2	El número permitido de caracteres (511)
def test_2_create_kit_with_511_letters():
    positive_assert(data.Kit_body_2)

#Prueba 3. El número de caracteres es menor que la cantidad permitida (0):
def test_3_create_with_nothing():
    negative_assert(data.Kit_body_3)

#Prueba 4. El número de caracteres es mayor que la cantidad permitida (512):
def test_4_create_with_512_letters():
    negative_assert(data.Kit_body_4)

#Prueba 5. Se permiten caracteres especiales:
def test_5_create_with_special_caracters():
    positive_assert(data.Kit_body_5)

# Prueba 6. Se permiten espacios:
def test_6_create_with_space():
    positive_assert(data.Kit_body_6)

#Prueba 7. Se permiten números:
def test_7_create_with_numbers():
    positive_assert(data.Kit_body_7)

#Prueba 8. El parámetro no se pasa en la solicitud:
def test_8_create_with_error_parameter():
    kit_body=data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)

#Prueba 8. El parámetro no se pasa en la solicitud:
def test_9_create_number_with_error():
    kit_body=get_kit_body(data.Kit_Body_9)
    response=sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
