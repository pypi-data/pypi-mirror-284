"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2375 import AlignConnectedComponentOptions
    from ._2376 import AlignmentMethod
    from ._2377 import AlignmentMethodForRaceBearing
    from ._2378 import AlignmentUsingAxialNodePositions
    from ._2379 import AngleSource
    from ._2380 import BaseFEWithSelection
    from ._2381 import BatchOperations
    from ._2382 import BearingNodeAlignmentOption
    from ._2383 import BearingNodeOption
    from ._2384 import BearingRaceNodeLink
    from ._2385 import BearingRacePosition
    from ._2386 import ComponentOrientationOption
    from ._2387 import ContactPairWithSelection
    from ._2388 import CoordinateSystemWithSelection
    from ._2389 import CreateConnectedComponentOptions
    from ._2390 import DegreeOfFreedomBoundaryCondition
    from ._2391 import DegreeOfFreedomBoundaryConditionAngular
    from ._2392 import DegreeOfFreedomBoundaryConditionLinear
    from ._2393 import ElectricMachineDataSet
    from ._2394 import ElectricMachineDynamicLoadData
    from ._2395 import ElementFaceGroupWithSelection
    from ._2396 import ElementPropertiesWithSelection
    from ._2397 import FEEntityGroupWithSelection
    from ._2398 import FEExportSettings
    from ._2399 import FEPartDRIVASurfaceSelection
    from ._2400 import FEPartWithBatchOptions
    from ._2401 import FEStiffnessGeometry
    from ._2402 import FEStiffnessTester
    from ._2403 import FESubstructure
    from ._2404 import FESubstructureExportOptions
    from ._2405 import FESubstructureNode
    from ._2406 import FESubstructureNodeModeShape
    from ._2407 import FESubstructureNodeModeShapes
    from ._2408 import FESubstructureType
    from ._2409 import FESubstructureWithBatchOptions
    from ._2410 import FESubstructureWithSelection
    from ._2411 import FESubstructureWithSelectionComponents
    from ._2412 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2413 import FESubstructureWithSelectionForModalAnalysis
    from ._2414 import FESubstructureWithSelectionForStaticAnalysis
    from ._2415 import GearMeshingOptions
    from ._2416 import IndependentMASTACreatedCondensationNode
    from ._2417 import LinkComponentAxialPositionErrorReporter
    from ._2418 import LinkNodeSource
    from ._2419 import MaterialPropertiesWithSelection
    from ._2420 import NodeBoundaryConditionStaticAnalysis
    from ._2421 import NodeGroupWithSelection
    from ._2422 import NodeSelectionDepthOption
    from ._2423 import OptionsWhenExternalFEFileAlreadyExists
    from ._2424 import PerLinkExportOptions
    from ._2425 import PerNodeExportOptions
    from ._2426 import RaceBearingFE
    from ._2427 import RaceBearingFESystemDeflection
    from ._2428 import RaceBearingFEWithSelection
    from ._2429 import ReplacedShaftSelectionHelper
    from ._2430 import SystemDeflectionFEExportOptions
    from ._2431 import ThermalExpansionOption
else:
    import_structure = {
        "_2375": ["AlignConnectedComponentOptions"],
        "_2376": ["AlignmentMethod"],
        "_2377": ["AlignmentMethodForRaceBearing"],
        "_2378": ["AlignmentUsingAxialNodePositions"],
        "_2379": ["AngleSource"],
        "_2380": ["BaseFEWithSelection"],
        "_2381": ["BatchOperations"],
        "_2382": ["BearingNodeAlignmentOption"],
        "_2383": ["BearingNodeOption"],
        "_2384": ["BearingRaceNodeLink"],
        "_2385": ["BearingRacePosition"],
        "_2386": ["ComponentOrientationOption"],
        "_2387": ["ContactPairWithSelection"],
        "_2388": ["CoordinateSystemWithSelection"],
        "_2389": ["CreateConnectedComponentOptions"],
        "_2390": ["DegreeOfFreedomBoundaryCondition"],
        "_2391": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2392": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2393": ["ElectricMachineDataSet"],
        "_2394": ["ElectricMachineDynamicLoadData"],
        "_2395": ["ElementFaceGroupWithSelection"],
        "_2396": ["ElementPropertiesWithSelection"],
        "_2397": ["FEEntityGroupWithSelection"],
        "_2398": ["FEExportSettings"],
        "_2399": ["FEPartDRIVASurfaceSelection"],
        "_2400": ["FEPartWithBatchOptions"],
        "_2401": ["FEStiffnessGeometry"],
        "_2402": ["FEStiffnessTester"],
        "_2403": ["FESubstructure"],
        "_2404": ["FESubstructureExportOptions"],
        "_2405": ["FESubstructureNode"],
        "_2406": ["FESubstructureNodeModeShape"],
        "_2407": ["FESubstructureNodeModeShapes"],
        "_2408": ["FESubstructureType"],
        "_2409": ["FESubstructureWithBatchOptions"],
        "_2410": ["FESubstructureWithSelection"],
        "_2411": ["FESubstructureWithSelectionComponents"],
        "_2412": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2413": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2414": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2415": ["GearMeshingOptions"],
        "_2416": ["IndependentMASTACreatedCondensationNode"],
        "_2417": ["LinkComponentAxialPositionErrorReporter"],
        "_2418": ["LinkNodeSource"],
        "_2419": ["MaterialPropertiesWithSelection"],
        "_2420": ["NodeBoundaryConditionStaticAnalysis"],
        "_2421": ["NodeGroupWithSelection"],
        "_2422": ["NodeSelectionDepthOption"],
        "_2423": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2424": ["PerLinkExportOptions"],
        "_2425": ["PerNodeExportOptions"],
        "_2426": ["RaceBearingFE"],
        "_2427": ["RaceBearingFESystemDeflection"],
        "_2428": ["RaceBearingFEWithSelection"],
        "_2429": ["ReplacedShaftSelectionHelper"],
        "_2430": ["SystemDeflectionFEExportOptions"],
        "_2431": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
