from validator_collection import validators, checkers, errors

def validate(data: dict, schema_class) -> list:
    errors = []
    if not isinstance(data, dict):
        return ["Invalid request body"]
    
    required_fields = {'session_id': str, 'auth_code': str, 'csrf_token': str}
    for field, field_type in required_fields.items():
        if field not in data or not data[field]:
            errors.append(f"The field '{field}' is required.")
        elif not isinstance(data[field], field_type):
            errors.append(f"The field '{field}' must be a {field_type.__name__}.")
    return errors