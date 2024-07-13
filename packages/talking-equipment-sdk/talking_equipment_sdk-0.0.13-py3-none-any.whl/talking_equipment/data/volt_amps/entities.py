from dataclasses import dataclass

from ..entities import Data, DataContainer
from ..mixins import UnitConversionMixin
from ..enums import DataValueType


@dataclass
class VoltAmpsData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit: str = 'Volt Amps'
    unit_abbreviation: str = 'VA'


@dataclass
class ThreePhaseVoltAmpsDataContainer(DataContainer):
    a: VoltAmpsData = ...
    b: VoltAmpsData = ...
    c: VoltAmpsData = ...

    value_type = DataValueType.JSON


@dataclass
class VoltAmpsReactiveData(VoltAmpsData):
    unit = 'Volt Amps Reactive'
    unit_abbreviation = 'VAR'


@dataclass
class ThreePhaseVoltAmpsReactiveDataContainer(DataContainer):
    a: VoltAmpsReactiveData = ...
    b: VoltAmpsReactiveData = ...
    c: VoltAmpsReactiveData = ...

    value_type = DataValueType.JSON