from typing import Union

from pydantic import BaseModel, Field

"""data transfer object, для сериализации"""


class TransferData(BaseModel):
    """указывает pydantic на необходимость преобразования не dict объектов в json"""

    class Config:
        from_attributes = True


class CargoId(TransferData):
    id: int = Field(gt=0, description='может быть только положительным целым числом')


class CargoBase(TransferData):
    name: str = Field(min_length=5, max_length=70, description='must be greater than 5, but less then 70 letters')
    type: int = Field(ge=1, le=3, description='must be between 1 and 3 inclusive')

    weight: float = Field(gt=0, description='must be greater than 0')
    cargo_cost: float = Field(ge=1, description='must be greater than 1 inclusive')


class RegisterCargo(CargoBase):
    type: int = Field(ge=1, le=3, description='must be between 1 and 3 inclusive')
    session_id: int = Field(ge=0, description='может быть только положительным целым числом')


class CargoType(TransferData):
    id: int = Field(gt=0, le=3, description='всего 3 типа груза')
    name: str


class CargoTypes(TransferData):
    cargo_types: list[CargoType]


class ShowCargo(RegisterCargo, CargoId):
    delivery_cost: Union[float, str]


class CargoWithoutDeliveryPrice(CargoBase):
    delivery_cost: str = 'Не рассчитано'


class Cargos(TransferData):
    cargos: list[ShowCargo]


class CargoFilter(TransferData):
    page: int = Field(1, gt=0, description='только целое число больлше 0'),
    per_page: int = Field(10, gt=0, le=100, description='только целое число от 1 до 100'),
    cargo_type: Union[int, list[int]] = Field(None, description='целое число, или массив целых чисел от 1 до 3'),
    delivery_cost_calculated: bool = Field(None, description='Только булевое значение')


class DeliveryData(CargoId):
    company_id: int = Field(gt=0, description='только положительное, целое число')
