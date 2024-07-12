"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2453 import Assembly
    from ._2454 import AbstractAssembly
    from ._2455 import AbstractShaft
    from ._2456 import AbstractShaftOrHousing
    from ._2457 import AGMALoadSharingTableApplicationLevel
    from ._2458 import AxialInternalClearanceTolerance
    from ._2459 import Bearing
    from ._2460 import BearingF0InputMethod
    from ._2461 import BearingRaceMountingOptions
    from ._2462 import Bolt
    from ._2463 import BoltedJoint
    from ._2464 import Component
    from ._2465 import ComponentsConnectedResult
    from ._2466 import ConnectedSockets
    from ._2467 import Connector
    from ._2468 import Datum
    from ._2469 import ElectricMachineSearchRegionSpecificationMethod
    from ._2470 import EnginePartLoad
    from ._2471 import EngineSpeed
    from ._2472 import ExternalCADModel
    from ._2473 import FEPart
    from ._2474 import FlexiblePinAssembly
    from ._2475 import GuideDxfModel
    from ._2476 import GuideImage
    from ._2477 import GuideModelUsage
    from ._2478 import InnerBearingRaceMountingOptions
    from ._2479 import InternalClearanceTolerance
    from ._2480 import LoadSharingModes
    from ._2481 import LoadSharingSettings
    from ._2482 import MassDisc
    from ._2483 import MeasurementComponent
    from ._2484 import MountableComponent
    from ._2485 import OilLevelSpecification
    from ._2486 import OilSeal
    from ._2487 import OuterBearingRaceMountingOptions
    from ._2488 import Part
    from ._2489 import PlanetCarrier
    from ._2490 import PlanetCarrierSettings
    from ._2491 import PointLoad
    from ._2492 import PowerLoad
    from ._2493 import RadialInternalClearanceTolerance
    from ._2494 import RootAssembly
    from ._2495 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2496 import SpecialisedAssembly
    from ._2497 import UnbalancedMass
    from ._2498 import UnbalancedMassInclusionOption
    from ._2499 import VirtualComponent
    from ._2500 import WindTurbineBladeModeDetails
    from ._2501 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        "_2453": ["Assembly"],
        "_2454": ["AbstractAssembly"],
        "_2455": ["AbstractShaft"],
        "_2456": ["AbstractShaftOrHousing"],
        "_2457": ["AGMALoadSharingTableApplicationLevel"],
        "_2458": ["AxialInternalClearanceTolerance"],
        "_2459": ["Bearing"],
        "_2460": ["BearingF0InputMethod"],
        "_2461": ["BearingRaceMountingOptions"],
        "_2462": ["Bolt"],
        "_2463": ["BoltedJoint"],
        "_2464": ["Component"],
        "_2465": ["ComponentsConnectedResult"],
        "_2466": ["ConnectedSockets"],
        "_2467": ["Connector"],
        "_2468": ["Datum"],
        "_2469": ["ElectricMachineSearchRegionSpecificationMethod"],
        "_2470": ["EnginePartLoad"],
        "_2471": ["EngineSpeed"],
        "_2472": ["ExternalCADModel"],
        "_2473": ["FEPart"],
        "_2474": ["FlexiblePinAssembly"],
        "_2475": ["GuideDxfModel"],
        "_2476": ["GuideImage"],
        "_2477": ["GuideModelUsage"],
        "_2478": ["InnerBearingRaceMountingOptions"],
        "_2479": ["InternalClearanceTolerance"],
        "_2480": ["LoadSharingModes"],
        "_2481": ["LoadSharingSettings"],
        "_2482": ["MassDisc"],
        "_2483": ["MeasurementComponent"],
        "_2484": ["MountableComponent"],
        "_2485": ["OilLevelSpecification"],
        "_2486": ["OilSeal"],
        "_2487": ["OuterBearingRaceMountingOptions"],
        "_2488": ["Part"],
        "_2489": ["PlanetCarrier"],
        "_2490": ["PlanetCarrierSettings"],
        "_2491": ["PointLoad"],
        "_2492": ["PowerLoad"],
        "_2493": ["RadialInternalClearanceTolerance"],
        "_2494": ["RootAssembly"],
        "_2495": ["ShaftDiameterModificationDueToRollingBearingRing"],
        "_2496": ["SpecialisedAssembly"],
        "_2497": ["UnbalancedMass"],
        "_2498": ["UnbalancedMassInclusionOption"],
        "_2499": ["VirtualComponent"],
        "_2500": ["WindTurbineBladeModeDetails"],
        "_2501": ["WindTurbineSingleBladeDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
