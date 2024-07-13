from dataclasses import dataclass

from ..entities import Data, DataContainer
from ..mixins import UnitConversionMixin
from ..enums import DataValueType


@dataclass
class CurrentData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit: str = 'Amps'
    unit_abbreviation: str = 'A'


@dataclass
class ThreePhaseCurrentDataContainer(DataContainer):
    a: CurrentData = ...
    b: CurrentData = ...
    c: CurrentData = ...

    value_type: DataValueType = DataValueType.JSON

