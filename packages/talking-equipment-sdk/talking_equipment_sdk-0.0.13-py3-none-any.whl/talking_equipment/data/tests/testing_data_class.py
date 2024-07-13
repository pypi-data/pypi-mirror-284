import uuid
from enum import Enum

from ..control.entities import ControlData
from ..counter.entities import CounterData
from ..current.entities import CurrentData, ThreePhaseCurrentDataContainer
from ..frequency.entities import FrequencyData, ThreePhaseFrequencyDataContainer
from ..power_factor.entities import PowerFactorData, ThreePhasePowerFactorDataContainer
from ..power_meter.entities import ThreePhasePowerMeterDataContainer, SinglePhasePowerMeterDataContainer
from ..temperature.entities import TemperatureData
from ..vibration.entities import VibrationData
from ..voltage.entities import VoltageData, ThreePhaseVoltageDataContainer
from ..volt_amps.entities import VoltAmpsData, ThreePhaseVoltAmpsDataContainer, VoltAmpsReactiveData, \
    ThreePhaseVoltAmpsReactiveDataContainer
from ..watts.entities import WattsData, ThreePhaseWattsDataContainer


class TestDataClass(Enum):
    # All Choices on this Enum should directly match the one in the choices.py file
    CONTROL = ('086f60a0-6761-4d41-b02c-be2d7c0fefe8', ControlData)
    COUNTER = ('55ea4d27-44ce-40f4-9fad-974cdff8c44d', CounterData)
    CURRENT = ('1c4f54b0-27f9-454b-ae19-ced402a89b18', CurrentData)
    FREQUENCY = ('284175d0-1370-4010-b523-402e26cdaca8', FrequencyData)
    POWER_FACTOR = ('4f85bc4f-d2d4-4852-a0b9-74bcc0de91c1', PowerFactorData)
    SINGLE_PHASE_POWER_METER = ('8f03cfa2-c9d7-4b38-9ec0-382b80da14be', SinglePhasePowerMeterDataContainer)
    TEMPERATURE = ('3434bab0-5d50-44a4-b30e-2341de3e4cad', TemperatureData)
    THREE_PHASE_CURRENT = ('8ca6bbea-52e8-4d16-9933-1989f92c8796', ThreePhaseCurrentDataContainer)
    THREE_PHASE_FREQUENCY = ('570b1cde-fdaf-40f6-9dd8-f11ea87f28ee', ThreePhaseFrequencyDataContainer)
    THREE_PHASE_POWER_METER = ('2c216bb6-bbd2-40d4-80a2-53ceebe94056', ThreePhasePowerMeterDataContainer)
    THREE_PHASE_POWER_FACTOR = ('4b1707fb-154b-45e6-808a-6939b800392a', ThreePhasePowerFactorDataContainer)
    THREE_PHASE_VOLT_AMPS = ('0e73f51c-3c68-4af9-872f-32cb1e74eec2', ThreePhaseVoltAmpsDataContainer)
    THREE_PHASE_VOLT_AMPS_REACTIVE = ('6c676e43-7229-4373-8e49-88b0d5023e41', ThreePhaseVoltAmpsReactiveDataContainer)
    THREE_PHASE_VOLTAGE = ('5085752b-7ec7-49d2-8d34-b78ecaba047f', ThreePhaseVoltageDataContainer)
    THREE_PHASE_WATTS = ('42c26719-0974-45d9-8aab-696d896bd6f0', ThreePhaseWattsDataContainer)
    VIBRATION = ('317e5126-e548-4c21-ba91-b1000c6204da', VibrationData)
    VOLT_AMPS = ('090eaece-d748-405c-814a-b0a20fb93998', VoltAmpsData)
    VOLT_AMPS_REACTIVE = ('4e3c4b23-535b-42b7-934d-15ce983afbed', VoltAmpsReactiveData)
    VOLTAGE = ('2895cba9-f6bd-4889-9b2e-d00a1160fdbb', VoltageData)
    WATTS = ('21334e72-e17b-4c0e-a913-a4b9672e64fd', WattsData)

    @classmethod
    def from_key(cls, key: uuid.UUID):
        for data_enum in cls:
            if data_enum.CLASS_KEY == str(key):
                return data_enum
        raise ValueError("Key not found in DataClass enum")

    @classmethod
    def from_class(cls, data_class):
        for data_enum in cls:
            if data_enum.CLASS == data_class.__class__:
                return data_enum
        raise ValueError("Class not found in DataClass enum")

    @property
    def CLASS(self):
        return self._value_[1]

    @property
    def CLASS_KEY(self):
        return self._value_[0]