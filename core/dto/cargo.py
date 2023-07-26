from typing import Union

from pydantic import BaseModel, Field
# from pydantic.fields import Optional


class TransferData(BaseModel):
    """указывает pydantic на необходимость преобразования не dict объектов в json"""

    class Config:
        from_attributes = True


class CargoBase(TransferData):
    name: str = Field(min_length=5, max_length=70, description='must be greater than 5, but less then 70 letters')
    type: int = Field(ge=1, le=3, description='must be between 1 and 3 inclusive')

    weight: float = Field(gt=0, description='must be greater than 0')
    cargo_cost: int = Field(ge=1, description='must be greater than 1 inclusive')


class RegisterCargo(CargoBase):
    type: int = Field(ge=1, le=3, description='must be between 1 and 3 inclusive')
    session_id: int


class CargoType(TransferData):
    id: int
    name: str
    session_id: int


class CargoTypes(TransferData):
    cargo_types: list[CargoType]


class ShowCargo(RegisterCargo):
    id: int
    delivery_cost: Union[float, str]


class CargoWithoutDeliveryPrice(CargoBase):
    delivery_cost: str = 'Не рассчитано'


class Cargos(TransferData):
    cargos: list[ShowCargo]


class CargoFilter(TransferData):
    page: int = Field(1, gt=0),
    per_page: int = Field(10, gt=0, le=100),
    cargo_type: Union[int, list[int]] = Field(None),
    delivery_cost_calculated: bool = Field(None)
