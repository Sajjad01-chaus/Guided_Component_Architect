from pydantic import BaseModel, ValidationError

class ComponentSchema(BaseModel):
    typescript: str
    html: str
    css: str

def validate_schema(component):
    try:
        ComponentSchema(**component)
        return []
    except ValidationError as e:
        return [str(e)]