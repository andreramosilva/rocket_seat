from cerberus import Validator


def registry_order_validator(body: any) -> dict:
    body_validator = Validator({
        "data": 
            {"type": "dict", 
            "schema": {
                "name": {"type": "string", "required": True},
                "adress": {"type": "string", "required": True},
                "cupom": {"type": "string", "required": True},
                "items": {"type": "list", 
                          "schema":{
                              "items": {"type": "string", "required": True},
                                "quantity": {"type": "integer", "required": True},
                          }, "required": True },
                }
            }
        })
    
    response = body_validator.validate(body)
    if response == False:
        raise Exception(body_validator.errors)

