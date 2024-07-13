from dataclasses import dataclass

from ..entities import Data, DataContainer
from ..mixins import UnitConversionMixin
from ..enums import DataValueType


@dataclass
class FrequencyData(Data, UnitConversionMixin):
    value: float
    value_type: DataValueType = DataValueType.FLOAT
    unit: str = 'Hertz'
    unit_abbreviation: str = 'Hz'


@dataclass
class ThreePhaseFrequencyDataContainer(DataContainer):
    a: FrequencyData = ...
    b: FrequencyData = ...
    c: FrequencyData = ...

    value_type: DataValueType = DataValueType.JSON