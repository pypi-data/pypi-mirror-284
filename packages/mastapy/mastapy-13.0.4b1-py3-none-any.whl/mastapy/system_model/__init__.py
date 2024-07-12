"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2220 import Design
    from ._2221 import ComponentDampingOption
    from ._2222 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2223 import DesignEntity
    from ._2224 import DesignEntityId
    from ._2225 import DesignSettings
    from ._2226 import DutyCycleImporter
    from ._2227 import DutyCycleImporterDesignEntityMatch
    from ._2228 import ElectricMachineGroup
    from ._2229 import ExternalFullFELoader
    from ._2230 import HypoidWindUpRemovalMethod
    from ._2231 import IncludeDutyCycleOption
    from ._2232 import MASTASettings
    from ._2233 import MemorySummary
    from ._2234 import MeshStiffnessModel
    from ._2235 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2236 import PowerLoadDragTorqueSpecificationMethod
    from ._2237 import PowerLoadInputTorqueSpecificationMethod
    from ._2238 import PowerLoadPIDControlSpeedInputType
    from ._2239 import PowerLoadType
    from ._2240 import RelativeComponentAlignment
    from ._2241 import RelativeOffsetOption
    from ._2242 import SystemReporting
    from ._2243 import ThermalExpansionOptionForGroundedNodes
    from ._2244 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2220": ["Design"],
        "_2221": ["ComponentDampingOption"],
        "_2222": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2223": ["DesignEntity"],
        "_2224": ["DesignEntityId"],
        "_2225": ["DesignSettings"],
        "_2226": ["DutyCycleImporter"],
        "_2227": ["DutyCycleImporterDesignEntityMatch"],
        "_2228": ["ElectricMachineGroup"],
        "_2229": ["ExternalFullFELoader"],
        "_2230": ["HypoidWindUpRemovalMethod"],
        "_2231": ["IncludeDutyCycleOption"],
        "_2232": ["MASTASettings"],
        "_2233": ["MemorySummary"],
        "_2234": ["MeshStiffnessModel"],
        "_2235": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2236": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2237": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2238": ["PowerLoadPIDControlSpeedInputType"],
        "_2239": ["PowerLoadType"],
        "_2240": ["RelativeComponentAlignment"],
        "_2241": ["RelativeOffsetOption"],
        "_2242": ["SystemReporting"],
        "_2243": ["ThermalExpansionOptionForGroundedNodes"],
        "_2244": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
