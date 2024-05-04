from pydantic import BaseModel


class RunDTO(BaseModel):
    path: str
    inputs: list


def validate(DTO, obj):
    try:
        return DTO(**obj).model_dump(), None
    except Exception as e:
        return None, {"ValidatorError": str(e)}
