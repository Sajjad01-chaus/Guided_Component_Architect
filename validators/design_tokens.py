import re

def validate_tokens(component, design_system):
    errors = []
    combined = " ".join(component.values())

    allowed = set(design_system["colors"].values())
    detected = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", combined)

    for color in detected:
        if color not in allowed:
            errors.append(f"Unauthorized color: {color}")

    if design_system["borderRadius"] not in combined:
        errors.append("Missing borderRadius token")

    if design_system["fontFamily"] not in combined:
        errors.append("Missing fontFamily token")

    return errors