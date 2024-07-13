from dataclasses import dataclass
from enum import Enum

from ..entities import Data
from ..enums import DataValueType


class TemperatureType(Enum):
    CELSIUS = 1
    FAHRENHEIT = 0


@dataclass
class TemperatureData(Data):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit_name: str = 'Temperature'
    unit_abbreviation: str = 'TEMP'

    type: TemperatureType = TemperatureType.CELSIUS

    @property
    def celsius(self) -> float:
        if self.type == TemperatureType.FAHRENHEIT:
            return (self.value - 32) * 5 / 9
        elif self.type == TemperatureType.CELSIUS:
            return self.value

    @property
    def fahrenheit(self) -> float:
        if self.type == TemperatureType.CELSIUS:
            return self.value * 9 / 5 + 32
        elif self.type == TemperatureType.FAHRENHEIT:
            return self.value

