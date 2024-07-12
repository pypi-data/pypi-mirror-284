"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1339 import DynamicForceResults
    from ._1340 import EfficiencyResults
    from ._1341 import ElectricMachineDQModel
    from ._1342 import ElectricMachineMechanicalResults
    from ._1343 import ElectricMachineMechanicalResultsViewable
    from ._1344 import ElectricMachineResults
    from ._1345 import ElectricMachineResultsForConductorTurn
    from ._1346 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1347 import ElectricMachineResultsForLineToLine
    from ._1348 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1349 import ElectricMachineResultsForPhase
    from ._1350 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1351 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1352 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1353 import ElectricMachineResultsTimeStep
    from ._1354 import ElectricMachineResultsTimeStepAtLocation
    from ._1355 import ElectricMachineResultsViewable
    from ._1356 import ElectricMachineForceViewOptions
    from ._1358 import LinearDQModel
    from ._1359 import MaximumTorqueResultsPoints
    from ._1360 import NonLinearDQModel
    from ._1361 import NonLinearDQModelGeneratorSettings
    from ._1362 import OnLoadElectricMachineResults
    from ._1363 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1339": ["DynamicForceResults"],
        "_1340": ["EfficiencyResults"],
        "_1341": ["ElectricMachineDQModel"],
        "_1342": ["ElectricMachineMechanicalResults"],
        "_1343": ["ElectricMachineMechanicalResultsViewable"],
        "_1344": ["ElectricMachineResults"],
        "_1345": ["ElectricMachineResultsForConductorTurn"],
        "_1346": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1347": ["ElectricMachineResultsForLineToLine"],
        "_1348": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1349": ["ElectricMachineResultsForPhase"],
        "_1350": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1351": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1352": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1353": ["ElectricMachineResultsTimeStep"],
        "_1354": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1355": ["ElectricMachineResultsViewable"],
        "_1356": ["ElectricMachineForceViewOptions"],
        "_1358": ["LinearDQModel"],
        "_1359": ["MaximumTorqueResultsPoints"],
        "_1360": ["NonLinearDQModel"],
        "_1361": ["NonLinearDQModelGeneratorSettings"],
        "_1362": ["OnLoadElectricMachineResults"],
        "_1363": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
