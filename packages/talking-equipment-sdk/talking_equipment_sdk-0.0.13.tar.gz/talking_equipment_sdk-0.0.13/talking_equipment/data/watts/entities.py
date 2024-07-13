from dataclasses import dataclass

from ..current.entities import CurrentData
from ..entities import Data, DataContainer
from ..enums import DataValueType
from ..mixins import UnitConversionMixin
from ..voltage.entities import VoltageData


@dataclass
class WattsData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit: str = 'Watts'
    unit_abbreviation: str = 'W'

    def to_voltage(self, current: CurrentData) -> float:
        return self.value / current.value

    def to_current(self, voltage: VoltageData) -> float:
        return self.value / voltage.value

    def set_from_voltage_and_current(self, voltage: VoltageData, current: CurrentData):
        self.value = voltage.value * current.value


@dataclass
class ThreePhaseWattsDataContainer(DataContainer):
    a: WattsData = ...
    b: WattsData = ...
    c: WattsData = ...

    value_type: DataValueType = DataValueType.JSON



@dataclass
class WattHoursData(WattsData):
    unit: str = 'Watt Hours'
    unit_abbreviation: str = 'Wh'
