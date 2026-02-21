def validate_typescript_structure(component):
    code = component["typescript"]
    errors = []

    if "export class" not in code:
        errors.append("Missing export class definition")

    if "@Component" not in code:
        errors.append("Missing @Component decorator")

    if "import" not in code:
        errors.append("Missing import statement")

    if code.count("{") != code.count("}"):
        errors.append("Bracket mismatch")

    return errors