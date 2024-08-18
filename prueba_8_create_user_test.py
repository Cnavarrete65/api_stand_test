import sender_stand_request
import data
# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def negative_assert_no_first_name(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
      response = sender_stand_request.post_new_user(user_body)
    # Comprueba si la respuesta contiene el código 400
      assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
      assert response.json()["code"] == 400
# Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
      assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_first_name(user_body)

