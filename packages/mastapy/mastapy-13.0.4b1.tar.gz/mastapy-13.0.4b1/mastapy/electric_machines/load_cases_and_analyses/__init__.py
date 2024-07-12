"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1364 import BasicDynamicForceLoadCase
    from ._1365 import DynamicForceAnalysis
    from ._1366 import DynamicForceLoadCase
    from ._1367 import DynamicForcesOperatingPoint
    from ._1368 import EfficiencyMapAnalysis
    from ._1369 import EfficiencyMapLoadCase
    from ._1370 import ElectricMachineAnalysis
    from ._1371 import ElectricMachineBasicMechanicalLossSettings
    from ._1372 import ElectricMachineControlStrategy
    from ._1373 import ElectricMachineEfficiencyMapSettings
    from ._1374 import ElectricMachineFEAnalysis
    from ._1375 import ElectricMachineFEMechanicalAnalysis
    from ._1376 import ElectricMachineLoadCase
    from ._1377 import ElectricMachineLoadCaseBase
    from ._1378 import ElectricMachineLoadCaseGroup
    from ._1379 import ElectricMachineMechanicalLoadCase
    from ._1380 import EndWindingInductanceMethod
    from ._1381 import LeadingOrLagging
    from ._1382 import LoadCaseType
    from ._1383 import LoadCaseTypeSelector
    from ._1384 import MotoringOrGenerating
    from ._1385 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1386 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1387 import OperatingPointsSpecificationMethod
    from ._1388 import SingleOperatingPointAnalysis
    from ._1389 import SlotDetailForAnalysis
    from ._1390 import SpecifyTorqueOrCurrent
    from ._1391 import SpeedPointsDistribution
    from ._1392 import SpeedTorqueCurveAnalysis
    from ._1393 import SpeedTorqueCurveLoadCase
    from ._1394 import SpeedTorqueLoadCase
    from ._1395 import Temperatures
else:
    import_structure = {
        "_1364": ["BasicDynamicForceLoadCase"],
        "_1365": ["DynamicForceAnalysis"],
        "_1366": ["DynamicForceLoadCase"],
        "_1367": ["DynamicForcesOperatingPoint"],
        "_1368": ["EfficiencyMapAnalysis"],
        "_1369": ["EfficiencyMapLoadCase"],
        "_1370": ["ElectricMachineAnalysis"],
        "_1371": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1372": ["ElectricMachineControlStrategy"],
        "_1373": ["ElectricMachineEfficiencyMapSettings"],
        "_1374": ["ElectricMachineFEAnalysis"],
        "_1375": ["ElectricMachineFEMechanicalAnalysis"],
        "_1376": ["ElectricMachineLoadCase"],
        "_1377": ["ElectricMachineLoadCaseBase"],
        "_1378": ["ElectricMachineLoadCaseGroup"],
        "_1379": ["ElectricMachineMechanicalLoadCase"],
        "_1380": ["EndWindingInductanceMethod"],
        "_1381": ["LeadingOrLagging"],
        "_1382": ["LoadCaseType"],
        "_1383": ["LoadCaseTypeSelector"],
        "_1384": ["MotoringOrGenerating"],
        "_1385": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1386": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1387": ["OperatingPointsSpecificationMethod"],
        "_1388": ["SingleOperatingPointAnalysis"],
        "_1389": ["SlotDetailForAnalysis"],
        "_1390": ["SpecifyTorqueOrCurrent"],
        "_1391": ["SpeedPointsDistribution"],
        "_1392": ["SpeedTorqueCurveAnalysis"],
        "_1393": ["SpeedTorqueCurveLoadCase"],
        "_1394": ["SpeedTorqueLoadCase"],
        "_1395": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
