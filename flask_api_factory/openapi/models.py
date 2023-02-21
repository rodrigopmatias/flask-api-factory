from pydantic import BaseModel, Field


def _translate_field_name(name_map: dict[str, str]):
    def _translate(field_name):
        return name_map.get(field_name, field_name)

    return _translate


class APIServer(BaseModel):
    url: str
    description: str


class APIContact(BaseModel):
    name: str
    url: str
    email: str


class APILicense(BaseModel):
    name: str
    url: str


class APIDescription(BaseModel):
    title: str
    summary: str
    termOfService: str
    version: str
    contact: APIContact
    license: APILicense
    servers: list[APIServer] = []

    class Config:
        alias_generator = _translate_field_name({"termOfService": "term_of_service"})
        allow_population_by_field_name = True


class APIDoc(BaseModel):
    desciption: APIDescription
