"""
  Copyright 2023 abnoname
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you 05_may not use this file except in compliance with the License.
  You 05_may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import open3e.Open3Ecodecs
from open3e.Open3Ecodecs import *

# Datapoints sourced from ViGuide Demo Mode:
# https://viguide.viessmann.com/installations/10000017?gatewaySerial=7736170-gw-serial-17&deviceSerial=7720533-device-serial

dataIdentifiers = {
    "name": "general", 
    "dids" : 
    {
        256 : O3EComplexType(36, "BusIdentification", [O3EByteVal(1, "BusAddress"), O3EEnum(1, "BusType", "BusTypes"), O3EEnum(1, "DeviceProperty","Devices"), O3EEnum(1, "DeviceFunction","Devices"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")]),
        257 : O3EList(122, "StatusDtcList", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"State","States"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        258 : O3EList(122, "StatusDtcHistory", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"State","States"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        259 : O3EList(122, "InfoDtcList", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Info","Infos"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        260 : O3EList(122, "InfoDtcHistory", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Info","Infos"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        261 : O3EList(122, "ServiceDtcList", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Service","Services"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        262 : O3EList(122, "ServiceDtcHistory", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Service","Services"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        263 : O3EList(122, "WarningDtcList", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Warning","Warnings"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        264 : O3EList(124, "WarningDtcHistory", [O3EByteVal(2, "Count"), O3EByteVal(2, "GrandTotal"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Warning","Warnings"), O3EDateTime(8, "DateTime"),O3EByteVal(2, "Unknown")] )]),
        265 : O3EList(122, "ErrorDtcList", [O3EByteVal(2, "Count"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Error","Errors"), O3EDateTime(8, "DateTime"), O3EByteVal(2, "Unknown")] )]),
        266 : O3EList(124, "ErrorDtcHistory", [O3EByteVal(2, "Count"), O3EByteVal(2, "GrandTotal"), O3EComplexType(12, "ListEntries",[O3EEnum(2,"Error","Errors"), O3EDateTime(8, "DateTime"), O3EByteVal(2, "Unknown")] )]),         
        268 : O3EComplexType(9, "FlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        269 : O3EComplexType(9, "ReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        271 : O3EComplexType(9, "DomesticHotWaterSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        272 : RawCodec(10, "DomesticHotWaterFlowSensor"),
        273 : O3EComplexType(9, "SolarRoofTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        274 : O3EComplexType(9, "OutsideTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        #Vitodens 300-W: 274 : O3EComplexType(9, "OutsideTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Average", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EByteVal(1, "Unknown")]),
        275 : O3EComplexType(9, "SolarBottomTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        277 : O3EComplexType(9, "BufferBottomTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        278 : O3EComplexType(9, "BufferMidBottomTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        279 : O3EComplexType(9, "BufferMidTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        281 : O3EComplexType(9, "BufferTopTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        282 : O3EComplexType(9, "HydraulicSeparatorTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        283 : O3EComplexType(9, "HydraulicSeparatorReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        284 : O3EComplexType(9, "MixerOneCircuitFlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        285 : O3EComplexType(9, "MixerOneCircuitReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        286 : O3EComplexType(9, "MixerTwoCircuitFlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        287 : O3EComplexType(9, "MixerTwoCircuitReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        288 : O3EComplexType(9, "MixerThreeCircuitFlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        289 : O3EComplexType(9, "MixerThreeCircuitReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        290 : O3EComplexType(9, "MixerFourCircuitFlowTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        291 : O3EComplexType(9, "MixerFourCircuitReturnTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        318 : O3EComplexType(9, "WaterPressureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        320 : O3EComplexType(9, "PrimaryHeatExchangerLiquidTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        321 : O3EComplexType(9, "CompressorInletTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        322 : O3EComplexType(9, "CompressorInletPressureSensor", [O3EInt16(2, "Actual", scale = 100), O3EInt16(2, "Minimum", scale = 100), O3EInt16(2, "Maximum", scale = 100), O3EInt16(2, "Average", scale = 100), O3EByteVal(1, "Unknown")]),
        324 : O3EComplexType(9, "CompressorOutletTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        325 : O3EComplexType(9, "CompressorOutletPressureSensor", [O3EInt16(2, "Actual", scale = 100), O3EInt16(2, "Minimum", scale = 100), O3EInt16(2, "Maximum", scale = 100), O3EInt16(2, "Average", scale = 100), O3EByteVal(1, "Unknown")]),
        327 : O3EComplexType(9, "OutdoorAirTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        328 : O3EComplexType(9, "SupplyAirTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        329 : O3EComplexType(9, "ExtractAirTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        330 : O3EComplexType(9, "ExhaustAirTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        331 : O3EComplexType(9, "FlueGasTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        323 : RawCodec(9, "EnhancedVapourInjectionTemperatureSensor"),
        334 : O3EComplexType(9, "MixerOneCircuitRoomTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        335 : O3EComplexType(9, "MixerTwoCircuitRoomTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        336 : O3EComplexType(9, "MixerThreeCircuitRoomTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        337 : O3EComplexType(9, "MixerFourCircuitRoomTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        354 : O3EByteVal(1, "PrimaryHeatExchangerBaseHeater"),
        355 : O3EComplexType(9, "SecondaryHeatExchangerLiquidTemperatureSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        360 : O3EComplexType(9, "DomesticHotWaterOutletSensor",[O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        364 : O3EComplexType(6, "Flame", [O3EInt8(1, "Flame"), RawCodec(5, "Unknown")]),
        365 : O3EInt16(42, "FlameStatistical", offset = 38, scale = 1),
        373 : RawCodec(2, "FanTargetSpeed"),
        377 : O3EUtf8(16, "ViessmannIdentificationNumber"),
        378 : O3EComplexType(4, "PointOfCommonCouplingPhaseOne", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        379 : O3EComplexType(4, "PointOfCommonCouplingPhaseTwo", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        380 : O3EComplexType(4, "PointOfCommonCouplingPhaseThree", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        381 : O3EInt8(4, "CentralHeatingPump", offset = 1),
        382 : O3EComplexType(5, "UnitsAndFormats", [O3EEnum(1, "Units", "Units"), O3EEnum(1, "DateFormat", "DateFormats"), O3EEnum(1, "TimeFormat", "TimeFormats"), O3EByteVal(1, "TimeZone"), O3EByteVal(1, "Unknown")]),
        386 : O3EByteVal(1, "DiverterValveTargetPosition"),
        388 : O3EInt8(1, "ElectronicExpansionValveOneTargetPositionPercent"),
        389 : O3EInt8(1, "ElectronicExpansionValveOneCurrentPositionPercent"),
        390 : O3EInt8(1, "ElectronicExpansionValveTwoTargetPositionPercent"),
        391 : O3EInt8(1, "ElectronicExpansionValveTwoCurrentPositionPercent"),
        392 : RawCodec(4, "DomesticHotWaterPump"),
        395 : O3EInt16(2, "CentralHeatingTemperatureSetpoint"),
        396 : O3EInt16(2, "DomesticHotWaterTemperatureSetpoint", signed=True),
        401 : O3EComplexType(5, "MixerOneCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        402 : O3EComplexType(5, "MixerTwoCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        403 : O3EComplexType(5, "MixerThreeCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        404 : O3EComplexType(5, "MixerFourCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        405 : O3EComplexType(5, "MixerFiveCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        406 : O3EComplexType(5, "MixerSixCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        407 : O3EComplexType(5, "MixerSevenCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        408 : O3EComplexType(5, "MixerEightCircuitPump", [O3EByteVal(1, "TargetPowerState"), O3EInt8(1,"TargetValue"), O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState"), O3EInt8(1,"ActualValue")]),
        417 : O3EInt8(5, "SolarCircuitPump"),
        419 : O3EComplexType(5, "OutdoorAirHumiditySensor",[O3EByteVal(1, "Actual"), O3EByteVal(1, "Minimum"), O3EByteVal(1, "Maximum"), O3EByteVal(1, "Average"), O3EByteVal(1, "Error")]),
        420 : O3EComplexType(5, "SupplyAirHumiditySensor",[O3EByteVal(1, "Actual"), O3EByteVal(1, "Minimum"), O3EByteVal(1, "Maximum"), O3EByteVal(1, "Average"), O3EByteVal(1, "Error")]),
        421 : O3EComplexType(5, "ExtractAirHumiditySensor",[O3EByteVal(1, "Actual"), O3EByteVal(1, "Minimum"), O3EByteVal(1, "Maximum"), O3EByteVal(1, "Average"), O3EByteVal(1, "Error")]),
        422 : O3EComplexType(5, "ExhaustAirHumiditySensor",[O3EByteVal(1, "Actual"), O3EByteVal(1, "Minimum"), O3EByteVal(1, "Maximum"), O3EByteVal(1, "Average"), O3EByteVal(1, "Error")]),
        424 : O3EComplexType(9, "MixerOneCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        426 : O3EComplexType(9, "MixerTwoCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        428 : O3EComplexType(9, "MixerThreeCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        429 : RawCodec(4, "ElectricalPreHeater"),
        430 : O3EComplexType(9, "MixerFourCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        431 : O3EComplexType(9, "SupplyAirVolumeFlowSensor",[O3EInt16(2, "Zuluftvolumenstrom", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        432 : O3EComplexType(9, "MixerFiveCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        433 : O3EComplexType(9, "ExhaustAirVolumeFlowSensor",[O3EInt16(2, "Abluftvolumenstrom", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Error")]),
        434 : O3EComplexType(9, "MixerSixCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        435 : O3EComplexType(8, "VentilationStageTargetVolumeFlow",[O3EInt16(2, "Stage1", scale=1.0), O3EInt16(2, "Stage2", scale=1.0), O3EInt16(2, "Stage3", scale=1.0), O3EInt16(2, "Stage4", scale=1.0)]),
        436 : O3EComplexType(9, "MixerSevenCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        437 : O3EComplexType(2, "BypassOperationState",[O3EByteVal(1, "BypassStatus"), O3EByteVal(1, "Unknown1")]),
        438 : O3EComplexType(9, "MixerEightCircuitRoomTemperatureSetpoint", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Standard", signed=True), O3EInt16(2, "Reduced", signed=True), RawCodec(2, "Unknown2"), O3EByteVal(1, "Unknown1")]),
        439 : O3EByteVal(1, "BypassAvailableModes"),
        449 : RawCodec(141, "ElectricalEnergyMatrix"),
        451 : RawCodec(4, "ExternalAlternatingCurrentPowerSetpoint"),
        475 : O3EComplexType(2, "MixerOneCircuitThreeWayValvePositionPercent", [O3EInt8(1,"Position", signed=True), RawCodec(1,"Unknown")]),
        476 : O3EComplexType(2, "MixerTwoCircuitThreeWayValvePositionPercent", [O3EInt8(1,"Position", signed=True), RawCodec(1,"Unknown")]),
        477 : O3EComplexType(2, "MixerThreeCircuitThreeWayValvePositionPercent", [O3EInt8(1,"Position", signed=True), RawCodec(1,"Unknown")]),
        478 : O3EComplexType(2, "MixerFourCircuitThreeWayValvePositionPercent", [O3EInt8(1,"Position", signed=True), RawCodec(1,"Unknown")]),
        491 : O3EComplexType(2, "DomesticHotWaterCirculationPump",[O3EByteVal(1,"State"),O3EByteVal(1,"Unknown")]),                
        497 : O3EComplexType(5, "DomesticHotWaterCirculationPumpMode",[O3EByteVal(1, "Mode"), O3EByteVal(1, "HygenieActive"), O3EByteVal(1, "HeatingActive"), O3EByteVal(1, "CyclesPerHour"), O3EByteVal(1, "Cycles")]),
        500 : RawCodec(2, "CentralHeatDemandExternalAc"),
        503 : RawCodec(2, "ScaldProtection"),
        504 : O3EComplexType(14, "DomesticHotWaterSetpointMetaData", [O3EInt16(2,"LowerBufferLimitTemperature", signed=True), O3EInt16(2, "MinimumBufferTemperature", signed=True), O3EInt16(2, "DefaultBufferTemperature", signed=True), O3EInt16(2, "MaximumBufferTemperature", signed=True), O3EInt16(2, "UpperBufferLimitTemperature", signed=True), O3EInt16(2, "EfficiencyLowerLimit", signed=True), O3EInt16(2, "EfficiencyUpperLimit",signed=True)]), #250xx Unit °C
        505 : O3ESdate(3, "Date"),
        506 : O3EStime(3, "Time"),
        507 : O3EUtc(4, "UniversalTimeCoordinated"),
        508 : O3EByteVal(1, "UniversalTimeCoordinatedOffset"),
        510 : O3EByteVal(1, "Language"),
        511 : RawCodec(8, "HolidayPhase"),
        512 : RawCodec(8, "HolidayAtHomePhase"),
        513 : RawCodec(8, "HolidayPhaseCircuitOne"),
        514 : RawCodec(8, "HolidayAtHomePhaseCircuitOne"),
        515 : RawCodec(8, "HolidayPhaseCircuitTwo"),
        516 : RawCodec(8, "HolidayAtHomePhaseCircuitTwo"),
        517 : RawCodec(8, "HolidayPhaseCircuitThree"),
        518 : RawCodec(8, "HolidayAtHomePhaseCircuitThree"),
        519 : RawCodec(8, "HolidayPhaseCircuitFour"),
        520 : RawCodec(8, "HolidayAtHomePhaseCircuitFour"),
        521 : O3EInt16(2, "OperatingHoursTillService", scale=1.0),
        522 : O3EComplexType(4, "ServiceDateNext",[O3ESdate(3, "Date"), O3EByteVal(1, "Status")]),
        523 : O3ESdate(3, "ServiceDateLast"),
        524 : O3EInt16(2, "ModulationTargetSetpoint"),
        525 : O3EInt16(2, "ExternalModulationSetpoint"),
        526 : O3EInt16(2, "ModulationCurrentValue"),
        527 : O3EInt16(2, "FlowTemperatureTargetSetpoint", signed=True),
        528 : O3EInt16(2, "ExternalTargetFlowTemperatureSetpoint"),
        531 : O3EComplexType(2, "DomesticHotWaterOperationState",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        533 : O3EComplexType(2, "VentilationTargetOperationLevel",[O3EByteVal(1, "Acutual"), O3EByteVal(1, "Unknown1")]),
        534 : RawCodec(2, "DomesticHotWaterPumpPostRunTime"),
        535 : O3EComplexType(12, "ObjectElectricalEnergyStatistical", [O3EInt32(4, "GridFeedInEnergy", scale=10),O3EInt32(4, "GridSuppliedEnergy", scale=10),O3EInt32(4, "ProducedEnergy", scale=10)]),
        537 : O3EComplexType(2, "ExternalMixerOneCircuitTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        538 : O3EComplexType(2, "ExternalDomesticHotWaterTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
#        543 : RawCodec(4, "SmartGridReadyConsolidator"), # ref https://github.com/open3e/open3e/discussions/110#discussioncomment-9880590
        543 : O3EComplexType(4, "SmartGridReadyConsolidator",[O3EByteVal(1, "Unknown1"), O3EByteVal(1, "OperatingStatus"), O3EByteVal(1, "Unknown2"),O3EByteVal(1, "Unknown3")]),
        544 : O3EComplexType(12, "GasConsumptionCentralHeating", [O3EInt16(2, "Today"), O3EInt16(2, "Past7Days"), O3EInt16(2, "CurrentMonth"), O3EInt16(2, "PastMonth"), O3EInt16(2, "CurrentYear"), O3EInt16(2, "PastYear")]),
        545 : O3EComplexType(12, "GasConsumptionDomesticHotWater", [O3EInt16(2, "Today"), O3EInt16(2, "Past7Days"), O3EInt16(2, "CurrentMonth"), O3EInt16(2, "PastMonth"), O3EInt16(2, "CurrentYear"), O3EInt16(2, "PastYear")]),
        548 : O3EComplexType(24, "EnergyConsumptionCentralHeating", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]),  
        565 : O3EComplexType(24, "EnergyConsumptionDomesticHotWater", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        566 : O3EComplexType(24, "EnergyConsumptionCooling", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        567 : O3EComplexType(24, "GeneratedElectricity", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        568 : RawCodec(24, "CoTwoSavings"),
        569 : O3EByteVal(1, "ResetSensorMinMaxAverageStatistics"),
        570 : RawCodec(1, "ResetStatistics"),
        572 : RawCodec(3, "SetDefaultValuesDate"),
        573 : RawCodec(2, "RemoteReset"),
        575 : O3EByteVal(1, "SetDeliveryStatus"),#+++
        576 : O3ESdate(3, "SetDeliveryStatusDate"),
        580 : O3ESoftVers(8, "SoftwareVersion"),
        581 : O3ESoftVers(8, "HardwareVersion"),
        589 : O3EInt32(4, "VentilationOperationHours", scale=1.0),
        592 : O3EMacAddr(6, "MacAddressLan"),
        593 : O3EMacAddr(6, "GatewayMac"),
        596 : RawCodec(1, "CentralHeatingPartLoadPercent"),
        597 : O3EInt8(1, "DomesticHotWaterPartLoadPercent", scale = 1),
        600 : RawCodec(3, "FuelCellReset"),
        602 : O3EByteVal(1, "GatewayRemoteLocalNetworkStatus"),
        603 : O3EByteVal(1, "GatewayApEnable"),
        604 : O3EComplexType(76, "GatewayApDataSet", [O3EUtf8(32, "SSID_AccessPoint"), O3EUtf8(40, "Password_AccessPoint"), O3EIp4Addr(4, "IP-Address_AccessPoint")]),
        607 : O3EComplexType(20, "GatewayRemoteIp", [O3EIp4Addr(4, "WLAN_IP-Address"), O3EIp4Addr(4, "SubnetMask"), O3EIp4Addr(4, "Gateway_IP-Address"), O3EIp4Addr(4, "DNSServer1"), O3EIp4Addr(4, "DNSServer2")]),
        609 : RawCodec(40, "ProxyServer"),
        610 : RawCodec(2, "ProxyPort"),
        611 : O3EUtf8(40, "ProxyUser"),
        613 : O3EByteVal(1, "ProxyEnabled"),
        616 : O3EByteVal(1, "GatewayRemoteEnable"),
        617 : O3EUtf8(72, "GatewayRemoteSsid"),#+++
        618 : O3EByteVal(1, "GatewayRemoteIpStatic"),
        619 : RawCodec(2, "GatewayRemoteScanNetwork"),
        620 : O3EByteVal(1, "DiagnosticServiceConnectionStatus"),
        621 : O3EComplexType(181, "ObjectContactDetails", [O3EUtf8(20, "Name"), O3EUtf8(15, "PreName"), O3EUtf8(20, "Street"), O3EUtf8(10, "StreetExtension"), O3EUtf8(7, "ZipCode"), O3EUtf8(15, "Region"), O3EUtf8(15, "City"), O3EUtf8(16, "Phone"), O3EUtf8(16, "Mobile"), O3EUtf8(30, "Email"), O3EEnum(1, "Country", "Countries"), O3EUtf8(16, "IdentificationNumber")]),
        622 : O3EComplexType(181, "CustomerDetails", [O3EUtf8(20, "Name"), O3EUtf8(15, "PreName"), O3EUtf8(20, "Street"), O3EUtf8(10, "StreetExtension"), O3EUtf8(7, "ZipCode"), O3EUtf8(15, "Region"), O3EUtf8(15, "City"), O3EUtf8(16, "Phone"), O3EUtf8(16, "Mobile"), O3EUtf8(30, "Email"), O3EEnum(1, "Country", "Countries"), O3EUtf8(16, "Identification Number")]), 
        623 : O3EComplexType(181, "ServiceEngineer", [O3EUtf8(20, "Name"), O3EUtf8(15, "PreName"), O3EUtf8(20, "Street"), O3EUtf8(10, "StreetExtension"), O3EUtf8(7, "ZipCode"), O3EUtf8(15, "Region"), O3EUtf8(15, "City"), O3EUtf8(16, "Phone"), O3EUtf8(16, "Mobile"), O3EUtf8(30, "Email"), O3EEnum(1, "Country", "Countries"), O3EUtf8(16, "Identification Number")]), # vizard\app\src\main\assets\one_click_configuration8.json
        624 : O3EComplexType(181, "TechnicalSupport", [O3EUtf8(20, "Name"), O3EUtf8(15, "PreName"), O3EUtf8(20, "Street"), O3EUtf8(10, "StreetExtension"), O3EUtf8(7, "ZipCode"), O3EUtf8(15, "Region"), O3EUtf8(15, "City"), O3EUtf8(16, "Phone"), O3EUtf8(16, "Mobile"), O3EUtf8(30, "Email"), O3EEnum(1, "Country", "Countries"), O3EUtf8(16, "Identification Number")]),
        625 : O3EComplexType(26, "ObjectDetails", [O3EInt32(4, "Latitude", scale=10000, signed=True), O3EInt32(4, "Longitude", scale=10000, signed=True), O3EInt16(2, "Altitude", scale=1, signed=True), O3EInt16(2, "OrientationHorizontally", scale=1, signed=True), O3EInt16(2, "OrientationVertically", scale=1, signed=True), O3EInt16(2, "HeatingLoadPerSquareMeterPerYear", scale=1, signed=False), O3EInt16(2, "CentralHeatingCylinderSize", scale=10, signed=False), O3EInt16(2, "DomesticHotWaterCylinderSize", scale=10, signed=False), O3EInt16(2, "BufferCylinderSize", scale=10, signed=False), O3EInt16(2, "InstallationRoomSize", scale=10, signed=False), O3EInt16(2, "NitrogenOxide", scale=1, signed=False)]),  # vizard\app\src\main\assets\one_click_configuration5.json
        627 : O3EUtf8(40, "CentralHeatingOneCircuitName"), # vizard\app\src\main\assets\one_click_configuration5.json
        628 : O3EUtf8(40, "CentralHeatingTwoCircuitName"),
        629 : O3EUtf8(40, "CentralHeatingThreeCircuitName"),
        630 : O3EUtf8(40, "CentralHeatingFourCircuitName"),
        631 : O3EUtf8(12, "CentralHeatingFiveCircuitName"),
        632 : O3EUtf8(12, "CentralHeatingSixCircuitName"),
        633 : O3EUtf8(12, "CentralHeatingSevenCircuitName"),
        634 : O3EUtf8(12, "CentralHeatingEightCircuitName"),
        645 : O3EByteVal(1, "GenericAnalogDigitalAccessoryOneModulFunction"),
        646 : O3EByteVal(1, "GenericAnalogDigitalAccessoryTwoModulFunction"),
        647 : O3EByteVal(1, "GenericAnalogDigitalAccessoryThreeModulFunction"),
        648 : O3EByteVal(1, "GenericAnalogDigitalAccessoryFourModulFunction"),
        649 : O3EByteVal(1, "GenericAnalogDigitalAccessoryFiveModulFunction"),
        650 : O3EByteVal(1, "GenericDigitalAccessoryOneModulFunction"),
        651 : O3EByteVal(1, "GenericDigitalAccessoryTwoModulFunction"),
        652 : O3EByteVal(1, "GenericDigitalAccessoryThreeModulFunction"),
        653 : O3EByteVal(1, "GenericDigitalAccessoryFourModulFunction"),
        654 : O3EByteVal(1, "GenericDigitalAccessoryFiveModulFunction"),
        680 : RawCodec(123, "EnergyMeter"),
        691 : O3EList(57, "DomesticHotWaterTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        692 : O3EList(57, "DomesticHotWaterTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        693 : O3EList(57, "DomesticHotWaterTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        694 : O3EList(57, "DomesticHotWaterTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        695 : O3EList(57, "DomesticHotWaterTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        696 : O3EList(57, "DomesticHotWaterTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        697 : O3EList(57, "DomesticHotWaterTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        726 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        727 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        728 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        729 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        730 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        731 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        732 : O3EList(57, "DomesticHotWaterCirculationTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        761 : O3EList(57, "MixerOneCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        762 : O3EList(57, "MixerOneCircuitTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        763 : O3EList(57, "MixerOneCircuitTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        764 : O3EList(57, "MixerOneCircuitTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        765 : O3EList(57, "MixerOneCircuitTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        766 : O3EList(57, "MixerOneCircuitTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        767 : O3EList(57, "MixerOneCircuitTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        768 : O3EList(57, "MixerTwoCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        769 : O3EList(57, "MixerTwoCircuitTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        770 : O3EList(57, "MixerTwoCircuitTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        771 : O3EList(57, "MixerTwoCircuitTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        772 : O3EList(57, "MixerTwoCircuitTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        773 : O3EList(57, "MixerTwoCircuitTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        774 : O3EList(57, "MixerTwoCircuitTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        775 : O3EList(57, "MixerThreeCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        776 : O3EList(57, "MixerThreeCircuitTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        777 : O3EList(57, "MixerThreeCircuitTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        778 : O3EList(57, "MixerThreeCircuitTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        779 : O3EList(57, "MixerThreeCircuitTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        780 : O3EList(57, "MixerThreeCircuitTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        781 : O3EList(57, "MixerThreeCircuitTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        782 : O3EList(57, "MixerFourCircuitTimeScheduleMonday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        783 : O3EList(57, "MixerFourCircuitTimeScheduleTuesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        784 : O3EList(57, "MixerFourCircuitTimeScheduleWednesday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        785 : O3EList(57, "MixerFourCircuitTimeScheduleThursday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        786 : O3EList(57, "MixerFourCircuitTimeScheduleFriday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        787 : O3EList(57, "MixerFourCircuitTimeScheduleSaturday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        788 : O3EList(57, "MixerFourCircuitTimeScheduleSunday",[O3EByteVal(1, "Count"), O3EComplexType(7, "Schedules",[O3EStime(2, "Start"),O3EStime(2, "Stop"), RawCodec(2, "Unknown"), O3EByteVal(1, "Mode")])]),
        873 : O3EComplexType(2, "LegionellaProtectionActivation",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),# Mode: 0 / 1 Legionella Protection deactivated / activated  State: 0 / 1 Legionella Protection not running / running
        874 : O3EInt16(3, "LegionellaProtectionTargetTemperatureSetpoint"),
        875 : O3EStime(2, "LegionellaProtectionStartTime"),
        876 : O3EByteVal(1, "LegionellaProtectionWeekday"),
        877 : O3EStime(3, "LegionellaProtectionLastSuccessfulStartTime"),
        878 : O3EByteVal(1, "LegionellaProtectionLastSuccessfulWeekday"),
        880 : O3EComplexType(4, "MixerOneCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        881 : O3EComplexType(4, "MixerTwoCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        882 : O3EComplexType(4, "MixerThreeCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        883 : O3EComplexType(4, "MixerFourCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        884 : O3EComplexType(4, "MixerFiveCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        885 : O3EComplexType(4, "MixerSixCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        886 : O3EComplexType(4, "MixerSevenCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        887 : O3EComplexType(4, "MixerEightCircuitCentralHeatingCurve", [O3EInt8(1, "Gradient", scale=10), O3EInt8(1, "Level", signed=True), O3EInt16(2, "BasePoint", signed=True)]),
        896 : O3EInt16(2, "OutsideTemperatureOffset", signed=True),
        897 : O3EByteVal(1, "ScreedDryingProfileActivation"),
        898 : O3EByteVal(1, "RemainingFloorDryingDays"),
        900 : O3EByteVal(1, "GatewayRemoteSignalStrength"),
        901 : O3EByteVal(1, "ServiceManagerIsRequired"),
        902 : O3EByteVal(1, "MalfunctionIdentification"),
        903 : RawCodec(4, "DisplaySettings"),
        905 : RawCodec(4, "ElectricalPostHeater"),
        906 : RawCodec(3, "ExhaustFlap"),
        907 : O3EByteVal(1, "UserInterfaceDefaultHomeScreen"),
        908 : O3EByteVal(1, "ExternalFaultSignal"),
        909 : O3EByteVal(1, "ExternalFaultSignalInput"),
        912 : RawCodec(5, "DaylightSavingTimeActive"),
        915 : O3ESdate(3, "LastBackupDate"),
        917 : RawCodec(20, "RemoteWeatherService"),
        918 : O3EByteVal(1, "TradeFairMode"),
        919 : O3EInt16(2, "OutsideTemperatureDampingFactor"),
        920 : RawCodec(36, "ThreeAxisAccelerationSensor"),
        921 : O3EComplexType(2, "ExternalAccessInProgress",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        922 : O3EInt16(2, "ProductionTraceabilityByte"),#+++
        923 : RawCodec(8, "RealTimeClockStatus"),
        924 : O3EByteVal(1, "StartUpWizard"),
        925 : RawCodec(5, "FillingVenting"),
        927 : O3EEnum(1, "BuildingType", "BuildingTypes"),
        928 : O3EUtf8(16, "ElectronicTraceabilityNumber"),
        929 : O3EEnum(1, "GasType", "GasTypes"),
        930 : RawCodec(10, "ExternalTargetCentralHeatingFlowSetpointMetaData"),
        931 : RawCodec(10, "DomesticHotWaterFlowSetpointMetaData"),            
        933 : O3EComplexType(9, "MixerOneCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        934 : O3EComplexType(9, "MixerTwoCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        935 : O3EComplexType(9, "MixerThreeCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        936 : O3EComplexType(9, "MixerFourCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        937 : O3EComplexType(9, "MixerFiveCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        938 : O3EComplexType(9, "MixerSixCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        939 : O3EComplexType(9, "MixerSevenCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        940 : O3EComplexType(9, "MixerEightCircuitProperty", [O3EEnum(1,"MixerCircuitType","MixerCircuitTypes"), O3EEnum(1,"BusType","BusTypes"), O3EEnum(1,"RemoteControl","RemoteControls"), O3EEnum(1,"Priority","Priorities"), O3EByteVal(1,"BusAddress"), O3EInt16(2,"FlowTemperatureOffset"), O3EEnum(1,"RegulationType","RegulationTypes"), O3EByteVal(1,"RoomTemperatureCorrectionFactor")]),
        950 : O3EInt8(4, "SolarCircuitWaterFlowRate", signed=True),
        951 : RawCodec(8, "SolarCircuitExtendedFunctions"),
        952 : RawCodec(51, "HydraulicMatrix"),
        953 : RawCodec(24, "SolarEnergyYield"),
        954 : O3EList(181, "BusTopologyMatrix", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        960 : O3EByteVal(1, "ExhaustPipeType"),
        961 : RawCodec(2, "SecurityAlgorithmNumber"),
        962 : O3ESoftVers(8, "BootLoaderVersion"),
        963 : O3EUtf8(16, "SparePartNumber"),
        964 : O3EEnum(1, "ActiveDiagnosticSession", "DiagnosticSessionLevels"),
        987 : O3EInt16(2, "MixerOneCircuitFlowTemperatureTargetSetpoint", signed=True),
        988 : O3EInt16(2, "MixerTwoCircuitFlowTemperatureTargetSetpoint", signed=True),
        989 : O3EInt16(2, "MixerThreeCircuitFlowTemperatureTargetSetpoint", signed=True),
        990 : O3EInt16(2, "MixerFourCircuitFlowTemperatureTargetSetpoint", signed=True),
        1004 : O3EEnum(1, "CentralHeatingRegulationMode", "RegulationTypes"),
        1006 : RawCodec(4, "TargetQuickMode"),
        1007 : RawCodec(4, "CurrentQuickMode"),
        1008 : RawCodec(4, "MixerOneCircuitTargetQuickMode"),
        1009 : RawCodec(4, "MixerTwoCircuitTargetQuickMode"),
        1010 : RawCodec(4, "MixerThreeCircuitTargetQuickMode"),
        1011 : RawCodec(4, "MixerFourCircuitTargetQuickMode"),
        1024 : RawCodec(4, "MixerOneCircuitCurrentQuickMode"),
        1025 : RawCodec(4, "MixerTwoCircuitCurrentQuickMode"),
        1026 : RawCodec(4, "MixerThreeCircuitCurrentQuickMode"),
        1027 : RawCodec(4, "MixerFourCircuitCurrentQuickMode"),
        1040 : O3EComplexType(6, "SupplyAirFan",[RawCodec(3, "Unknown1"), O3EInt16(2, "Actual", signed=True), RawCodec(1, "Unknown2")]),
        1041 : O3EComplexType(6, "ExhaustAirFan",[RawCodec(3, "Unknown1"), O3EInt16(2, "Actual", signed=True), RawCodec(1, "Unknown2")]),
        1042 : RawCodec(9, "PrimaryHeatExchangerTemperatureSensor"),            
        1043 : O3EComplexType(5, "AllengraSensor", [O3EInt16(2, "Actual"), O3EInt16(2, "Temperature"), RawCodec(1, "Unknown")]),
        1044 : RawCodec(2, "SecondaryCentralHeatingPump"),
        1047 : RawCodec(11, "TimeSeriesRecordedFlowTemperatureSensor"),
        1084 : RawCodec(4, "FlowTemperatureMinimumMaximumLimit"),
        1085 : O3EComplexType(4, "DomesticHotWaterHysteresis", [O3EInt16(2, "SetpointSwitchOn", signed=True), O3EInt16(2, "SetpointSwitchOff", signed=True)]),
        1087 : O3EComplexType(2, "MaximumDomesticHotWaterLoadingTime", [O3EInt8(1, "SetpointMaxOn", signed=False), O3EInt8(1, "SetpointMinOff", signed=False)]),
        1088 : O3EByteVal(1, "OutsideAirBypass"),
        1089 : O3EByteVal(1, "InsideAirBypass"),
        1090 : RawCodec(9, "EnvironmentAirQuality"),
        1093 : RawCodec(2, "ExhaustPipeLength"),
        1096 : O3EByteVal(1, "ResetEnergyManagerDataCollector"),
        1097 : O3EComplexType(20, "ElectricityPrice", [RawCodec(4, "Unknown1"), RawCodec(4, "Unknown2"), O3EInt32(4, "NormalRate", scale=100), O3EInt32(4, "LowRate", scale = 100), RawCodec(4, "Unknown3")]), # Unit ct
        1098 : O3EComplexType(20, "GasProperties", [O3EInt32(4, "Rate", scale = 100), RawCodec(4, "Unknown1"), RawCodec(4, "Unknown2"), RawCodec(4, "Unknown3"), RawCodec(4, "Unknown4")]), # Unit ct
        1100 : O3EComplexType(3, "CentralHeatingPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1101 : O3EComplexType(3, "DomesticHotWaterPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1102 : O3EComplexType(3, "MixerOneCircuitPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1103 : O3EComplexType(3, "MixerTwoCircuitPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1104 : O3EComplexType(3, "MixerThreeCircuitPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1105 : O3EComplexType(3, "MixerFourCircuitPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1118 : O3EComplexType(3, "SolarCircuitPumpMinimumMaximumLimit", [O3EInt8(1, "MinSpeed"), O3EInt8(1, "MaxSpeed"), O3EInt8(1, "Setpoint")]),
        1125 : O3EInt16(2, "SolarMaximumLoadingTemperature", signed=True),
        1128 : O3EInt16(2, "SolarStagnationHours", signed=True),
        1132 : O3EComplexType(97, "ViessmannIdentificationNumberListInternal", [O3EByteVal(1, "Count"), O3EUtf8(16, "VIN1"), O3EUtf8(16, "VIN2"), O3EUtf8(16, "VIN3"), O3EUtf8(16, "VIN4"), O3EUtf8(16, "VIN5"), O3EUtf8(16, "VIN6")]),
        1136 : RawCodec(4, "SolarProperty"),
        1137 : O3EByteVal(1, "ServiceModeActivation"),
        1138 : RawCodec(1, "AccentLedBar"),
        1139 : RawCodec(7, "CentralHeatingCurveAdaptionParameter"),
        1165 : O3EByteVal(1, "BackendConnectionStatus"),
        1166 : RawCodec(5, "ResetDtcHistory"),
        1167 : O3EInt16(2, "ExternalDomesticHotWaterTemperatureSetpoint", signed=True),
        1172 : RawCodec(14, "SolarCircuitPumpStatistical"),
        1175 : O3EByteVal(1, "AcknowledgeInfoAlarmMessage"),
        1176 : O3EByteVal(1, "AcknowledgeWarningAlarmMessage"),
        1177 : O3EByteVal(1, "AcknowledgeServiceAlarmMessage"),
        1178 : O3EByteVal(1, "AcknowledgeErrorAlarmMessage"),
        1181 : O3EInt8(1, "DisplayTestMode"),#+++
        1190 : O3EInt16(4, "ThermalPower"),
        1191 : RawCodec(1, "FuelCellStatus"),
        1192 : O3EComplexType(10, "MixerOneCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1193 : O3EComplexType(10, "MixerTwoCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1194 : O3EComplexType(10, "MixerThreeCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1195 : O3EComplexType(10, "MixerFourCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1196 : O3EComplexType(10, "MixerFiveCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1197 : O3EComplexType(10, "MixerSixCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1198 : O3EComplexType(10, "MixerSevenCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1199 : O3EComplexType(10, "MixerEightCircuitFlowTemperatureMinimumMaximumLimit", [O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), RawCodec(6, "Unknown")]),
        1210 : RawCodec(13, "FuelCellStatistical"),
        1211 : O3EComplexType(24, "GeneratedCentralHeatingOutput", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        1214 : RawCodec(2, "ElectricalPowerOutput"),
        1215 : RawCodec(1, "FuelCellState"),
        1216 : RawCodec(1, "FuelCellStateTwo"),
        1217 : RawCodec(1, "FuelCellGenerationMode"),
        1218 : RawCodec(1, "FuelCellInstruction"),
        1220 : RawCodec(1, "FuelCellMode"),
        1221 : RawCodec(1, "FuelCellModeResult"),
        1222 : RawCodec(1, "FuelCellRunRequest"),
        1223 : RawCodec(1, "FuelCellRunRequestResult"),
        1224 : RawCodec(1, "FuelCellStopRequest"),
        1226 : RawCodec(1, "FuelCellProcessNumber"),
        1227 : RawCodec(1, "FuelCellRequestAction"),
        1228 : RawCodec(1, "FuelCellCompletionNotification"),
        1229 : RawCodec(1, "FuelCellGasTypeSetting"),
        1230 : RawCodec(1, "FuelCellCountrySetting"),
        1231 : RawCodec(4, "FuelCellPrimaryPump"),
        1232 : O3EEnum(1, "GenericDigitalInputConfigurationOnBoardOne", "DigitalInputConfigurations"),
        1233 : RawCodec(68, "GatewayRemoteVisibleOneTwo"),
        1234 : RawCodec(68, "GatewayRemoteVisibleThreeFour"),
        1235 : RawCodec(68, "GatewayRemoteVisibleFiveSix"),
        1236 : RawCodec(68, "GatewayRemoteVisibleSevenEight"),
        1237 : RawCodec(68, "GatewayRemoteVisibleNineTen"),
        1238 : RawCodec(31, "AvailableActorSensorComponents"),
        1239 : RawCodec(2, "ActorSensorTest"),
        1240 : O3EByteVal(1, "CentralHeatingPumpMode"),
        1241 : O3EByteVal(1, "MixerOneCircuitPumpMode"),
        1242 : O3EByteVal(1, "MixerTwoCircuitPumpMode"),
        1243 : O3EByteVal(1, "MixerThreeCircuitPumpMode"),
        1244 : O3EByteVal(1, "MixerFourCircuitPumpMode"),
        1263 : RawCodec(2, "DiverterValveBoilerHydraulicTower"),
        1264 : RawCodec(2, "DiverterValveFuelCellHydraulicTower"),
        1265 : RawCodec(8, "FanTargetSpeedMeta"),            
        1266 : O3EInt16(8, "DiverterValveStatistical", scale = 1),
        1286 : O3EList(181, "BusTopologyMatrixTwo", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        1287 : O3EList(181, "BusTopologyMatrixThree", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        1288 : O3EList(181, "BusTopologyMatrixFour", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        1289 : O3EList(181, "BusTopologyMatrixFive", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        1290 : RawCodec(4, "DomesticHotWaterShiftLoadPump"),
        1294 : O3EComplexType(124, "EnergyConsumptionCentralHeatingMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1311 : O3EComplexType(124, "EnergyConsumptionDomesticHotWaterMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1312 : O3EComplexType(124, "EnergyConsumptionCoolingMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1313 : O3EComplexType(124, "GeneratedElectricityMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1314 : O3EComplexType(124, "SolarEnergyYieldMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1315 : O3EComplexType(124, "GeneratedCentralHeatingOutputMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1316 : O3EComplexType(96,"EnergyConsumptionCentralHeatingYearMatrix",[O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1333 : O3EComplexType(96, "EnergyConsumptionDomesticHotWaterYearMatrix",[O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1334 : O3EComplexType(96, "EnergyConsumptionCoolingYearMatrix", [O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1335 : O3EComplexType(96, "GeneratedElectricityYearMatrix",[O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1336 : O3EComplexType(96, "SolarEnergyYieldYearMatrix", [O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1337 : O3EComplexType(96, "GeneratedCentralHeatingOutputYearMatrix", [
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1338 : RawCodec(31, "ScreedDryingProfileDefinition"),
        1339 : O3EByteVal(1, "MalfunctionHeatingUnitBlocked"),
        1340 : O3EComplexType(124, "FuelCellGeneratedHeatOutputMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1341 : O3EComplexType(96, "FuelCellGeneratedHeatOutputYearMatrix",[
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1342 : O3EComplexType(124, "GasConsumptionCentralHeatingMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1343 : O3EComplexType(48, "GasConsumptionCentralHeatingYearMatrix",  [
            O3EList(24, "CurrentYear", [O3EInt16(2, "01_January", scale=10), O3EInt16(2, "02_February", scale=10), O3EInt16(2, "03_March", scale=10), O3EInt16(2, "04_April", scale=10), O3EInt16(2, "05_May", scale=10), O3EInt16(2, "06_June", scale=10),
                                                                      O3EInt16(2, "07_July", scale=10), O3EInt16(2, "08_August", scale=10), O3EInt16(2, "09_September", scale=10), O3EInt16(2, "10_October", scale=10), O3EInt16(2, "11_November", scale=10), O3EInt16(2, "12_December", scale=10)]),
            O3EList(24, "LastYear", [O3EInt16(2, "01_January", scale=10), O3EInt16(2, "02_February", scale=10), O3EInt16(2, "03_March", scale=10), O3EInt16(2, "04_April", scale=10), O3EInt16(2, "05_May", scale=10), O3EInt16(2, "06_June", scale=10),
                                                                      O3EInt16(2, "07_July", scale=10), O3EInt16(2, "08_August", scale=10), O3EInt16(2, "09_September", scale=10), O3EInt16(2, "10_October", scale=10), O3EInt16(2, "11_November", scale=10), O3EInt16(2, "12_December", scale=10)]),
        ]),
        1344 : O3EComplexType(124, "GasConsumptionDomesticHotWaterMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1345 : O3EComplexType(48, "GasConsumptionDomesticHotWaterYearMatrix",[
            O3EList(24, "CurrentYear", [O3EInt16(2, "01_January", scale=10), O3EInt16(2, "02_February", scale=10), O3EInt16(2, "03_March", scale=10), O3EInt16(2, "04_April", scale=10), O3EInt16(2, "05_May", scale=10), O3EInt16(2, "06_June", scale=10),
                                                                      O3EInt16(2, "07_July", scale=10), O3EInt16(2, "08_August", scale=10), O3EInt16(2, "09_September", scale=10), O3EInt16(2, "10_October", scale=10), O3EInt16(2, "11_November", scale=10), O3EInt16(2, "12_December", scale=10)]),
            O3EList(24, "LastYear", [O3EInt16(2, "01_January", scale=10), O3EInt16(2, "02_February", scale=10), O3EInt16(2, "03_March", scale=10), O3EInt16(2, "04_April", scale=10), O3EInt16(2, "05_May", scale=10), O3EInt16(2, "06_June", scale=10),
                                                                      O3EInt16(2, "07_July", scale=10), O3EInt16(2, "08_August", scale=10), O3EInt16(2, "09_September", scale=10), O3EInt16(2, "10_October", scale=10), O3EInt16(2, "11_November", scale=10), O3EInt16(2, "12_December", scale=10)]),
        ]),
        1346 : O3EComplexType(12, "HeatEngineStatistical", [O3EInt32(4, "Betriebsstunden", scale = 1), O3EInt32(4, "Brennerstunden", scale = 1), O3EInt32(4, "Brennerstarts", scale = 1)]),
        1347 : RawCodec(10, "ObjectElectricalEnergyStatus"),
        1348 : RawCodec(12, "FuelCellGasConsumption"),
        1349 : RawCodec(124, "FuelCellGasConsumptionMonthMatrix"),
        1350 : RawCodec(48, "FuelCellGasConsumptionYearMatrix"),
        1351 : RawCodec(24, "FeedInEnergy"),
        1352 : RawCodec(124, "FeedInEnergyMonthMatrix"),
        1353 : RawCodec(96, "FeedInEnergyYearMatrix"),
        1354 : RawCodec(6, "ProductionCoverageRate"),
        1355 : RawCodec(62, "ProductionCoverageRateMonthMatrix"),
        1356 : RawCodec(24, "ProductionCoverageRateYearMatrix"),
        1357 : RawCodec(11, "FuelCellOperationTime"),
        1358 : RawCodec(124, "FuelCellOperationTimeMonthMatrix"),
        1359 : RawCodec(48, "FuelCellOperationTimeYearMatrix"),
        1360 : RawCodec(11, "FuelCellRunTime"),
        1361 : RawCodec(124, "FuelCellRunTimeMonthMatrix"),
        1362 : RawCodec(48, "FuelCellRunTimeYearMatrix"),
        1363 : RawCodec(1, "FuelCellTargetOperationMode"),
        1364 : O3EByteVal(1, "GenericSdioAccessoryOneModulFunction"),
        1367 : RawCodec(2, "FuelCellThermalPower"),
        1371 : RawCodec(6, "DemandCoverageRate"),
        1372 : RawCodec(62, "DemandCoverageRateMonthMatrix"),
        1373 : RawCodec(24, "DemandCoverageRateYearMatrix"),
        1383 : RawCodec(11, "FuelCellBreakdownRate"),
        1384 : RawCodec(124, "FuelCellBreakdownRateMonthMatrix"),
        1385 : RawCodec(48, "FuelCellBreakdownRateYearMatrix"),
        1389 : RawCodec(124, "CoTwoSavingsMonthMatrix"),
        1390 : RawCodec(96, "CoTwoSavingsYearMatrix"),
        1391 : O3EComplexType(24, "GeneratedDomesticHotWaterOutput", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        1392 : O3EComplexType(124, "GeneratedDomesticHotWaterOutputMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        1393 : O3EComplexType(96, "GeneratedDomesticHotWaterOutputYearMatrix", [
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        1394 : O3EInt16(2, "SolarChargingDomesticHotWaterSetpoint", signed=True),
        1395 : O3EComplexType(3, "MixerOneCircuitSummerSavingTemperatureThreshold", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        1396 : O3EComplexType(3, "MixerTwoCircuitSummerSavingTemperatureThreshold", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        1397 : O3EComplexType(3, "MixerThreeCircuitSummerSavingTemperatureThreshold", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        1398 : O3EComplexType(3, "MixerFourCircuitSummerSavingTemperatureThreshold", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        1411 : O3EByteVal(1, "ResetServiceInterval"),
        1415 : O3EComplexType(2, "MixerOneCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1416 : O3EComplexType(2, "MixerTwoCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1417 : O3EComplexType(2, "MixerThreeCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1418 : O3EComplexType(2, "MixerFourCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1419 : O3EComplexType(2, "MixerFiveCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1420 : O3EComplexType(2, "MixerSixCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1421 : O3EComplexType(2, "MixerSevenCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1422 : O3EComplexType(2, "MixerEightCircuitOperationState",[O3EEnum(1,"Mode","OpModes"),O3EEnum(1,"State","OpStates")]),
        1431 : RawCodec(8, "CarbonEmissionSettings"),
        1432 : RawCodec(4, "CentralHeatingPumpPerformance"),
        1434 : RawCodec(1, "ResetFuelCellStatistics"),
        1435 : RawCodec(9, "FuelCellFlowTemperatureSensor"),
        1436 : RawCodec(9, "FuelCellReturnTemperatureSensor"),
        1439 : RawCodec(41, "NoiseReductionTimeScheduleMonday"),
        1440 : RawCodec(41, "NoiseReductionTimeScheduleTuesday"),
        1441 : RawCodec(41, "NoiseReductionTimeScheduleWednesday"),
        1442 : RawCodec(41, "NoiseReductionTimeScheduleThursday"),
        1443 : RawCodec(41, "NoiseReductionTimeScheduleFriday"),
        1444 : RawCodec(41, "NoiseReductionTimeScheduleSaturday"),
        1445 : RawCodec(41, "NoiseReductionTimeScheduleSunday"),
        1451 : RawCodec(4, "ApplicationChecksum"),
        1467 : RawCodec(2, "SafetyRelevantRemoteUnlock"),
        1468 : RawCodec(9, "FuelCellGasPressure"),
        1469 : RawCodec(31, "SensorActuatorTestGroupHeatEngine"),
        1470 : RawCodec(31, "SensorActuatorTestGroupDomesticHotWater"),
        1471 : RawCodec(31, "SensorActuatorTestGroupFuelCell"),
        1472 : RawCodec(31, "SensorActuatorTestGroupHeatingCircuit"),
        1473 : RawCodec(31, "SensorActuatorTestGroupSolar"),
        1492 : RawCodec(4, "SolarCircuitPumpHysteresis"),
        1493 : RawCodec(16, "HeatEnginePerformanceStatistics"),
        1494 : O3ESoftVers(8, "OemProductVersion"),
        1503 : RawCodec(1, "MinimumLoadPercent"),
        1504 : O3EEnum(1, "TimeSettingSource", "TimeSettingSources"),
        1505 : RawCodec(2, "SolarStagnationTemperatureOffset"),
        1529 : O3EByteVal(1, "SolarRechargeSuppressionImpact"),
        1533 : RawCodec(2, "InstallationWizardInProgress"),
        1535 : RawCodec(3, "FlueGasSensorTestMode"),
        1536 : RawCodec(3, "PrimaryCircuitWaterFlowTestMode"),
        1537 : RawCodec(3, "ChimneySweeperTestMode"),
        1538 : O3EByteVal(1, "ZigbeeEnable"),
        1539 : O3EByteVal(1, "ZigbeeStatus"),
        1540 : RawCodec(26, "ZigbeeIdentification"),
        1541 : RawCodec(5, "LegionellaProtectionPump"),
        1549 : RawCodec(97, "HydraulicMatrixConfiguration"),
        1550 : RawCodec(22, "FunctionMatrix"),
        1551 : RawCodec(1, "FuelCellExternalControl"),
        1552 : RawCodec(7, "ElectricalEnergyStorageOperationState"),
        1553 : RawCodec(6, "ElectronicControlUnitOdxVersion"),
        1554 : RawCodec(2, "HeatingSupport"),
        1555 : RawCodec(6, "MixerOneCircuitFixedValueFlowTemperatureSetpoint"),
        1556 : RawCodec(6, "MixerTwoCircuitFixedValueFlowTemperatureSetpoint"),
        1557 : RawCodec(6, "MixerThreeCircuitFixedValueFlowTemperatureSetpoint"),
        1558 : RawCodec(6, "MixerFourCircuitFixedValueFlowTemperatureSetpoint"),
        1559 : RawCodec(6, "MixerFiveCircuitFixedValueFlowTemperatureSetpoint"),
        1560 : RawCodec(6, "MixerSixCircuitFixedValueFlowTemperatureSetpoint"),
        1561 : RawCodec(6, "MixerSevenCircuitFixedValueFlowTemperatureSetpoint"),
        1562 : RawCodec(6, "MixerEightCircuitFixedValueFlowTemperatureSetpoint"),
        1573 : RawCodec(9, "SystemReturnTemperatureSensor"),
        1577 : RawCodec(139, "ElectricalEnergyStorageModuleOneOperatingData"),
        1578 : RawCodec(139, "ElectricalEnergyStorageModuleTwoOperatingData"),
        1579 : RawCodec(139, "ElectricalEnergyStorageModuleThreeOperatingData"),
        1580 : RawCodec(139, "ElectricalEnergyStorageModuleFourOperatingData"),
        1581 : RawCodec(139, "ElectricalEnergyStorageModuleFiveOperatingData"),
        1582 : RawCodec(139, "ElectricalEnergyStorageModuleSixOperatingData"),
        1585 : RawCodec(2, "IncreasedReturnTemperatureSetpoint"),
        1587 : RawCodec(4, "ExternalAlternatingCurrentPowerSetpointMetaData"),
        1588 : RawCodec(4, "AlternatingCurrentPowerSetpoint"),
        1589 : RawCodec(4, "AlternatingCurrentPowerSetpointMetaData"),
        1590 : RawCodec(6, "ElectricalEnergySystemOperationState"),
        1591 : RawCodec(6, "ElectricalEnergyInverterOperationState"),
        1592 : RawCodec(1, "ElectricalEnergyInverterPath"),
        1593 : RawCodec(4, "BufferHysteresis"),
        1594 : O3ESdate(3, "LastApplicationUpdate"),
        1595 : RawCodec(8, "ParameterIdentificationVersionFactory"),
        1596 : RawCodec(9, "IncreasedReturnTemperatureSensor"),
        1598 : RawCodec(4, "SolarStaticTemperatureControlHysteresis"),
        1599 : RawCodec(4, "SolarSecondaryDeltaTemperatureHysteresis"),
        1600 : RawCodec(2, "BufferDischargeFunctionThreeWayValvePositionPercent"),
        1601 : RawCodec(1, "FuelCellCondition"),
        1603 : O3EComplexType(4, "PointOfCommonCouplingPower", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        1604 : RawCodec(2, "GatewayExternalTargetFlowTemperatureSetpoint"),
        1605 : O3EComplexType(2, "GatewayExternalHeatEngineTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        1606 : RawCodec(8, "IntervalStrategyProperties"),
        1607 : O3EByteVal(1, "MalfunctionUnitBlocked"),
        1608 : RawCodec(9, "DifferentialTemperatureControllerHeatSourceTemperatureSensor"),
        1609 : RawCodec(9, "DifferentialTemperatureControllerHeatSinkTemperatureSensor"),
        1610 : RawCodec(9, "HeatingSupportBufferTemperatureSensor"),
        1611 : RawCodec(9, "PreheatingReferenceTemperatureSensor"),
        1612 : O3EComplexType(2, "ExternalMixerTwoCircuitTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        1613 : O3EComplexType(2, "ExternalMixerThreeCircuitTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        1614 : O3EComplexType(2, "ExternalMixerFourCircuitTargetOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        1627 : O3EInt16(2, "ExternalMixerOneCircuitFixedValueTargetTemperatureSetpoint", scale = 10, signed=True),
        1628 : O3EInt16(2, "ExternalMixerTwoCircuitFixedValueTargetTemperatureSetpoint", scale = 10, signed=True),
        1629 : O3EInt16(2, "ExternalMixerThreeCircuitFixedValueTargetTemperatureSetpoint", scale = 10, signed=True),
        1630 : O3EInt16(2, "ExternalMixerFourCircuitFixedValueTargetTemperatureSetpoint", scale = 10, signed=True),
        1643 : O3EInt16(2, "MixerOneCircuitCurrentTemperatureSetpoint", scale = 10, signed=True),
        1644 : O3EInt16(2, "MixerTwoCircuitCurrentTemperatureSetpoint", scale = 10, signed=True),
        1645 : O3EInt16(2, "MixerThreeCircuitCurrentTemperatureSetpoint", scale = 10, signed=True),
        1646 : O3EInt16(2, "MixerFourCircuitCurrentTemperatureSetpoint", scale = 10, signed=True),
        1659 : O3EInt16(3, "EndResultDomesticHotWaterTemperatureSetpoint", scale = 10, signed=True),
        1660 : RawCodec(16, "SupportedFeatures"),
        1661 : RawCodec(5, "SolarSecondaryTransferPump"),
        1662 : RawCodec(2, "HeatingSupportBufferThreeWayValvePositionPercent"),
        1663 : RawCodec(41, "TestStatus"),
        1664 : O3EInt8(1, "ElectricalEnergyStorageStateOfCharge"),
        1667 : RawCodec(2, "MixerOneCircuitPumpOscillationTime"),
        1668 : RawCodec(2, "MixerTwoCircuitPumpOscillationTime"),
        1669 : RawCodec(2, "MixerThreeCircuitPumpOscillationTime"),
        1670 : RawCodec(2, "MixerFourCircuitPumpOscillationTime"),
        1684 : O3EComplexType(9, "AmbientTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1685 : RawCodec(3, "ElectricalEnergyInverterDCConfiguration"),
        1686 : RawCodec(3, "ElectricalEnergySystemPhotovoltaicLimitation"),
        1687 : O3EInt16(2, "ElectricalEnergySystemPhotovoltaicConfiguration", scale=10),
        1690 : O3EComplexType(17, "ElectricalEnergySystemPhotovoltaicStatus", 
                                  [O3EInt16(2, "ActivePower cumulated", scale=1.0, signed=True), O3EInt16(2, "RectivePower cumulated", scale=1.0, signed=True),
                                   O3EInt16(2, "ActivePower String C", scale=1.0, signed=True), O3EInt16(2, "RectivePower String C", scale=1.0, signed=True),
                                   O3EInt16(2, "ActivePower String B", scale=1.0, signed=True), O3EInt16(2, "RectivePower String B", scale=1.0, signed=True),
                                   O3EInt16(2, "ActivePower String A", scale=1.0, signed=True), O3EInt16(2, "RectivePower String A", scale=1.0, signed=True),
                                   O3EInt8(1, "OpMode", scale=1.0, signed=False)]),
        1691 : O3EByteVal(1, "BusTopologyScanStatus"),
        1692 : RawCodec(1, "PowerGridCodeConfiguration"),
        1693 : O3EByteVal(1, "GridOperatorConfigurationLock"),
        1694 : O3EByteVal(1, "GatewayEthernetEnable"),
        1695 : RawCodec(21, "GatewayEthernetConfig"),
        1696 : RawCodec(20, "GatewayEthernetIp"),
        1697 : O3EByteVal(1, "GatewayEthernetNetworkStatus"),
        1698 : RawCodec(16, "SupportedFeaturesTelemetryControlUnit"),
        1699 : RawCodec(16, "ActivatedFeaturesTelemetryControlUnit"),
        1700 : RawCodec(104, "EebusDeviceList"),
        1701 : RawCodec(104, "EebusOwnInfo"),
        1702 : RawCodec(104, "EebusPartnerInfo"),
        1703 : RawCodec(1, "EebusConnectionStatus"),
        1706 : RawCodec(1, "GenericMZIOAccessoryTwoModuleFunction"),
        1710 : O3ESoftVers(8, "FunctionalSoftwareVersion"),
        1718 : O3EComplexType(2, "ElectricalEnergySystemConfiguration", [O3EByteVal(1, "Netzbetriebsart"), O3EByteVal(1, "Elektrische Anlagenkomponenten")]),
        1719 : RawCodec(3, "SolarIntervalFunction"),
        1721 : RawCodec(8, "WaterPressureConfiguration"),
        1728 : RawCodec(2, "ThermostatTerminalOneCircuitPump"),
        1729 : RawCodec(2, "ThermostatTerminalTwoCircuitPump"),
        1730 : RawCodec(2, "ThermostatTerminalThreeCircuitPump"),
        1731 : O3EByteVal(1, "ExternalLockActive"),
        1732 : RawCodec(6, "FixedRoomTemperatureSetpoint"),
        1749 : RawCodec(176, "TimeSeriesRecordedModulationCurrentValueStepsAndDurationOne"),
        1750 : RawCodec(176, "TimeSeriesRecordedModulationCurrentValueStepsAndDurationTwo"),
        1751 : RawCodec(132, "TimeSeriesRecordedModulationCurrentValueStepsAndDurationThree"),
        1752 : RawCodec(176, "TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationOne"),
        1753 : RawCodec(176, "TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationTwo"),
        1754 : RawCodec(132, "TimeSeriesRecordedFlowTemperatureSensorStepsAndDurationThree"),
        1759 : RawCodec(40, "TimeSeriesRecordedDomesticHotWaterOutletTemperature"),
        1760 : RawCodec(40, "TimeSeriesRecordedCombustionAirInletTemperature"),
        1761 : RawCodec(40, "TimeSeriesRecordedCentralHeatingPumpSpeed"),
        1762 : RawCodec(1, "LowWaterCutOffSignalInput"),
        1763 : RawCodec(1, "LowGasPressureSignalInput"),
        1764 : RawCodec(1, "HighGasPressureSignalInput"),
        1765 : RawCodec(2, "CombustionAirInterlock"),
        1768 : O3EComplexType(9, "ReceiverTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1769 : O3EComplexType(9, "PrimaryInletTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1770 : O3EComplexType(9, "SecondaryOutletTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1771 : O3EComplexType(9, "EngineRoomTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1772 : O3EComplexType(9, "CompressorOilTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        1773 : O3EByteVal(1, "RefrigerantCircuitFourWayValve"),
        1774 : O3EByteVal(1, "CompressorCrankCaseHeater"),
        1775 : O3EByteVal(1, "PrimaryCircuitFanOne"),
        1776 : O3EByteVal(1, "PrimaryCircuitFanTwo"),
        1777 : RawCodec(176, "TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationOne"),
        1778 : RawCodec(176, "TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationTwo"),
        1779 : RawCodec(132, "TimeSeriesRecordedFlueGasTemperatureSensorStepsAndDurationThree"),
        1780 : RawCodec(80, "TimeSeriesRecordedIgnitionTimeSteps"),
        1781 : RawCodec(16, "TimeSeriesRecordedCalibrationCount"),
        1782 : RawCodec(56, "TimeSeriesRecordedMonitoringIonizationMaximum"),
        1783 : RawCodec(120, "TimeSeriesRecordedHeatingBurnerStopEvents"),
        1784 : RawCodec(120, "TimeSeriesRecordedDomesticHotWaterBurnerStopEvents"),
        1785 : RawCodec(40, "TimeSeriesRecordedFlameLossModulation"),
        1786 : RawCodec(52, "TimeSeriesRecordedWaterPressureStagnation"),
        1787 : RawCodec(32, "TimeSeriesRecordedWaterPressurePeaks"),
        1788 : RawCodec(8, "CanInterfaceVersion"),            
        1791 : O3EByteVal(1, "DiverterValveDefaultPositionConfiguration"),
        1792 : RawCodec(1, "ResetElectricalEnergyHistory"),
        1793 : RawCodec(1, "BurnerPreconditions"),
        1794 : RawCodec(4, "HeatingCircuitHeatDeficit"),
        1795 : RawCodec(1, "FuelCellRuntimePrediction"),
        1796 : RawCodec(2, "DomesticElectricalEnergyConsumption"),
        1797 : RawCodec(2, "PredictionDomesticElectricalEnergyConsumptionNextHour"),
        1798 : RawCodec(1, "FuelCellHoursTillNextStart"),
        1799 : O3EInt16(2, "PrimaryCircuitCurrentTemperatureSetpoint", scale = 10, signed=True),
        1800 : RawCodec(4, "ResetTimeSeriesRecordingGroups"),
        1801 : O3EComplexType(40, "ElectricalEnergyStorageEnergyTransferStatistic", [O3EInt32(4, "BatteryChargeToday", scale=1.0), O3EInt32(4, "BatteryChargeWeek", scale=1.0), O3EInt32(4, "BatteryChargeMonth", scale=1.0), O3EInt32(4, "BatteryChargeYear", scale=1.0), O3EInt32(4, "BatteryChargeTotal", scale=1.0), O3EInt32(4, "BatteryDischargeToday", scale=1.0), O3EInt32(4, "BatteryDischargeWeek", scale=1.0), O3EInt32(4, "BatteryDischargeMonth", scale=1.0), O3EInt32(4, "BatteryDischargeYear", scale=1.0), O3EInt32(4, "BatteryDischargeTotal", scale=1.0)]),
        1802 : O3EComplexType(80, "EnergyProductionPhotovoltaic", [O3EInt32(4, "PhotovoltaicProductionToday"), O3EInt32(4, "PhotovoltaicProductionWeek"), O3EInt32(4, "PhotovoltaicProductionMonth"), O3EInt32(4, "PhotovoltaicProductionYear"), O3EInt32(4, "PhotovoltaicProductionTotal"), O3EInt32(4, "PhotovoltaicProductionToday1"), O3EInt32(4, "PhotovoltaicProductionWeek1"), O3EInt32(4, "PhotovoltaicProductionMonth1"), O3EInt32(4, "PhotovoltaicProductionYear1"), O3EInt32(4, "PhotovoltaicProductionTotal1"), O3EInt32(4, "PhotovoltaicProductionToday2"), O3EInt32(4, "PhotovoltaicProductionWeek2"), O3EInt32(4, "PhotovoltaicProductionMonth2"), O3EInt32(4, "PhotovoltaicProductionYear2"), O3EInt32(4, "PhotovoltaicProductionTotal2"), O3EInt32(4, "PhotovoltaicProductionToday3"), O3EInt32(4, "PhotovoltaicProductionWeek3"), O3EInt32(4, "PhotovoltaicProductionMonth3"), O3EInt32(4, "PhotovoltaicProductionYear3"), O3EInt32(4, "PhotovoltaicProductionTotal3")]),
        1807 : RawCodec(10, "ElectricalEnergyInverterDcInputOne"),
        1808 : RawCodec(10, "ElectricalEnergyInverterDcInputTwo"),
        1809 : RawCodec(10, "ElectricalEnergyInverterDcInputThree"),
        1810 : O3EComplexType(4, "ElectricalEnergyInverterPowerAc", [O3EInt16(2, "ActivePower", scale=1.0, signed=True), O3EInt16(2, "ReactivePower", scale=1.0, signed=True)]),
        1811 : RawCodec(1, "ElectricalEnergyStorageModuleSetUpCheck"),
        1812 : RawCodec(2, "PointOfCommonCouplingConfiguredEnergyMeter"),
        1813 : O3EInt8(1, "EnhancedVapourInjectionValve"),#+++
        1814 : RawCodec(5, "ReceiverLiquidLevelSensor"),
        1815 : O3EInt8(1, "ElectricalHeaterPhaseOne"),
        1816 : O3EInt8(1, "ElectricalHeaterPhaseTwo"),
        1817 : O3EInt8(1, "ElectricalHeaterPhaseThree"),
        1819 : O3EByteVal(1, "SolarPumpConfigurationSelection"),
        1822 : RawCodec(51, "ThreePhaseInverterCurrent"),
        1823 : RawCodec(27, "ThreePhaseInverterVoltage"),
        1824 : O3EComplexType(16, "ThreePhaseInverterCurrentPower", [O3EInt32(4, "cumulated", scale=1, signed=True), O3EInt32(4, "L1", scale=1, signed=True), O3EInt32(4, "L2", scale=1, signed=True), O3EInt32(4, "L3", scale=1, signed=True)]),
        1825 : O3EComplexType(16, "ThreePhaseInverterCurrentApparentPower", [O3EInt32(4, "cumulated", scale=1, signed=True), O3EInt32(4, "L1", scale=1, signed=True), O3EInt32(4, "L2", scale=1, signed=True), O3EInt32(4, "L3", scale=1, signed=True)]),
        1826 : O3EInt16(4, "ThreePhaseInverterMaximunNominalPower", scale=1.0),
        1827 : O3EInt16(4, "InverterElectricalEnergyStorageMaximumNominalChargePower", scale=1.0),
        1828 : O3EInt16(4, "InverterElectricalEnergyStorageCurrentMaximumlChargePower", scale=1.0),
        1829 : O3EInt16(4, "InverterElectricalEnergyStorageMaximumNominalDischargePower", scale=1.0),
        1830 : O3EInt16(4, "InverterElectricalEnergyStorageCurrentMaximumlDishargePower", scale=1.0),
        1831 : O3EComplexType(12, "PhotovoltaicCurrentStringPower", [O3EInt32(4, "String1", scale=1.0, signed=True), O3EInt32(4, "String2", scale=1.0, signed=True), O3EInt32(4, "String3", scale=1.0, signed=True)]),
        1832 : O3EComplexType(12, "PhotovoltaicStringCurrent", [O3EInt32(4, "String1", scale=1.0, signed=True), O3EInt32(4, "String2", scale=1.0, signed=True), O3EInt32(4, "String3", scale=1.0, signed=True)]),
        1833 : O3EComplexType(12, "PhotovoltaicStringVoltage", [O3EInt32(4, "String1", scale=1000.0, signed=True), O3EInt32(4, "String2", scale=1000.0, signed=True), O3EInt32(4, "String3", scale=1000.0, signed=True)]),
        1834 : O3EComplexType(4, "ElectricalEnergyStorageStateOfEnergy", [O3EInt16(2, "StateOfEnergy", scale=1.0, signed=False), O3EInt16(2, "Unknown", scale=1.0, signed=False)]),            
        1835 : RawCodec(20, "ManufacturerProperties"),
        1836 : O3EInt32(4, "ElectricalEnergyStorageCurrentPower", scale=1.0, signed=True),
        1837 : O3EInt16(4, "ElectricalEnergyStorageCurrent", scale=1.0, signed=True),
        1838 : O3EInt16(2, "ElectricalEnergyStorageVoltage"),
        1839 : RawCodec(4, "ElectricalEnergyStorageUsableEnergy"),
        1840 : RawCodec(4, "ElectricalEnergyStorageUsableNominalEnergy"),
        1841 : RawCodec(32, "PointOfCommonCouplingOverview"),
#        1842 : RawCodec(2, "SecondaryCircuitFourThreeWayValve"),
        1842 : O3EComplexType(2, "SecondaryCircuitFourThreeWayValve", [O3EInt8(1, "Setpoint", signed=True), O3EInt8(1, "CurrentPosition", signed=True)]), #250-xH Unit: %        
        1843 : RawCodec(2, "MixerOneCircuitHumidityProtection"),
        1844 : RawCodec(2, "MixerTwoCircuitHumidityProtection"),
        1845 : RawCodec(36, "HeatPumpCompressorEnvelope"),#+++
        1846 : RawCodec(4, "HeatPumpCompressorCurrentOperatingPoint"),#+++
        1847 : RawCodec(81, "CustomerDetailsExtensions"),
        1848 : RawCodec(27, "ApartmentOneProperty"),
        1849 : RawCodec(50, "ApartmentOneSetpoints"),
        1850 : RawCodec(57, "ApartmentOneTimeScheduleMonday"),
        1851 : RawCodec(57, "ApartmentOneTimeScheduleTuesday"),
        1852 : RawCodec(57, "ApartmentOneTimeScheduleWednesday"),
        1853 : RawCodec(57, "ApartmentOneTimeScheduleThursday"),
        1854 : RawCodec(57, "ApartmentOneTimeScheduleFriday"),
        1855 : RawCodec(57, "ApartmentOneTimeScheduleSaturday"),
        1856 : RawCodec(57, "ApartmentOneTimeScheduleSunday"),
        1884 : RawCodec(84, "RoomOneProperty"),#+++ (str, "name"); (o5cVar, "roomType"); (h5cVar, "lockMode"); (c5cVar, "roomControlAlgorithmType"); (list, "supplyChannel"); (list2, "roomDevices");
        1885 : RawCodec(30, "RoomOneSetpoints"),
        1886 : RawCodec(46, "RoomOneCurrentValues"),
        1887 : RawCodec(84, "RoomTwoProperty"),#+++
        1888 : RawCodec(30, "RoomTwoSetpoints"),
        1889 : RawCodec(46, "RoomTwoCurrentValues"),
        1890 : RawCodec(84, "RoomThreeProperty"),#+++
        1891 : RawCodec(30, "RoomThreeSetpoints"),
        1892 : RawCodec(46, "RoomThreeCurrentValues"),
        1893 : RawCodec(84, "RoomFourProperty"),#+++
        1894 : RawCodec(30, "RoomFourSetpoints"),
        1895 : RawCodec(46, "RoomFourCurrentValues"),
        1896 : RawCodec(84, "RoomFiveProperty"),#+++
        1897 : RawCodec(30, "RoomFiveSetpoints"),
        1898 : RawCodec(46, "RoomFiveCurrentValues"),
        1899 : RawCodec(84, "RoomSixProperty"),#+++
        1900 : RawCodec(30, "RoomSixSetpoints"),
        1901 : RawCodec(46, "RoomSixCurrentValues"),
        1902 : RawCodec(84, "RoomSevenProperty"),#+++
        1903 : RawCodec(30, "RoomSevenSetpoints"),
        1904 : RawCodec(46, "RoomSevenCurrentValues"),
        1905 : RawCodec(84, "RoomEightProperty"),#+++
        1906 : RawCodec(30, "RoomEightSetpoints"),
        1907 : RawCodec(46, "RoomEightCurrentValues"),
        1908 : RawCodec(84, "RoomNineProperty"),#+++
        1909 : RawCodec(30, "RoomNineSetpoints"),
        1910 : RawCodec(46, "RoomNineCurrentValues"),
        1911 : RawCodec(84, "RoomTenProperty"),#+++
        1912 : RawCodec(30, "RoomTenSetpoints"),
        1913 : RawCodec(46, "RoomTenCurrentValues"),
        1914 : RawCodec(84, "RoomElevenProperty"),#+++
        1915 : RawCodec(30, "RoomElevenSetpoints"),
        1916 : RawCodec(46, "RoomElevenCurrentValues"),
        1917 : RawCodec(84, "RoomTwelveProperty"),#+++
        1918 : RawCodec(30, "RoomTwelveSetpoints"),
        1919 : RawCodec(46, "RoomTwelveCurrentValues"),
        1920 : RawCodec(84, "RoomThirteenProperty"),#+++
        1921 : RawCodec(30, "RoomThirteenSetpoints"),
        1922 : RawCodec(46, "RoomThirteenCurrentValues"),
        1923 : RawCodec(84, "RoomFourteenProperty"),#+++
        1924 : RawCodec(30, "RoomFourteenSetpoints"),
        1925 : RawCodec(46, "RoomFourteenCurrentValues"),
        1926 : RawCodec(84, "RoomFifteenProperty"),#+++
        1927 : RawCodec(30, "RoomFifteenSetpoints"),
        1928 : RawCodec(46, "RoomFifteenCurrentValues"),
        1929 : RawCodec(84, "RoomSixteenProperty"),#+++
        1930 : RawCodec(30, "RoomSixteenSetpoints"),
        1931 : RawCodec(46, "RoomSixteenCurrentValues"),
        1932 : RawCodec(84, "RoomSeventeenProperty"),#+++
        1933 : RawCodec(30, "RoomSeventeenSetpoints"),
        1934 : RawCodec(46, "RoomSeventeenCurrentValues"),
        1935 : RawCodec(84, "RoomEighteenProperty"),#+++
        1936 : RawCodec(30, "RoomEighteenSetpoints"),
        1937 : RawCodec(46, "RoomEighteenCurrentValues"),
        1938 : RawCodec(84, "RoomNineteenProperty"),#+++
        1939 : RawCodec(30, "RoomNineteenSetpoints"),
        1940 : RawCodec(46, "RoomNineteenCurrentValues"),
        1941 : RawCodec(84, "RoomTwentyProperty"),#+++
        1942 : RawCodec(30, "RoomTwentySetpoints"),
        1943 : RawCodec(46, "RoomTwentyCurrentValues"),
        1944 : RawCodec(57, "RoomOneTimeScheduleMonday"),
        1945 : RawCodec(57, "RoomOneTimeScheduleTuesday"),
        1946 : RawCodec(57, "RoomOneTimeScheduleWednesday"),
        1947 : RawCodec(57, "RoomOneTimeScheduleThursday"),
        1948 : RawCodec(57, "RoomOneTimeScheduleFriday"),
        1949 : RawCodec(57, "RoomOneTimeScheduleSaturday"),
        1950 : RawCodec(57, "RoomOneTimeScheduleSunday"),
        1951 : RawCodec(57, "RoomTwoTimeScheduleMonday"),
        1952 : RawCodec(57, "RoomTwoTimeScheduleTuesday"),
        1953 : RawCodec(57, "RoomTwoTimeScheduleWednesday"),
        1954 : RawCodec(57, "RoomTwoTimeScheduleThursday"),
        1955 : RawCodec(57, "RoomTwoTimeScheduleFriday"),
        1956 : RawCodec(57, "RoomTwoTimeScheduleSaturday"),
        1957 : RawCodec(57, "RoomTwoTimeScheduleSunday"),
        1958 : RawCodec(57, "RoomThreeTimeScheduleMonday"),
        1959 : RawCodec(57, "RoomThreeTimeScheduleTuesday"),
        1960 : RawCodec(57, "RoomThreeTimeScheduleWednesday"),
        1961 : RawCodec(57, "RoomThreeTimeScheduleThursday"),
        1962 : RawCodec(57, "RoomThreeTimeScheduleFriday"),
        1963 : RawCodec(57, "RoomThreeTimeScheduleSaturday"),
        1964 : RawCodec(57, "RoomThreeTimeScheduleSunday"),
        1965 : RawCodec(57, "RoomFourTimeScheduleMonday"),
        1966 : RawCodec(57, "RoomFourTimeScheduleTuesday"),
        1967 : RawCodec(57, "RoomFourTimeScheduleWednesday"),
        1968 : RawCodec(57, "RoomFourTimeScheduleThursday"),
        1969 : RawCodec(57, "RoomFourTimeScheduleFriday"),
        1970 : RawCodec(57, "RoomFourTimeScheduleSaturday"),
        1971 : RawCodec(57, "RoomFourTimeScheduleSunday"),
        1972 : RawCodec(57, "RoomFiveTimeScheduleMonday"),
        1973 : RawCodec(57, "RoomFiveTimeScheduleTuesday"),
        1974 : RawCodec(57, "RoomFiveTimeScheduleWednesday"),
        1975 : RawCodec(57, "RoomFiveTimeScheduleThursday"),
        1976 : RawCodec(57, "RoomFiveTimeScheduleFriday"),
        1977 : RawCodec(57, "RoomFiveTimeScheduleSaturday"),
        1978 : RawCodec(57, "RoomFiveTimeScheduleSunday"),
        1979 : RawCodec(57, "RoomSixTimeScheduleMonday"),
        1980 : RawCodec(57, "RoomSixTimeScheduleTuesday"),
        1981 : RawCodec(57, "RoomSixTimeScheduleWednesday"),
        1982 : RawCodec(57, "RoomSixTimeScheduleThursday"),
        1983 : RawCodec(57, "RoomSixTimeScheduleFriday"),
        1984 : RawCodec(57, "RoomSixTimeScheduleSaturday"),
        1985 : RawCodec(57, "RoomSixTimeScheduleSunday"),
        1986 : RawCodec(57, "RoomSevenTimeScheduleMonday"),
        1987 : RawCodec(57, "RoomSevenTimeScheduleTuesday"),
        1988 : RawCodec(57, "RoomSevenTimeScheduleWednesday"),
        1989 : RawCodec(57, "RoomSevenTimeScheduleThursday"),
        1990 : RawCodec(57, "RoomSevenTimeScheduleFriday"),
        1991 : RawCodec(57, "RoomSevenTimeScheduleSaturday"),
        1992 : RawCodec(57, "RoomSevenTimeScheduleSunday"),
        1993 : RawCodec(57, "RoomEightTimeScheduleMonday"),
        1994 : RawCodec(57, "RoomEightTimeScheduleTuesday"),
        1995 : RawCodec(57, "RoomEightTimeScheduleWednesday"),
        1996 : RawCodec(57, "RoomEightTimeScheduleThursday"),
        1997 : RawCodec(57, "RoomEightTimeScheduleFriday"),
        1998 : RawCodec(57, "RoomEightTimeScheduleSaturday"),
        1999 : RawCodec(57, "RoomEightTimeScheduleSunday"),
        2000 : RawCodec(57, "RoomNineTimeScheduleMonday"),
        2001 : RawCodec(57, "RoomNineTimeScheduleTuesday"),
        2002 : RawCodec(57, "RoomNineTimeScheduleWednesday"),
        2003 : RawCodec(57, "RoomNineTimeScheduleThursday"),
        2004 : RawCodec(57, "RoomNineTimeScheduleFriday"),
        2005 : RawCodec(57, "RoomNineTimeScheduleSaturday"),
        2006 : RawCodec(57, "RoomNineTimeScheduleSunday"),
        2007 : RawCodec(57, "RoomTenTimeScheduleMonday"),
        2008 : RawCodec(57, "RoomTenTimeScheduleTuesday"),
        2009 : RawCodec(57, "RoomTenTimeScheduleWednesday"),
        2010 : RawCodec(57, "RoomTenTimeScheduleThursday"),
        2011 : RawCodec(57, "RoomTenTimeScheduleFriday"),
        2012 : RawCodec(57, "RoomTenTimeScheduleSaturday"),
        2013 : RawCodec(57, "RoomTenTimeScheduleSunday"),
        2014 : RawCodec(57, "RoomElevenTimeScheduleMonday"),
        2015 : RawCodec(57, "RoomElevenTimeScheduleTuesday"),
        2016 : RawCodec(57, "RoomElevenTimeScheduleWednesday"),
        2017 : RawCodec(57, "RoomElevenTimeScheduleThursday"),
        2018 : RawCodec(57, "RoomElevenTimeScheduleFriday"),
        2019 : RawCodec(57, "RoomElevenTimeScheduleSaturday"),
        2020 : RawCodec(57, "RoomElevenTimeScheduleSunday"),
        2021 : RawCodec(57, "RoomTwelveTimeScheduleMonday"),
        2022 : RawCodec(57, "RoomTwelveTimeScheduleTuesday"),
        2023 : RawCodec(57, "RoomTwelveTimeScheduleWednesday"),
        2024 : RawCodec(57, "RoomTwelveTimeScheduleThursday"),
        2025 : RawCodec(57, "RoomTwelveTimeScheduleFriday"),
        2026 : RawCodec(57, "RoomTwelveTimeScheduleSaturday"),
        2027 : RawCodec(57, "RoomTwelveTimeScheduleSunday"),
        2028 : RawCodec(57, "RoomThirteenTimeScheduleMonday"),
        2029 : RawCodec(57, "RoomThirteenTimeScheduleTuesday"),
        2030 : RawCodec(57, "RoomThirteenTimeScheduleWednesday"),
        2031 : RawCodec(57, "RoomThirteenTimeScheduleThursday"),
        2032 : RawCodec(57, "RoomThirteenTimeScheduleFriday"),
        2033 : RawCodec(57, "RoomThirteenTimeScheduleSaturday"),
        2034 : RawCodec(57, "RoomThirteenTimeScheduleSunday"),
        2035 : RawCodec(57, "RoomFourteenTimeScheduleMonday"),
        2036 : RawCodec(57, "RoomFourteenTimeScheduleTuesday"),
        2037 : RawCodec(57, "RoomFourteenTimeScheduleWednesday"),
        2038 : RawCodec(57, "RoomFourteenTimeScheduleThursday"),
        2039 : RawCodec(57, "RoomFourteenTimeScheduleFriday"),
        2040 : RawCodec(57, "RoomFourteenTimeScheduleSaturday"),
        2041 : RawCodec(57, "RoomFourteenTimeScheduleSunday"),
        2042 : RawCodec(57, "RoomFifteenTimeScheduleMonday"),
        2043 : RawCodec(57, "RoomFifteenTimeScheduleTuesday"),
        2044 : RawCodec(57, "RoomFifteenTimeScheduleWednesday"),
        2045 : RawCodec(57, "RoomFifteenTimeScheduleThursday"),
        2046 : RawCodec(57, "RoomFifteenTimeScheduleFriday"),
        2047 : RawCodec(57, "RoomFifteenTimeScheduleSaturday"),
        2048 : RawCodec(57, "RoomFifteenTimeScheduleSunday"),
        2049 : RawCodec(57, "RoomSixteenTimeScheduleMonday"),
        2050 : RawCodec(57, "RoomSixteenTimeScheduleTuesday"),
        2051 : RawCodec(57, "RoomSixteenTimeScheduleWednesday"),
        2052 : RawCodec(57, "RoomSixteenTimeScheduleThursday"),
        2053 : RawCodec(57, "RoomSixteenTimeScheduleFriday"),
        2054 : RawCodec(57, "RoomSixteenTimeScheduleSaturday"),
        2055 : RawCodec(57, "RoomSixteenTimeScheduleSunday"),
        2056 : RawCodec(57, "RoomSeventeenTimeScheduleMonday"),
        2057 : RawCodec(57, "RoomSeventeenTimeScheduleTuesday"),
        2058 : RawCodec(57, "RoomSeventeenTimeScheduleWednesday"),
        2059 : RawCodec(57, "RoomSeventeenTimeScheduleThursday"),
        2060 : RawCodec(57, "RoomSeventeenTimeScheduleFriday"),
        2061 : RawCodec(57, "RoomSeventeenTimeScheduleSaturday"),
        2062 : RawCodec(57, "RoomSeventeenTimeScheduleSunday"),
        2063 : RawCodec(57, "RoomEighteenTimeScheduleMonday"),
        2064 : RawCodec(57, "RoomEighteenTimeScheduleTuesday"),
        2065 : RawCodec(57, "RoomEighteenTimeScheduleWednesday"),
        2066 : RawCodec(57, "RoomEighteenTimeScheduleThursday"),
        2067 : RawCodec(57, "RoomEighteenTimeScheduleFriday"),
        2068 : RawCodec(57, "RoomEighteenTimeScheduleSaturday"),
        2069 : RawCodec(57, "RoomEighteenTimeScheduleSunday"),
        2070 : RawCodec(57, "RoomNineteenTimeScheduleMonday"),
        2071 : RawCodec(57, "RoomNineteenTimeScheduleTuesday"),
        2072 : RawCodec(57, "RoomNineteenTimeScheduleWednesday"),
        2073 : RawCodec(57, "RoomNineteenTimeScheduleThursday"),
        2074 : RawCodec(57, "RoomNineteenTimeScheduleFriday"),
        2075 : RawCodec(57, "RoomNineteenTimeScheduleSaturday"),
        2076 : RawCodec(57, "RoomNineteenTimeScheduleSunday"),
        2077 : RawCodec(57, "RoomTwentyTimeScheduleMonday"),
        2078 : RawCodec(57, "RoomTwentyTimeScheduleTuesday"),
        2079 : RawCodec(57, "RoomTwentyTimeScheduleWednesday"),
        2080 : RawCodec(57, "RoomTwentyTimeScheduleThursday"),
        2081 : RawCodec(57, "RoomTwentyTimeScheduleFriday"),
        2082 : RawCodec(57, "RoomTwentyTimeScheduleSaturday"),
        2083 : RawCodec(57, "RoomTwentyTimeScheduleSunday"),
        2084 : RawCodec(84, "ZigBeeOneDeviceProperty"),#+++
        2085 : RawCodec(13, "ZigBeeOneDeviceSetpoint"),#+++
        2086 : RawCodec(57, "ZigBeeOneDeviceCurrentValues"),#+++
        2087 : RawCodec(84, "ZigBeeTwoDeviceProperty"),#+++
        2088 : RawCodec(13, "ZigBeeTwoDeviceSetpoint"),#+++
        2089 : RawCodec(57, "ZigBeeTwoDeviceCurrentValues"),#+++
        2090 : RawCodec(84, "ZigBeeThreeDeviceProperty"),#+++
        2091 : RawCodec(13, "ZigBeeThreeDeviceSetpoint"),#+++
        2092 : RawCodec(57, "ZigBeeThreeDeviceCurrentValues"),#+++
        2093 : RawCodec(84, "ZigBeeFourDeviceProperty"),#+++
        2094 : RawCodec(13, "ZigBeeFourDeviceSetpoint"),#+++
        2095 : RawCodec(57, "ZigBeeFourDeviceCurrentValues"),#+++
        2096 : RawCodec(84, "ZigBeeFiveDeviceProperty"),#+++
        2097 : RawCodec(13, "ZigBeeFiveDeviceSetpoint"),#+++
        2098 : RawCodec(57, "ZigBeeFiveDeviceCurrentValues"),#+++
        2099 : RawCodec(84, "ZigBeeSixDeviceProperty"),#+++
        2100 : RawCodec(13, "ZigBeeSixDeviceSetpoint"),#+++
        2101 : RawCodec(57, "ZigBeeSixDeviceCurrentValues"),#+++
        2102 : RawCodec(84, "ZigBeeSevenDeviceProperty"),#+++
        2103 : RawCodec(13, "ZigBeeSevenDeviceSetpoint"),#+++
        2104 : RawCodec(57, "ZigBeeSevenDeviceCurrentValues"),#+++
        2105 : RawCodec(84, "ZigBeeEightDeviceProperty"),#+++
        2106 : RawCodec(13, "ZigBeeEightDeviceSetpoint"),#+++
        2107 : RawCodec(57, "ZigBeeEightDeviceCurrentValues"),#+++
        2108 : RawCodec(84, "ZigBeeNineDeviceProperty"),#+++
        2109 : RawCodec(13, "ZigBeeNineDeviceSetpoint"),#+++
        2110 : RawCodec(57, "ZigBeeNineDeviceCurrentValues"),#+++
        2111 : RawCodec(84, "ZigBeeTenDeviceProperty"),#+++
        2112 : RawCodec(13, "ZigBeeTenDeviceSetpoint"),#+++
        2113 : RawCodec(57, "ZigBeeTenDeviceCurrentValues"),#+++
        2114 : RawCodec(84, "ZigBeeElevenDeviceProperty"),#+++
        2115 : RawCodec(13, "ZigBeeElevenDeviceSetpoint"),#+++
        2116 : RawCodec(57, "ZigBeeElevenDeviceCurrentValues"),#+++
        2117 : RawCodec(84, "ZigBeeTwelveDeviceProperty"),#+++
        2118 : RawCodec(13, "ZigBeeTwelveDeviceSetpoint"),#+++
        2119 : RawCodec(57, "ZigBeeTwelveDeviceCurrentValues"),#+++
        2120 : RawCodec(84, "ZigBeeThirteenDeviceProperty"),#+++
        2121 : RawCodec(13, "ZigBeeThirteenDeviceSetpoint"),#+++
        2122 : RawCodec(57, "ZigBeeThirteenDeviceCurrentValues"),#+++
        2123 : RawCodec(84, "ZigBeeFourteenDeviceProperty"),#+++
        2124 : RawCodec(13, "ZigBeeFourteenDeviceSetpoint"),#+++
        2125 : RawCodec(57, "ZigBeeFourteenDeviceCurrentValues"),#+++
        2126 : RawCodec(84, "ZigBeeFifteenDeviceProperty"),#+++
        2127 : RawCodec(13, "ZigBeeFifteenDeviceSetpoint"),#+++
        2128 : RawCodec(57, "ZigBeeFifteenDeviceCurrentValues"),#+++
        2129 : RawCodec(84, "ZigBeeSixteenDeviceProperty"),#+++
        2130 : RawCodec(13, "ZigBeeSixteenDeviceSetpoint"),#+++
        2131 : RawCodec(57, "ZigBeeSixteenDeviceCurrentValues"),#+++
        2132 : RawCodec(84, "ZigBeeSeventeenDeviceProperty"),#+++
        2133 : RawCodec(13, "ZigBeeSeventeenDeviceSetpoint"),#+++
        2134 : RawCodec(57, "ZigBeeSeventeenDeviceCurrentValues"),#+++
        2135 : RawCodec(84, "ZigBeeEighteenDeviceProperty"),#+++
        2136 : RawCodec(13, "ZigBeeEighteenDeviceSetpoint"),#+++
        2137 : RawCodec(57, "ZigBeeEighteenDeviceCurrentValues"),#+++
        2138 : RawCodec(84, "ZigBeeNineteenDeviceProperty"),#+++
        2139 : RawCodec(13, "ZigBeeNineteenDeviceSetpoint"),#+++
        2140 : RawCodec(57, "ZigBeeNineteenDeviceCurrentValues"),#+++
        2141 : RawCodec(84, "ZigBeeTwentyDeviceProperty"),#+++
        2142 : RawCodec(13, "ZigBeeTwentyDeviceSetpoint"),#+++
        2143 : RawCodec(57, "ZigBeeTwentyDeviceCurrentValues"),#+++
        2144 : RawCodec(16, "PointOfCommonCouplingAcActiveCurrent"),
        2145 : RawCodec(38, "ObjectTopology"),
        2146 : RawCodec(8, "ZigBeeApartmentOneProperty"),
        2147 : RawCodec(106, "ZigBeeApartmentOneTopology"),
        2158 : RawCodec(16, "ActivatedFeatures"),
        2159 : RawCodec(84, "ApartmentOneCurrentValues"),
        2164 : O3EByteVal(1, "DeviceDigitalInputSixValue"),
        2165 : O3EInt8(1, "DevicePwmOutputThreeValue"),#+++
        2166 : RawCodec(1, "MixerOneCircuitExternalHookupDemandInput"),
        2167 : RawCodec(1, "MixerTwoCircuitExternalHookupDemandInput"),
        2168 : RawCodec(1, "MixerThreeCircuitExternalHookupDemandInput"),
        2169 : RawCodec(1, "MixerFourCircuitExternalHookupDemandInput"),
        2182 : RawCodec(15, "SupportedApartmentFeatures"),
        2183 : RawCodec(15, "ActivatedApartmentFeatures"),
        2184 : RawCodec(2, "BackupBoxTest"),
        2188 : RawCodec(6, "PointOfCommonCouplingSetActivePowerTotal"),
        2189 : RawCodec(104, "EebusDeviceListTwo"),
        2190 : RawCodec(104, "EebusDeviceListThree"),
        2191 : RawCodec(104, "EebusDeviceListFour"),
        2192 : RawCodec(104, "EebusDeviceListFive"),
        2193 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleMonday"),
        2194 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleTuesday"),
        2195 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleWednesday"),
        2196 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleThursday"),
        2197 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleFriday"),
        2198 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleSaturday"),
        2199 : RawCodec(57, "ApartmentOneSupplyChannelTwoTimeScheduleSunday"),
        2200 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleMonday"),
        2201 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleTuesday"),
        2202 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleWednesday"),
        2203 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleThursday"),
        2204 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleFriday"),
        2205 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleSaturday"),
        2206 : RawCodec(57, "ApartmentOneSupplyChannelThreeTimeScheduleSunday"),
        2207 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleMonday"),
        2208 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleTuesday"),
        2209 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleWednesday"),
        2210 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleThursday"),
        2211 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleFriday"),
        2212 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleSaturday"),
        2213 : RawCodec(57, "ApartmentOneSupplyChannelFourTimeScheduleSunday"),
        2214 : O3EComplexType(2, "BackupBoxConfiguration", [O3EInt8(1, "DischargeLimit", scale=1, signed=False),O3EInt8(1, "Unknown", scale=1, signed=False)]),
        2217 : RawCodec(1, "InputDemandSideManagementlReceiver"),
        2218 : RawCodec(4, "RemoteLimitValueDemandSideManagement"),
        2219 : RawCodec(1, "BatteryCalibration"),
        2220 : RawCodec(1, "BatteryReactivePowerMode"),
        2221 : RawCodec(3, "BatteryReactivePowerFixCosinusPhi"),
        2222 : RawCodec(18, "BatteryReactivePower"),
        2223 : RawCodec(15, "BatteryReactivePowerCosinusPhi"),
        2224 : RawCodec(16, "PhotovoltaicsActivePowerLimitation"),
        2225 : RawCodec(12, "ElectricEnergyStorageSetpoint"),
        2226 : RawCodec(12, "ElectricEnergyStorageMaximum"),
        2229 : RawCodec(1, "ThermostatTerminalOneFunction"),
        2230 : RawCodec(1, "ThermostatTerminalTwoFunction"),
        2231 : RawCodec(1, "ThermostatTerminalThreeFunction"),
        2233 : O3EByteVal(1, "PersistentStorageStatus"),
        2234 : RawCodec(27, "PowerGridCodeSettingsNormOne"),
        2235 : RawCodec(65, "CascadeSystemConfiguration"),
        2236 : RawCodec(10, "CascadeDeviceSetpoint"),
        2237 : RawCodec(18, "CascadeDeviceStatus"),
        2239 : RawCodec(1, "ElectricEnergyStorageControlMode"),
        2240 : O3EComplexType(9, "BatteryTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        2241 : RawCodec(1, "OutsideTemperatureSensorSource"),
        2242 : RawCodec(27, "PowerGridCodeSettingsNormTwo"),
        2244 : RawCodec(27, "PowerGridCodeSettingsNormFour"),
        2246 : RawCodec(26, "FixReactivePowerIn"),
        2247 : O3EComplexType(12, "FilterRuntime",[O3EInt32(4, "Actual", scale=1.0), O3EInt32(4, "Remaining", scale=1.0), O3EInt32(4, "Overdue", scale=1.0)]),
        2248 : O3EByteVal(1, "CurrentVentilationHeatRecovery"),
        2249 : RawCodec(8, "DigitalSwitchSettingOne"),
        2250 : RawCodec(8, "DigitalSwitchSettingTwo"),
        2251 : RawCodec(8, "LedStatusOne"),
        2252 : RawCodec(8, "LedStatusTwo"),
        2253 : O3EByteVal(1, "DeviceDigitalInputSevenValue"),
        2254 : RawCodec(1, "PowerGridCodeSettingConfiguration"),
        2255 : O3EInt16(2, "MinimumSecondaryReturnTemperatureRefrigerantCircuit", signed=True),
        2256 : O3EInt16(2, "DesiredThermalEnergyDefrost"),
        2257 : O3EInt16(2, "DomesticHotWaterTemperatureSetpointOffset", signed=True),
        2259 : O3EByteVal(1, "RefrigerationCircuitStatus"),
        2260 : RawCodec(84, "ZigBeeTwentyOneDeviceProperty"),#+++
        2261 : RawCodec(13, "ZigBeeTwentyOneDeviceSetpoint"),#+++
        2262 : RawCodec(57, "ZigBeeTwentyOneDeviceCurrentValues"),#+++
        2263 : RawCodec(84, "ZigBeeTwentyTwoDeviceProperty"),#+++
        2264 : RawCodec(13, "ZigBeeTwentyTwoDeviceSetpoint"),#+++
        2265 : RawCodec(57, "ZigBeeTwentyTwoDeviceCurrentValues"),#+++
        2266 : RawCodec(84, "ZigBeeTwentyThreeDeviceProperty"),#+++
        2267 : RawCodec(13, "ZigBeeTwentyThreeDeviceSetpoint"),#+++
        2268 : RawCodec(57, "ZigBeeTwentyThreeDeviceCurrentValues"),#+++
        2269 : RawCodec(84, "ZigBeeTwentyFourDeviceProperty"),#+++
        2270 : RawCodec(13, "ZigBeeTwentyFourDeviceSetpoint"),#+++
        2271 : RawCodec(57, "ZigBeeTwentyFourDeviceCurrentValues"),#+++
        2272 : RawCodec(84, "ZigBeeTwentyFiveDeviceProperty"),#+++
        2273 : RawCodec(13, "ZigBeeTwentyFiveDeviceSetpoint"),#+++
        2274 : RawCodec(57, "ZigBeeTwentyFiveDeviceCurrentValues"),#+++
        2275 : RawCodec(84, "ZigBeeTwentySixDeviceProperty"),#+++
        2276 : RawCodec(13, "ZigBeeTwentySixDeviceSetpoint"),#+++
        2277 : RawCodec(57, "ZigBeeTwentySixDeviceCurrentValues"),#+++
        2278 : RawCodec(84, "ZigBeeTwentySevenDeviceProperty"),#+++
        2279 : RawCodec(13, "ZigBeeTwentySevenDeviceSetpoint"),#+++
        2280 : RawCodec(57, "ZigBeeTwentySevenDeviceCurrentValues"),#+++
        2281 : RawCodec(84, "ZigBeeTwentyEightDeviceProperty"),#+++
        2282 : RawCodec(13, "ZigBeeTwentyEightDeviceSetpoint"),#+++
        2283 : RawCodec(57, "ZigBeeTwentyEightDeviceCurrentValues"),#+++
        2284 : RawCodec(84, "ZigBeeTwentyNineDeviceProperty"),#+++
        2285 : RawCodec(13, "ZigBeeTwentyNineDeviceSetpoint"),#+++
        2286 : RawCodec(57, "ZigBeeTwentyNineDeviceCurrentValues"),#+++
        2287 : RawCodec(84, "ZigBeeThirtyDeviceProperty"),#+++
        2288 : RawCodec(13, "ZigBeeThirtyDeviceSetpoint"),#+++
        2289 : RawCodec(57, "ZigBeeThirtyDeviceCurrentValues"),#+++
        2290 : RawCodec(84, "ZigBeeThirtyOneDeviceProperty"),#+++
        2291 : RawCodec(13, "ZigBeeThirtyOneDeviceSetpoint"),#+++
        2292 : RawCodec(57, "ZigBeeThirtyOneDeviceCurrentValues"),#+++
        2293 : RawCodec(84, "ZigBeeThirtyTwoDeviceProperty"),#+++
        2294 : RawCodec(13, "ZigBeeThirtyTwoDeviceSetpoint"),#+++
        2295 : RawCodec(57, "ZigBeeThirtyTwoDeviceCurrentValues"),#+++
        2296 : RawCodec(84, "ZigBeeThirtyThreeDeviceProperty"),#+++
        2297 : RawCodec(13, "ZigBeeThirtyThreeDeviceSetpoint"),#+++
        2298 : RawCodec(57, "ZigBeeThirtyThreeDeviceCurrentValues"),#+++
        2299 : RawCodec(84, "ZigBeeThirtyFourDeviceProperty"),#+++
        2300 : RawCodec(13, "ZigBeeThirtyFourDeviceSetpoint"),#+++
        2301 : RawCodec(57, "ZigBeeThirtyFourDeviceCurrentValues"),#+++
        2302 : RawCodec(84, "ZigBeeThirtyFiveDeviceProperty"),#+++
        2303 : RawCodec(13, "ZigBeeThirtyFiveDeviceSetpoint"),#+++
        2304 : RawCodec(57, "ZigBeeThirtyFiveDeviceCurrentValues"),#+++
        2305 : RawCodec(84, "ZigBeeThirtySixDeviceProperty"),#+++
        2306 : RawCodec(13, "ZigBeeThirtySixDeviceSetpoint"),#+++
        2307 : RawCodec(57, "ZigBeeThirtySixDeviceCurrentValues"),#+++
        2308 : RawCodec(84, "ZigBeeThirtySevenDeviceProperty"),#+++
        2309 : RawCodec(13, "ZigBeeThirtySevenDeviceSetpoint"),#+++
        2310 : RawCodec(57, "ZigBeeThirtySevenDeviceCurrentValues"),#+++
        2311 : RawCodec(84, "ZigBeeThirtyEightDeviceProperty"),#+++
        2312 : RawCodec(13, "ZigBeeThirtyEightDeviceSetpoint"),#+++
        2313 : RawCodec(57, "ZigBeeThirtyEightDeviceCurrentValues"),#+++
        2314 : RawCodec(84, "ZigBeeThirtyNineDeviceProperty"),#+++
        2315 : RawCodec(13, "ZigBeeThirtyNineDeviceSetpoint"),#+++
        2316 : RawCodec(57, "ZigBeeThirtyNineDeviceCurrentValues"),#+++
        2317 : RawCodec(84, "ZigBeeFourtyDeviceProperty"),#+++
        2318 : RawCodec(13, "ZigBeeFourtyDeviceSetpoint"),#+++
        2319 : RawCodec(57, "ZigBeeFourtyDeviceCurrentValues"),#+++
        2320 : O3EByteVal(1, "DomesticHotWaterStatus"),# 0 = Idle, 1 = Active, 2 = Postrun
        2321 : RawCodec(91, "ZigBeeApartmentOneDecoupleList"),
        2327 : O3EComplexType(4, "VentilationTargetVolumeFlow",[O3EInt16(2, "ActualFlow", scale=1.0), O3EInt16(2, "Unknown", scale=1.0)]),
        2328 : O3EComplexType(4, "VentilationCurrentVolumeFlow",[O3EInt16(2, "TargetFlow", scale=1.0), O3EInt16(2, "Unknown", scale=1.0)]),
        2329 : RawCodec(14, "BatteryEnergyUsedAverage"),
        2330 : O3EEnum(1, "GenericDigitalInputConfigurationOnBoardTwo", "DigitalInputConfigurations"),
        2331 : O3EEnum(1, "GenericDigitalInputConfigurationOnBoardThree", "DigitalInputConfigurations"),
        2332 : O3EEnum(1, "GenericDigitalInputConfigurationOnBoardFour", "DigitalInputConfigurations"),
        2333 : O3EComplexType(9, "EconomizerLiquidTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        2334 : O3EComplexType(9, "EvaporatorVaporTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        2336 : O3EComplexType(9, "ControllerBoardTemperatureSensor",[O3EInt16(2, "Sensor1", scale=10), O3EInt16(2, "Sensor2", scale=10), RawCodec(5, "Unknown")]),
        2337 : RawCodec(1, "UltraLowNitroOxideStatusActive"),
        2338 : RawCodec(3, "HighLimitTestMode"),
        2339 : RawCodec(2, "SafetyLimiterThresholdTemperature"),
        2340 : RawCodec(2, "ElectricalHeaterConfiguration"),
        2341 : RawCodec(4, "CoefficientOfPerformanceConfiguration"),
        2342 : O3EInt32(4, "NominalThermalCapacityHeating", scale = 1, signed=True),
        2343 : O3EInt32(4, "NominalThermalCapacityCooling", scale = 1, signed=True),
        2344 : RawCodec(1, "CombustionAirInterlockSettings"),
        2345 : O3EInt8(1, "CompressorSetpointPercent"),#+++
        2346 : O3EInt8(1, "CompressorSpeedPercent"),
        2348 : RawCodec(8, "PhotovoltaicsActivePowerLimitationEnergyManagementSystem"),
        2349 : RawCodec(8, "PhotovoltaicsActivePowerLimitationFallbackEnergyManagementSystem"),
        2350 : O3EByteVal(1, "EnergyManagmentSystemResultingControlState"),
        2351 : O3EComplexType(2, "HeatPumpCompressor", [O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState")]),
        2352 : O3EComplexType(2, "AdditionalElectricHeater", [O3EByteVal(1, "PowerState"), O3EByteVal(1, "ErrorState")]),
        2353 : O3EComplexType(4, "TargetDemandHeatProducer", [O3EByteVal(1, "StateHeating"), O3EInt16(2, "FlowTemperature", signed=True), O3EByteVal(1, "Modulation")]),
        2355 : O3EComplexType(4, "MinimumVentilationSupplyAirTemperature",[O3EInt16(2, "Sensor1", scale=10), O3EInt16(2, "Sensor2", scale=10)]),
        2356 : O3EInt8(1, "CurrentSystemHeatingCoolingLevel"),
        2369 : O3EComplexType(14, "HeatPumpCompressorStatistical",[RawCodec(6, "Unknown1"), O3EInt16(2, "starts", scale=1), RawCodec(2, "Unknown2"), O3EInt16(2, "hours", scale=1), RawCodec(2, "Unknown3")]),
        2370 : O3EComplexType(11, "AdditionalElectricHeaterStatistical",[RawCodec(3, "Unknown1"), O3EInt16(2, "starts", scale=1), RawCodec(2, "Unknown2"), O3EInt16(2, "hours", scale=1), RawCodec(2, "Unknown3")]),
        2371 : O3EComplexType(2, "VentilationControlMode",[O3EByteVal(1, "Mode"), RawCodec(1, "Unknown")]),
        2372 : O3EComplexType(2, "VentilationControllerOperationState",[RawCodec(1, "Unknown1"), RawCodec(1, "Unknown2")]),
        2373 : RawCodec(2, "VentilationAirVolumeFlowBalancingOffset"),
        2374 : O3EByteVal(1, "VentilationExternalLockFunctionSetting"),
        2375 : RawCodec(7, "NarrowBandInternetOfThingsConfiguration"),#+++
        2376 : RawCodec(132, "NarrowBandInternetOfThingsRadio"),#+++
        2377 : RawCodec(45, "EvolvedUniversalTerrestrialRadioAccessDataLinkInfo"),#+++
        2378 : RawCodec(48, "EvolvedUniversalTerrestrialRadioAccessNeighborCells"),#+++
        2379 : RawCodec(22, "EvolvedUniversalTerrestrialRadioAccessServingCellInfo"),#+++
        2380 : RawCodec(17, "EvolvedUniversalTerrestrialRadioAccessServingCellMeasurements"),#+++
        2382 : RawCodec(2, "PaddleSwitch"),
        2403 : O3EInt8(1, "BypassOperationLevel"),
        2404 : O3EComplexType(6, "BivalenceControlMode", [O3EByteVal(1, "OperationMode"), O3EInt16(2, "BivalenceControlTemperature", scale=10, signed=True), O3EInt16(2, "BivalenceControlAlternativeTemperature", scale=10, signed=True), O3EByteVal(1, "ControlMode")]),
        2405 : RawCodec(6, "MixerOneCircuitConstantFlowSetTemperatureCooling"),
        2406 : RawCodec(6, "MixerTwoCircuitConstantFlowSetTemperatureCooling"),
        2407 : RawCodec(6, "MixerThreeCircuitConstantFlowSetTemperatureCooling"),
        2408 : RawCodec(6, "MixerFourCircuitConstantFlowSetTemperatureCooling"),
        2409 : RawCodec(12, "MixerOneCircuitMinimumMaximumFlowSetTemperatureCooling"),
        2410 : RawCodec(12, "MixerTwoCircuitMinimumMaximumFlowSetTemperatureCooling"),
        2411 : RawCodec(12, "MixerThreeCircuitMinimumMaximumFlowSetTemperatureCooling"),
        2412 : RawCodec(12, "MixerFourCircuitMinimumMaximumFlowSetTemperatureCooling"),
        2413 : RawCodec(4, "MixerOneCircuitThresholdCooling"),
        2414 : RawCodec(4, "MixerTwoCircuitThresholdCooling"),
        2415 : RawCodec(4, "MixerThreeCircuitThresholdCooling"),
        2416 : RawCodec(4, "MixerFourCircuitThresholdCooling"),
        2417 : RawCodec(6, "MixerOneCircuitTargetValueRelativeHumidityCooling"),
        2418 : RawCodec(6, "MixerTwoCircuitTargetValueRelativeHumidityCooling"),
        2419 : RawCodec(6, "MixerThreeCircuitTargetValueRelativeHumidityCooling"),
        2420 : RawCodec(6, "MixerFourCircuitTargetValueRelativeHumidityCooling"),
        2421 : RawCodec(2, "MixerOneCircuitTemperatureOffsetCooling"),
        2422 : RawCodec(2, "MixerTwoCircuitTemperatureOffsetCooling"),
        2423 : RawCodec(2, "MixerThreeCircuitTemperatureOffsetCooling"),
        2424 : RawCodec(2, "MixerFourCircuitTemperatureOffsetCooling"),
        2426 : O3EComplexType(6, "MixerOneCircuitRoomEcoFunctionSettings",  [O3EBool(1,"State"), O3EInt16(2, "OutsideTemperatureLimit", scale=10.0, signed=True),O3EByteVal(1,"Unknown"), O3EInt16(2, "RoomTemperatureLimit", scale=10.0, signed=True)]),
        2427 : O3EComplexType(6, "MixerTwoCircuitRoomEcoFunctionSettings",  [O3EBool(1,"State"), O3EInt16(2, "OutsideTemperatureLimit", scale=10.0, signed=True),O3EByteVal(1,"Unknown"), O3EInt16(2, "RoomTemperatureLimit", scale=10.0, signed=True)]),
        2428 : O3EComplexType(6, "MixerThreeCircuitRoomEcoFunctionSettings",[O3EBool(1,"State"), O3EInt16(2, "OutsideTemperatureLimit", scale=10.0, signed=True),O3EByteVal(1,"Unknown"), O3EInt16(2, "RoomTemperatureLimit", scale=10.0, signed=True)]),
        2429 : O3EComplexType(6, "MixerFourCircuitRoomEcoFunctionSettings", [O3EBool(1,"State"), O3EInt16(2, "OutsideTemperatureLimit", scale=10.0, signed=True),O3EByteVal(1,"Unknown"), O3EInt16(2, "RoomTemperatureLimit", scale=10.0, signed=True)]),
        2442 : O3EInt8(1, "HeatPumpFrostProtection"),#+++
        2444 : O3EInt8(1, "LogLevelEmbbededApplication"),
        2445 : RawCodec(2, "SupplementalHeatEngineConfiguration"),
        2446 : RawCodec(4, "HmiWakeupTrigger"),
        2447 : O3EComplexType(4, "SupplyAirVolumeFlowDeviceLimit",[O3EInt16(2, "Minimum", scale=1.0), O3EInt16(2, "Maximum", scale=1.0)]),
        2448 : O3EComplexType(4, "ExhaustAirVolumeFlowDeviceLimit",[O3EInt16(2, "Minimum", scale=1.0), O3EInt16(2, "Maximum", scale=1.0)]),
        2449 : RawCodec(2, "CustomerSpecificDeviceName"),
        2450 : RawCodec(16, "CascadeSequenceCurrentBoiler"),
        2451 : RawCodec(3, "CascadeEmergencyOperationMode"),            
        2452 : RawCodec(4, "MixerOneCircuitRoomTemperatureThresholdCooling"),
        2453 : RawCodec(4, "MixerTwoCircuitRoomTemperatureThresholdCooling"),
        2454 : RawCodec(4, "MixerThreeCircuitRoomTemperatureThresholdCooling"),
        2455 : RawCodec(4, "MixerFourCircuitRoomTemperatureThresholdCooling"),
        2457 : O3EComplexType(9, "CalculatedOutsideTemperature", [O3EInt16(2, "DampedActual", signed=True), O3EInt16(2, "DampedMin", signed=True), O3EInt16(2, "DampedMax", signed=True), O3EInt16(2, "DampedAverage", signed=True), RawCodec(1, "Unknown")]),
        2458 : RawCodec(18, "CascadeDeviceStatusLead"),
        2459 : RawCodec(18, "CascadeDeviceStatusLagOne"),
        2460 : RawCodec(18, "CascadeDeviceStatusLagTwo"),
        2461 : RawCodec(18, "CascadeDeviceStatusLagThree"),
        2462 : RawCodec(18, "CascadeDeviceStatusLagFour"),
        2463 : RawCodec(18, "CascadeDeviceStatusLagFive"),
        2464 : RawCodec(18, "CascadeDeviceStatusLagSix"),
        2465 : RawCodec(18, "CascadeDeviceStatusLagSeven"),
        2466 : RawCodec(18, "CascadeDeviceStatusLagEight"),
        2467 : RawCodec(18, "CascadeDeviceStatusLagNine"),
        2468 : RawCodec(18, "CascadeDeviceStatusLagTen"),
        2469 : RawCodec(18, "CascadeDeviceStatusLagEleven"),
        2470 : RawCodec(18, "CascadeDeviceStatusLagTwelve"),
        2471 : RawCodec(18, "CascadeDeviceStatusLagThirteen"),
        2472 : RawCodec(18, "CascadeDeviceStatusLagFourteen"),
        2473 : RawCodec(18, "CascadeDeviceStatusLagFifteen"),
        2474 : RawCodec(9, "CascadeCommonFlowTemperatureSensor"),
        2475 : O3EInt16(2, "CascadeCommonFlowCurrentTemperatureSetpoint"),
        2476 : RawCodec(21, "EnvironmentAirQualityTargetValues"),
        2477 : O3EByteVal(1, "EnvironmentAirQualitySensor"),
        2479 : RawCodec(5, "MixerOneCircuitRoomAirHumiditySensor"),
        2480 : RawCodec(5, "MixerTwoCircuitRoomAirHumiditySensor"),
        2481 : RawCodec(5, "MixerThreeCircuitRoomAirHumiditySensor"),
        2482 : RawCodec(5, "MixerFourCircuitRoomAirHumiditySensor"),
        2484 : RawCodec(8, "ElectricalPowerRangeMetaData"),
        2486 : O3EInt32(4, "CurrentElectricalPowerConsumptionRefrigerantCircuit", scale = 1),
        2487 : O3EInt32(4, "CurrentElectricalPowerConsumptionElectricHeater", scale = 1),
        2488 : O3EInt32(4, "CurrentElectricalPowerConsumptionSystem", scale = 1),
        2489 : RawCodec(3, "FrostProtectionStatus"),
        2490 : RawCodec(1, "StartUpWizardState"),
        2491 : RawCodec(1, "DomesticHotWaterDemandInput"),
        2493 : RawCodec(2, "VentilationBypassPosition"),
        2494 : O3EInt32(4, "CurrentThermalCapacityRefrigerantCircuit", scale = 1),
        2495 : O3EInt32(4, "CurrentThermalCapacityElectricHeater", scale = 1),
        2496 : O3EInt32(4, "CurrentThermalCapacitySystem", scale = 1),
        2497 : RawCodec(3, "ResetStatisticalValuesDate"),
        2498 : O3EByteVal(1, "CentralHeatingPumpType"),
        2499 : O3EByteVal(1, "MixerOneCircuitPumpType"),
        2500 : O3EByteVal(1, "MixerTwoCircuitPumpType"),
        2501 : O3EByteVal(1, "MixerThreeCircuitPumpType"),
        2502 : O3EByteVal(1, "MixerFourCircuitPumpType"),
        2515 : O3EComplexType(124, "EnergyConsumptionDomesticHotWaterMonthMatrixElectricHeater", [
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")])]),
        2516 : O3EComplexType(96, "EnergyConsumptionDomesticHotWaterYearMatrixElectricHeater",  [
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        2517 : O3EComplexType(24, "EnergyConsumptionDomesticHotWaterElectricHeater", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        2524 : O3EComplexType(124, "EnergyConsumptionCentralHeatingMonthMatrixElectricHeater", [
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")])]),
        2525 : O3EComplexType(96, "EnergyConsumptionCentralHeatingYearMatrixElectricHeater",  [
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        2526 : O3EComplexType(24, "EnergyConsumptionCentralHeatingElectricHeater", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        2527 : O3EComplexType(124, "GeneratedCoolingOutputMonthMatrix",[
            O3EList(62, "CurrentMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
            O3EList(62, "LastMonth",[O3EInt16(2, "01"), O3EInt16(2, "02"), O3EInt16(2, "03"), O3EInt16(2, "04"), O3EInt16(2, "05"), O3EInt16(2, "06"), O3EInt16(2, "07"), O3EInt16(2, "08"), O3EInt16(2, "09"), O3EInt16(2, "10"), O3EInt16(2, "11"), O3EInt16(2, "12"), O3EInt16(2, "13"), O3EInt16(2, "14"), O3EInt16(2, "15"), O3EInt16(2, "16"), O3EInt16(2, "17"), O3EInt16(2, "18"), O3EInt16(2, "19"), O3EInt16(2, "20"), O3EInt16(2, "21"), O3EInt16(2, "22"), O3EInt16(2, "23"), O3EInt16(2, "24"), O3EInt16(2, "25"), O3EInt16(2, "26"), O3EInt16(2, "27"), O3EInt16(2, "28"), O3EInt16(2, "29"), O3EInt16(2, "30"), O3EInt16(2, "31")]),
        ]),
        2528 : O3EComplexType(96, "GeneratedCoolingOutputYearMatrix", [
            O3EList(48, "CurrentYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
            O3EList(48, "LastYear", [O3EInt32(4, "01_January", scale=10), O3EInt32(4, "02_February", scale=10), O3EInt32(4, "03_March", scale=10), O3EInt32(4, "04_April", scale=10), O3EInt32(4, "05_May", scale=10), O3EInt32(4, "06_June", scale=10),
                                                                      O3EInt32(4, "07_July", scale=10), O3EInt32(4, "08_August", scale=10), O3EInt32(4, "09_September", scale=10), O3EInt32(4, "10_October", scale=10), O3EInt32(4, "11_November", scale=10), O3EInt32(4, "12_December", scale=10)]),
        ]),
        2529 : O3EComplexType(24, "GeneratedCoolingOutput", [O3EInt32(4, "Today", scale=10), O3EInt32(4, "Past7Days", scale=10), O3EInt32(4, "CurrentMonth", scale=10), O3EInt32(4, "PastMonth", scale=10), O3EInt32(4, "CurrentYear", scale=10), O3EInt32(4, "PastYear", scale=10)]), 
        2533 : RawCodec(27, "PowerGridCodeSettingsNormSix"),
        #2534 : O3EList(181, "BusTopologyMatrixSix", [O3EInt8(1, "Count"), O3EComplexType(36, "TopologyElement",[O3EByteVal(1, "NodeID"), O3EEnum(1, "BusType", "BusTypes"), O3EByteVal(1, "DeviceProperty"), O3EByteVal(1, "DeviceFunction"), O3ESoftVers(8, "SW-Version"), O3ESoftVers(8, "HW-Version"), O3EUtf8(16, "VIN")])]),
        2534 : RawCodec(181, "BusTopologyMatrixSix"),#+++
        2535 : RawCodec(181, "BusTopologyMatrixSeven"),#+++
        2536 : RawCodec(181, "BusTopologyMatrixEight"),#+++
        2537 : RawCodec(181, "BusTopologyMatrixNine"),#+++
        2538 : RawCodec(181, "BusTopologyMatrixTen"),#+++
        2539 : RawCodec(40, "AlternatingCurrentEnergyStatistic"),
        2540 : RawCodec(6, "NoiseReductionSettings"),
        2541 : O3EComplexType(4, "SupplyAirVolumeFlowConfigurationLimit",[O3EInt16(2, "Minimum", scale=1.0), O3EInt16(2, "Maximum", scale=1.0)]),
        2542 : O3EComplexType(4, "ExhaustAirVolumeFlowConfigurationLimit",[O3EInt16(2, "Minimum", scale=1.0), O3EInt16(2, "Maximum", scale=1.0)]),
        2543 : O3EComplexType(10, "SmartGridTemperatureOffsets", [O3EInt16(2,"SetpointIncreaseRoomTemperatureHeating"), O3EInt16(2, "SetpointDecreaseRoomTemperatureCooling"), O3EInt16(2, "SetpointIncreaseDHWTemperature"), O3EInt16(2, "SetpointIncreaseBufferTemperatureHeating"), O3EInt16(2,"SetpointDecreaseBufferTemperatureCooling")]), #github #127 Unit K
        2544 : O3EByteVal(1, "EnableElectricalHeaterSmartGridLock"),
        2545 : O3EByteVal(1, "EnableElectricalHeaterSmartGridIncreaseMaxDemand"),
        2546 : O3EComplexType(9, "MixerOneCircuitRoomTemperatureSetpointCooling", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Normal", signed=True), O3EInt16(2, "Reduced", signed=True), O3EInt16(2, "Unknown", signed=True), O3EEnum(1, "State", "OpStates")]),
        2547 : O3EComplexType(9, "MixerTwoCircuitRoomTemperatureSetpointCooling", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Normal", signed=True), O3EInt16(2, "Reduced", signed=True), O3EInt16(2, "Unknown", signed=True), O3EEnum(1, "State", "OpStates")]),
        2548 : O3EComplexType(9, "MixerThreeCircuitRoomTemperatureSetpointCooling", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Normal", signed=True), O3EInt16(2, "Reduced", signed=True), O3EInt16(2, "Unknown", signed=True), O3EEnum(1, "State", "OpStates")]),
        2549 : O3EComplexType(9, "MixerFourCircuitRoomTemperatureSetpointCooling", [O3EInt16(2, "Comfort", signed=True), O3EInt16(2, "Normal", signed=True), O3EInt16(2, "Reduced", signed=True), O3EInt16(2, "Unknown", signed=True), O3EEnum(1, "State", "OpStates")]),
        2551 : RawCodec(6, "FlameBurnerTwo"),
        2552 : RawCodec(2, "ModulationCurrentValueBurnerTwo"),
        2553 : RawCodec(12, "HeatEngineStatisticalBurnerTwo"),
        2554 : RawCodec(62, "CellularModemIdentification"),#+++
        2555 : RawCodec(4, "ElectricalPowerSetPoint"),
        2556 : RawCodec(4, "ElectricalEnergyRemainingCapacity"),
        2557 : O3EByteVal(1, "HeatPumpState"),
        2558 : RawCodec(3, "HeatPumpSupportedStates"),
        2559 : RawCodec(2, "VentilationFanModbusId"),
        2560 : O3EByteVal(1, "SmartGridFeatureSelection"),
        2563 : RawCodec(91, "ZigBeeDeviceDecoupleList"),#+++
        2564 : RawCodec(1, "HydraulicFlapState"),
        2566 : O3EInt32(4, "VentilationSupplyFanRuntime", scale=1.0),
        2567 : O3EInt32(4, "VentilationExhaustFanRuntime", scale=1.0),
        2568 : O3EInt8(1, "RefrigerantType"),#+++
        2569 : O3EInt16(2, "CompressorSpeedRps", scale = 10),
        2570 : O3EInt16(2, "CompressorModulType"),#+++
        2571 : O3EInt16(2, "CompressorSuctionSuperheat"),#+++
        2572 : RawCodec(4, "ActualCompressorInletMassflow"),
        2573 : RawCodec(2, "CompressorOnTimer"),
        2574 : O3EInt16(8, "NominalPowerElectricalHeater", scale = 1),
        2575 : O3EInt16(2, "RefrigerationCycleApplicationState"),#+++
        2576 : RawCodec(2, "FuelCellTestModeOne"),
        2577 : RawCodec(6, "FuelCellTestModeTwo"),
        2578 : O3EInt8(1, "RefrigerationCircuitDesiredOperatingMode"),#+++
        2579 : RawCodec(4, "CompressorMinMaxAllowedPrimaryTemperatureHeating"),#+++
        2580 : O3EInt8(2, "CompressorSetpointRps", signed=True), #250xH Unit RpS
        2581 : O3EInt16(2, "CompressorCalculatedSetpointRps"),#+++
        2582 : RawCodec(2, "CompressorOffTimer"),
        2583 : RawCodec(15, "OxygenProbeProcessValuesBurnerOne"),
        2584 : RawCodec(15, "OxygenProbeProcessValuesBurnerTwo"),
        2586 : RawCodec(2, "DigitalOutputCooling"),
        2590 : RawCodec(8, "HeatPumpCommonSettingsHeating"),#+++
        2591 : RawCodec(8, "HeatPumpCommonSettingsCooling"),#+++
        2592 : RawCodec(4, "ExpansionValveTheoreticalSetpoint"),#+++
        2593 : RawCodec(181, "ProductMatrix"),
        2594 : RawCodec(124, "ElectricalPreHeaterMonthMatrix"),
        2595 : RawCodec(96, "ElectricalPreHeaterYearMatrix"),
        2598 : O3EByteVal(1, "VentilationFanAssignmentAvailable"),
        2599 : O3EByteVal(1, "VentilationFanAssignmentSwitch"),
        2600 : RawCodec(2, "ElectricalHeaterActivation"),
        2601 : RawCodec(2, "ElectricalHeaterVentilationConfiguration"),
        2602 : RawCodec(10, "PrimaryHeatExchangerStatus"),#+++
        2603 : RawCodec(4, "PrimaryHeatExchangerCommonSettings"),#+++
        2604 : O3EByteVal(1, "LevelSwitchActivation"),
        2605 : O3EComplexType(4, "QuickModeRuntime",[O3EInt16(2, "NoiseReduced", scale=1.0), O3EInt16(2, "Intensive", scale=1.0)]),
        2606 : O3EByteVal(1, "ExternalTriggerActivation"),
        2607 : O3EByteVal(1, "ExternalTriggerSettings"),
        2608 : RawCodec(28, "FilterSettings"),
        2609 : RawCodec(6, "CommissioningStatus"),
        2610 : RawCodec(1, "SetDeliveryStateExpert"),
        2611 : RawCodec(4, "NominalThermalCapacityIndoorUnit"),
        2612 : O3EComplexType(7, "PrimarySourceCommonSettingsHeating", [O3EByteVal(1, "Mode"), O3EInt16(2, "MaxFanSpeed"), O3EInt16(2, "DefaultFanSpeed"), O3EInt16(2, "MinFanSpeed")]),# ODU-FanSpeed --> Mode: Fixed/Variable, Unit: %
        2613 : O3EComplexType(7, "PrimarySourceCommonSettingsCooling", [O3EByteVal(1, "Mode"), O3EInt16(2, "MaxFanSpeed"), O3EInt16(2, "DefaultFanSpeed"), O3EInt16(2, "MinFanSpeed")]),# ODU-FanSpeed --> Mode: Fixed/Variable, Unit: %
        2621 : O3EInt16(2, "MaximumOperatingPressureActualTemperatureSetpoint"),#+++
        2622 : O3EInt16(9, "SeasonalCoefficientOfPerformaceHeating"),
        2623 : O3EInt16(9, "SeasonalEnergyEfficiencyRatioCooling"),
        2624 : O3EInt16(9, "SeasonalCoefficientOfPerformaceDomesticHotWater"),
        2625 : O3EInt16(9, "SeasonalCoefficientOfPerformaceHeatingAndDomesticHotWater"),
        2626 : O3EInt32(4, "MaximumPowerElectricalHeater", scale = 1),
        2627 : O3EInt16(2, "CompressorStartUpTimer"),#+++
        2629 : O3EInt32(4, "DesiredThermalCapacity", scale = 1),
#        2630 : RawCodec(4, "CompressorMinMaxSpeedHeating"),#+++
        2630 : O3EComplexType(4, "CompressorMinMaxSpeedHeating", [O3EInt16(2, "Min", scale =10, signed = "True"), O3EInt16(2, "Max", scale =10, signed = "True")]), #250SH Unit RpS
#        2631 : RawCodec(4, "CompressorMinMaxSpeedCooling"),#+++
        2631 : O3EComplexType(4, "CompressorMinMaxSpeedCooling", [O3EInt16(2, "Min", scale =10, signed = "True"), O3EInt16(2, "Max", scale =10, signed = "True")]), #250SH Unit RpS
#        2632 : RawCodec(4, "CompressorMinMaxSpeedDefrost"),#+++
        2632 : O3EComplexType(4, "CompressorMinMaxSpeedDefrost", [O3EInt16(2, "Min", scale =10, signed = "True"), O3EInt16(2, "Max")]), #250SH Unit RpS
        2633 : RawCodec(12, "MaxSpeedNoiseReductionMode"),#+++
        2634 : O3EByteVal(1, "NoiseReductionMode"),
        2635 : RawCodec(8, "BurnerProcessDataFlags"),
        2636 : RawCodec(8, "BurnerTwoProcessDataFlags"),
        2637 : RawCodec(8, "BurnerThreeProcessDataFlags"),
        2638 : RawCodec(4, "SupportedCountryCodes"),
        2643 : RawCodec(2, "MaximumRechargePower"),
        2733 : RawCodec(3, "InstallationConfirmation"),
        2735 : O3EByteVal(1, "FourThreeWayValveValveCurrentPosition"),# 0 = Central Heating / Cooling, 1 = Internal Buffer, 2 = Domestic Hot Water, 3 = Central Heating / Cooling + Internal Buffer, 4 = Domestic Hot Water + Internal Buffer
        2741 : RawCodec(3, "ComfortEnsuringMode"),
        2742 : O3EInt8(1, "DiagnosticHydraulicFilterInterval"),
        2743 : O3EInt8(1, "DiagnosticElectricalHeaterSafetyTemperatureLimiter"),
        2744 : O3EInt8(1, "DiagnosticSecondaryFourThreeWayValve"),
        2745 : O3EInt8(1, "DiagnosticHydraulicFilterContamination"),
        2746 : O3EInt8(1, "DiagnosticHydraulicSafetyValve"),
        2748 : O3EInt8(1, "DiagnosticControlledLowPressureShutDown"),#+++
        2749 : O3EInt8(1, "DiagnosticControlledHighPressureShutDown"),#+++
        2750 : O3EInt8(1, "DiagnosticHydraulicTemperatureSensors"),
        2751 : O3EInt8(1, "DiagnosticElectronicExpansionValve"),#+++
        2752 : O3EInt8(1, "DiagnosticFanOperation"),#+++
        2753 : O3EInt8(1, "DiagnosticHeatExchangerConstraints"),#+++
        2758 : RawCodec(1, "GasPressureSwitchErrorReaction"),
        2759 : RawCodec(24, "EnergyRecoveredCrossHeatExchanger"),
        2760 : RawCodec(24, "EnergyOwnConsumption"),
        2767 : O3EInt8(1, "DiagnosticMonitoringPressureDrop"),
        2768 : O3EInt8(1, "DiagnosticMonitoringPressurePeaks"),
        2772 : RawCodec(124, "EnergyRecoveredCrossHeatExchangerMonthMatrix"),
        2773 : RawCodec(96, "EnergyRecoveredCrossHeatExchangerYearMatrix"),
        2774 : RawCodec(124, "EnergyOwnConsumptionMonthMatrix"),
        2775 : RawCodec(96, "EnergyOwnConsumptionYearMatrix"),
        2776 : RawCodec(181, "ProductMatrixTwo"),
        2777 : RawCodec(8, "PrimaryBootLoaderVersion"),
        2778 : RawCodec(2, "ErrorMessageInputSelection"),
        2779 : RawCodec(2, "DeltaTemperaturePumpControlSetpoint"),
        2780 : RawCodec(1, "DomesticHotWaterFlowRangeDwellDuration"), 
        2781 : RawCodec(7, "AirVolumeFlowSetpoint"),
        2782 : RawCodec(24, "AirVolumeFlowStatus"),
        2783 : RawCodec(4, "VentilationSelfCheckDuration"),
        2784 : O3EInt16(9, "SecondaryHeatExchangerVaporPressureSensor", scale = 100),
        2785 : RawCodec(16, "ElectricalHeaterStarts"),
        2786 : RawCodec(2, "ElectricalPreheaterCurrentPowerConsumption"),
        2791 : O3EInt8(5, "CentralHeatingPumpStatus"),
        2792 : O3EInt8(5, "MixerOneCircuitPumpStatus"),
        2793 : O3EInt8(5, "MixerTwoCircuitPumpStatus"),
        2794 : O3EInt8(5, "MixerThreeCircuitPumpStatus"),
        2795 : O3EInt8(5, "MixerFourCircuitPumpStatus"),
        2796 : RawCodec(2, "ExternalHeaterConfiguration"),
        2797 : O3EByteVal(1, "VentilationBypassFlapAvailableCount"),
        2798 : O3EByteVal(1, "RelativeHumiditySensorSelection"),
        2799 : O3EByteVal(1, "ElectricalHeatersShutdownDelay"),
        2800 : O3EByteVal(1, "VentilationHeatExchangerType"),
        2801 : O3EByteVal(1, "VentilationFanAssignmentSwitchManufacturing"),
        2802 : RawCodec(6, "InverterSelfTestStatus"),
        2804 : RawCodec(151, "InverterSelfTestResultTwo"),
        2805 : RawCodec(151, "InverterSelfTestResultThree"),
        2806 : O3EComplexType(2, "RefrigerationCircuitOperationMode",[O3EByteVal(1,"Mode"),O3EByteVal(1,"State")]),
        2807 : RawCodec(9, "InverterHousingTemperature"),#+++
        2808 : RawCodec(9, "InverterInternalPowerModuleTemperature"),#+++
        2809 : RawCodec(1, "PumpMinSpeedConfiguration"),
        2810 : RawCodec(1, "CentralHeatingPumpFeedbackSignalHandlingMode"),
        2826 : RawCodec(40, "FuelCellNetworkSystemProtectionErrorHistory"),
        2827 : RawCodec(48, "FuelCellNetworkSystemProtectionParameters"),
        2828 : RawCodec(2, "FuelCellSdCardRecording"),
        2829 : RawCodec(20, "ProductIdentification"),
        2830 : RawCodec(1, "EmergencyMode"),
        2831 : O3EInt16(2, "BivalenceControlAlternativeTemperature", scale=10, signed=True),
        2832 : RawCodec(4, "BaseHeaterTimer"),#+++
        2833 : O3EInt8(1, "BaseHeaterTimerMode"),#+++
        2834 : O3EInt16(2, "BaseHeaterTimerDuration"),#+++
        2835 : O3EInt16(2, "BaseHeaterTemperatureThreshold"),#+++
        2836 : O3EInt16(2, "SecondaryHeatExchangerMinimumVolumeFlowThreshold"),#+++
        2837 : O3EInt16(2, "SecondaryHeatExchangerOptimumTemperatureSpreadExponent"),#+++
        2838 : RawCodec(4, "SecondaryHeatExchangerOptimumTemperatureSpreadHeating"),#+++
        2839 : RawCodec(4, "SecondaryHeatExchangerOptimumTemperatureSpreadCooling"),#+++
        2840 : O3EInt16(2, "SecondaryHeatExchangerOptimumVolumeFlowDefrost"),#+++
        2842 : O3EInt16(2, "SecondaryHeatExchangerHxSubcooling"),#+++
        2843 : O3EInt16(2, "SecondaryHeatExchangerMinimumVolumeFlow"),#+++
        2844 : O3EInt16(2, "SecondaryHeatExchangerMinimumOutletTemperature"),#+++
        2845 : O3EInt16(2, "SecondaryHeatExchangerMaximumOutletTemperature"),#+++
        2847 : RawCodec(8, "CrankCaseHeaterStatistics"),#+++
        2848 : O3EInt16(2, "CrankCaseHeaterTemperatureStatistics"),#+++
        2849 : RawCodec(27, "CrankCaseHeaterOnTimer"),
        2850 : RawCodec(3, "CrankCaseHeaterSensorErrorType"),#+++
        2851 : O3EInt16(2, "PreStartDuration"),#+++
        2852 : O3EInt8(1, "FanDuctHeater"),#+++
        2853 : O3EInt16(2, "ExternalHeaterTimeIntegralThershold", scale=10, signed=False),
        2855 : O3EComplexType(3, "MixerOneCircuitFrostProtectionConfiguration", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        2856 : O3EComplexType(3, "MixerTwoCircuitFrostProtectionConfiguration", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        2857 : O3EComplexType(3, "MixerThreeCircuitFrostProtectionConfiguration", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        2858 : O3EComplexType(3, "MixerFourCircuitFrostProtectionConfiguration", [O3EByteVal(1, "State"), O3EInt16(2, "Temperature", signed=True)]),
        2874 : O3EInt16(2, "PrimarySourceRpsOne"),#+++
        2875 : O3EInt16(2, "PrimarySourceRpsTwo"),#+++
        2876 : O3EInt16(2, "PrimaryPumpCommonSetpoint"),#+++
        2877 : O3EInt16(2, "SuctionSuperheatSetpoint"),#+++
        2878 : O3EInt16(2, "SubcoolingSetpoint"),#+++
        2879 : RawCodec(2, "MixerOneCircuitHeatingBlocked"),
        2880 : RawCodec(2, "MixerTwoCircuitHeatingBlocked"),
        2881 : RawCodec(4, "ExpansionValveOneTimer"),#+++
        2882 : RawCodec(4, "ExpansionValveTwoTimer"),#+++
        2883 : O3EInt16(2, "ExpansionValveMaximumOperatingPressureTemperatureSetpoint"),#+++
        2884 : O3EInt16(2, "ExpansionValveOneStatus"),#+++
        2885 : O3EInt16(2, "ExpansionValveTwoStatus"),#+++
        2886 : O3EInt16(2, "RefrigerantCyclePostStopDuration"),#+++
        2887 : O3EInt16(2, "RefrigerantCycleAlarmPauseDuration"),#+++
        2888 : O3EInt16(2, "RefrigerantCyclePumpdownStoppingDelay"),#+++
        2889 : RawCodec(6, "RefrigerantCycleTimers"),#+++
        2890 : O3EInt16(2, "RefrigerantCyclePumpdownHoldTimer"),#+++
        2891 : RawCodec(6, "RefrigerantCycleDefrostTimers"),#+++
        2892 : O3EInt16(2, "RefrigerantCycleTransitionToHeatingTimer"),#+++
        2893 : O3EInt16(2, "RefrigerantCycleTransitionToCoolingTimer"),#+++
        2894 : O3EByteVal(1, "RefrigerantCycleAvailability"),
        2895 : RawCodec(5, "PrimaryPumpSettings"),#+++
        2896 : O3EInt8(1, "PrimaryPumpOneStatus"),#+++
        2897 : O3EInt8(1, "PrimaryPumpTwoStatus"),#+++
        2908 : O3EInt8(1, "InverterModuleType"),#+++
        2909 : RawCodec(4, "CompressorMinMaxRequestedSecondaryReturnTemperatureCooling"),#+++
        2910 : RawCodec(4, "CompressorMinMaxRequestedSecondaryReturnTemperaturePreStartDefrost"),#+++
        2911 : O3EInt16(2, "CompressorMaximumRequestedSecondaryReturnTempDefrost"),#+++
        2912 : O3EInt16(2, "CompressorMaximumDischargeTemperature"),#+++
        2913 : O3EInt16(2, "CompressorMinimumAllowedSecondaryOutletTemperatureHeating"),#+++
        2914 : RawCodec(4, "CompressorMinMaxAllowedPrimaryTemperatureCooling"),#+++
        2915 : O3EInt16(2, "CompressorMaximumCondensingPressure"),#+++
        2916 : O3EInt16(2, "CompressorMaximumEvaporatingPressure"),#+++
        2917 : O3EInt16(2, "CompressorMinimumEvaporatingPressureHeating"),#+++
        2918 : O3EInt16(2, "CompressorMinimumEvaporatingPressureCooling"),#+++
        2920 : RawCodec(2, "ExternalHeaterSpecification"),
        2921 : RawCodec(2, "DiagnosticHydraulicFilterIntervalSettings"),
        2922 : RawCodec(2, "DiagnosticHydraulicFilterIntervalTemporalSettings"),
        2923 : RawCodec(6, "DiagnosticSecondaryFourThreeWayValveSettings"),
        2924 : RawCodec(4, "DiagnosticHydraulicFilterContaminationSettings"),
        2925 : RawCodec(2, "DiagnosticMonitoringPressurePeaksSettings"),
        2926 : RawCodec(6, "DiagnosticMonitoringPressureDropSettings"),
        2927 : O3EInt8(1, "DiagnosticElectronicExpansionValveSettings"),#+++
        2928 : O3EInt16(2, "DiagnosticHeatExchangerConstraintsSettings"),#+++
        2929 : O3EInt8(1, "DiagnosticRefrigerantCircuitPressureSensors"),#+++
        2930 : O3EInt8(1, "DiagnosticRefrigerantCircuitFourTwoWayValve"),#+++
        2931 : O3EInt8(1, "DiagnosticRefrigerantCircuitTemperatureSensors"),#+++
        2932 : RawCodec(4, "TimeCounterSinceLastReset"),
        2936 : RawCodec(3, "ElectricalEnergyStorageSystemState"),
        2937 : RawCodec(2, "SystemPumpConfiguration"),
        2938 : RawCodec(4, "CascadeSystemPump"),
        2939 : O3EInt16(2, "PrimaryHeatExchangerLowEvaporatingTemperatureAlarmDelay"),#+++
#        2940 : RawCodec(3, "ExternalHeaterDelayTimer"), # ref https://github.com/open3e/open3e/discussions/110#discussioncomment-9880590
        2940 : O3EComplexType(3, "ExternalHeaterDelayTimer",[O3EInt8(1, "SwitchOnDelay", scale=1.0), O3EInt8(1, "MinRunTime", scale=1.0), O3EInt8(1, "SwitchOffDelay", scale=1.0)]),        
        2942 : RawCodec(137, "ListOfLayerSettingServiceDevices"),
        2944 : O3EByteVal(1, "NodeIdOnExternalCan"),
        2945 : RawCodec(1, "PointOfCommonCouplingEnergyMeterConnectedPhases"),
        2946 : RawCodec(24, "EnergyConsumptionElectricalPreHeater"),
        2947 : RawCodec(5, "SleepModePrevention"),
        2952 : RawCodec(137, "ListOfLayerSettingServiceDevicesTwo"),
        2953 : RawCodec(10, "CascadeSystemConfigurationArray"),
        2956 : O3EInt8(1, "DeviceDigitalInputEightValue"),#+++
        2957 : O3EInt8(1, "DeviceDigitalInputNineValue"),#+++
        2969 : O3EByteVal(1, "ElectronicControlUnitSafeStateStatus"),
        2985 : O3EInt16(2, "ExternalHeaterTemperatureSetpoint", signed=True),
        2986 : O3EByteVal(1, "ExternalHeaterOperationState"),
        2987 : O3EInt8(1, "RefrigerantCycleUnlock"),#+++
        2999 : RawCodec(16, "ElectricalHeatersOperationHours"),
        3000 : RawCodec(115, "EcuResetInformationList"),
        3001 : RawCodec(196, "LowEvaporatingLowCondensingDriveDuration"),#+++
        3002 : RawCodec(196, "MidEvaporatingLowCondensingDriveDuration"),#+++
        3003 : RawCodec(196, "HighEvaporatingLowCondensingDriveDuration"),#+++
        3004 : RawCodec(196, "LowEvaporatingHighCondensingDriveDuration"),#+++
        3005 : RawCodec(196, "MidEvaporatingHighCondensingDriveDuration"),#+++
        3006 : RawCodec(196, "HighEvaporatingHighCondensingDriveDuration"),#+++
        3008 : O3EInt16(2, "FanDuctHeaterOnDuration"),#+++
        3009 : RawCodec(4, "FanDuctHeaterOnTimer"),#+++
        3013 : RawCodec(2, "MixerHybridThreeWayValvePositionPercent"),
        3014 : O3EComplexType(9, "OutdoorMiddleCoilTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3015 : O3EComplexType(9, "HeatSinkTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3016 : O3EComplexType(9, "HeatingBufferTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3017 : O3EComplexType(9, "CoolingBufferTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3018 : O3EComplexType(9, "HeatingCoolingBufferTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3019 : O3EComplexType(9, "CompressorOutletTargetTemperature", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]), # 250xH Unit °C
        3029 : O3EByteVal(1, "DomesticHotWaterEfficiencyMode"),# 0 = Eco, 1 = N/A, 2 = Comfort
        3030 : RawCodec(2, "DomesticHotWaterEfficiencyModeAvailability"),
        3031 : RawCodec(2, "ExternalHeater"),
        3032 : RawCodec(2, "PrimaryEnergyFactorElectricity"),
        3034 : O3EComplexType(9, "DomesticHotWaterReturnTemperaturTankLoadSystem", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3035 : O3EComplexType(9, "DomesticHotWaterFlowTemperaturTankLoadSystem", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]),
        3036 : RawCodec(2, "PrimaryEnergyFactorExternalHeater"),
        3037 : RawCodec(57, "ElectricityPriceTimeScheduleMonday"),
        3038 : RawCodec(57, "ElectricityPriceTimeScheduleTuesday"),
        3039 : RawCodec(57, "ElectricityPriceTimeScheduleWednesday"),
        3040 : RawCodec(57, "ElectricityPriceTimeScheduleThursday"),
        3041 : RawCodec(57, "ElectricityPriceTimeScheduleFriday"),
        3042 : RawCodec(57, "ElectricityPriceTimeScheduleSaturday"),
        3043 : RawCodec(57, "ElectricityPriceTimeScheduleSunday"),
        3056 : O3EInt8(1, "NarrowBandInternetOfThingsNetworkStatus"),#+++
        3057 : O3EInt8(1, "NarrowBandInternetOfThingsCloudStatus"),#+++
        3066 : RawCodec(4, "DomesticHotWaterHighDemandDetection"),
        3067 : RawCodec(9, "AirVolumeFlowValue"),#+++
        3068 : RawCodec(2, "DomesticHotWaterTemperatureSetpointComfort"),
        3069 : O3EByteVal(1, "DomesticHotWaterSensorForDemand"),
        3070 : O3EByteVal(1, "BufferTargetOperationMode"),
        3085 : RawCodec(18, "ElectricalEnergyStorageModuleOneInformation"),
        3086 : RawCodec(18, "ElectricalEnergyStorageModuleTwoInformation"),
        3087 : RawCodec(18, "ElectricalEnergyStorageModuleThreeInformation"),
        3088 : RawCodec(18, "ElectricalEnergyStorageModuleFourInformation"),
        3089 : RawCodec(18, "ElectricalEnergyStorageModuleFiveInformation"),
        3090 : RawCodec(18, "ElectricalEnergyStorageModuleSixInformation"),
        3091 : O3EByteVal(1, "GatewayEthernetTwoEnable"),
        3092 : RawCodec(21, "GatewayEthernetTwoConfig"),
        3093 : RawCodec(20, "GatewayEthernetTwoIp"),
        3094 : O3EByteVal(1, "GatewayEthernetTwoNetworkStatus"),
        3095 : RawCodec(6, "MacAddressLanTwo"),
        3096 : O3EByteVal(1, "GatewayWifiStationEnable"),
        3097 : O3EByteVal(1, "GatewayInternetAccess"),
#        3098 : RawCodec(2, "ExternalHeaterTemperatureOffset"),
        3098 : O3EInt8(2, "ExternalHeaterTemperatureOffset", scale=10), #250-xH Unit: K
        3103 : RawCodec(6, "IsCountryModeLoadInformation"),
#        3106 : RawCodec(4, "BufferMinimumMaximumSetTemperature"), # ref https://github.com/open3e/open3e/discussions/110#discussioncomment-9880590
        3106 : O3EComplexType(4, "BufferMinimumMaximumSetTemperature",[O3EInt16(2, "BufferMin", scale=10.0, signed=True), O3EInt16(2, "BufferMax", scale=10.0, signed=True)]),        
        3107 : RawCodec(7, "BatteryModuleExchangeAssistent"),
        3108 : RawCodec(9, "PhotovoltaicsActivePowerLimitationRampRate"),
        3109 : RawCodec(8, "PrimaryHeatExchangerBaseHeaterStatistical"),#+++
        3113 : RawCodec(8, "DeviceDigitalOutputOneValueStatistical"),
        3114 : RawCodec(8, "DeviceDigitalOutputTwoValueStatistical"),
        3115 : RawCodec(8, "DeviceDigitalOutputThreeValueStatistical"),#+++
        3116 : RawCodec(8, "DeviceDigitalOutputFourValueStatistical"),#+++
        3117 : RawCodec(8, "DeviceDigitalOutputFiveValueStatistical"),#+++
        3119 : RawCodec(8, "RefrigerantCircuitFourWayValveStatistical"),#+++
        3120 : RawCodec(8, "CompressorCrankCaseHeaterStatistical"),#+++
        3129 : RawCodec(8, "FanDuctHeaterStatistical"),#+++
        3134 : RawCodec(8, "DomesticHotWaterCirculationPumpStatistical"), 
        3146 : RawCodec(8, "ElectricalHeaterPhaseOneStatistical"),#+++
        3147 : RawCodec(8, "ElectricalHeaterPhaseTwoStatistical"),#+++
        3148 : RawCodec(8, "ElectricalHeaterPhaseThreeStatistical"),#+++
        3155 : RawCodec(5, "DomesticHotWaterShiftLoadPumpStatus"),
        3156 : O3EByteVal(1, "DomesticHotWaterShiftLoadPumpType"),
        3190 : O3EByteVal(1, "RefrigerantCircuitFourWayValvePosition"),
        3191 : RawCodec(199, "ExtendedEventLoggingHistory"),
        3212 : O3EInt8(2, "BivalentMixerDomesticHotWaterTemperatureOffset", scale=10), #250-xH Unit: K
        3213 : O3EComplexType(9, "ExternalHeaterTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]), # Unit °C
        3215 : O3EComplexType(9, "ExternalHeaterSeparatorTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]), # Unit °C
        3234 : O3EComplexType(9, "DomesticHotWaterBufferTopTemperatureSensor", [O3EInt16(2, "Actual", signed=True), O3EInt16(2, "Minimum", signed=True), O3EInt16(2, "Maximum", signed=True), O3EInt16(2, "Average", signed=True), O3EByteVal(1, "Unknown")]), # Unit °C    
    }
}
