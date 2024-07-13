from dataclasses import dataclass

from ..entities import Data, DataContainer
from ..enums import DataValueType
from ..mixins import UnitConversionMixin


@dataclass
class VoltageData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit_name: str = 'Volts'
    unit_abbreviation: str = 'V'

    def __str__(self):
        return self.auto_scale_verbose


@dataclass
class ThreePhaseVoltageDataContainer(DataContainer):
    a: VoltageData = ...
    b: VoltageData = ...
    c: VoltageData = ...

    def average(self) -> float:
        return (self.a.value + self.b.value + self.c.value) / 3
