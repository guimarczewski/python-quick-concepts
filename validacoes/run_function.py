from cerberus import Validator

def validate_body(body):

    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "idade": { "type": "integer", "required": True, "empty": False},
                "altura": { "type": "float", "required": False, "empty": False},
                "nome": { "type": "string", "required": True, "empty": False},
                "documento": { "type": "string", "required": False, "empty": True}
            }
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)

    print('Ok')


input = {
    "data": {
        "idade":27,
        "altura":1.75,
        "nome": "Guilherme Marczewski",
        "documento": ""
    }
}

validate_body(input)