from dataclasses import dataclass

from ..entities import Data
from ..enums import DataValueType


@dataclass
class CounterData(Data):
    value: int
    value_type: DataValueType = DataValueType.INT
    unit: str = 'Count'
    unit_abbreviation: str = 'CNT'