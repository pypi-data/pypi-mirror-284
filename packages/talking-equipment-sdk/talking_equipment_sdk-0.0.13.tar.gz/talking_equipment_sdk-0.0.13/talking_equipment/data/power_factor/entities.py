from dataclasses import dataclass

from ..entities import Data, DataContainer
from ..mixins import UnitConversionMixin
from ..volt_amps.entities import VoltAmpsData
from ..watts.entities import WattsData
from ..enums import DataValueType


@dataclass
class PowerFactorData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit: str = 'Power Factor'
    unit_abbreviation: str = 'PF'

    def set_from_watts_and_voltamps(self, watts: WattsData, voltamps: VoltAmpsData):
        self.value = watts.value / voltamps.value


@dataclass
class ThreePhasePowerFactorDataContainer(DataContainer):
    a: PowerFactorData = ...
    b: PowerFactorData = ...
    c: PowerFactorData = ...

    value_type: DataValueType = DataValueType.JSON