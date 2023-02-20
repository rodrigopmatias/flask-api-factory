from pydantic import BaseModel, condate, constr


class PetTypeSerializer(BaseModel):
    id: str | None = None
    name: constr(min_length=0, max_length=30)

    class Config:
        orm_mode = True


class OwnerSerializer(BaseModel):
    id: str | None = None
    name: constr(min_length=0, max_length=50)
    phone_number: constr(min_length=0, max_length=12)

    class Config:
        orm_mode = True


class PetSerializer(BaseModel):
    id: str | None = None
    owner_id: constr(min_length=36, max_length=36)
    pet_type_id: constr(min_length=36, max_length=36)

    name: constr(min_length=0, max_length=50)
    sex: constr(min_length=1, max_length=1, regex="^(M|F|I)$")
    born_date: condate()

    class Config:
        orm_mode = True
