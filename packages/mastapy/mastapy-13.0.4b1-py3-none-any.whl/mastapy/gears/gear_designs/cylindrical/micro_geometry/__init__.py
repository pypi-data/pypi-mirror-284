"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1105 import CylindricalGearBiasModification
    from ._1106 import CylindricalGearCommonFlankMicroGeometry
    from ._1107 import CylindricalGearFlankMicroGeometry
    from ._1108 import CylindricalGearLeadModification
    from ._1109 import CylindricalGearLeadModificationAtProfilePosition
    from ._1110 import CylindricalGearMeshMicroGeometry
    from ._1111 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1112 import CylindricalGearMicroGeometry
    from ._1113 import CylindricalGearMicroGeometryBase
    from ._1114 import CylindricalGearMicroGeometryDutyCycle
    from ._1115 import CylindricalGearMicroGeometryMap
    from ._1116 import CylindricalGearMicroGeometryPerTooth
    from ._1117 import CylindricalGearProfileModification
    from ._1118 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1119 import CylindricalGearSetMicroGeometry
    from ._1120 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1121 import CylindricalGearToothMicroGeometry
    from ._1122 import CylindricalGearTriangularEndModification
    from ._1123 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1124 import DrawDefiningGearOrBoth
    from ._1125 import GearAlignment
    from ._1126 import LeadFormReliefWithDeviation
    from ._1127 import LeadModificationForCustomer102CAD
    from ._1128 import LeadReliefSpecificationForCustomer102
    from ._1129 import LeadReliefWithDeviation
    from ._1130 import LeadSlopeReliefWithDeviation
    from ._1131 import LinearCylindricalGearTriangularEndModification
    from ._1132 import MeasuredMapDataTypes
    from ._1133 import MeshAlignment
    from ._1134 import MeshedCylindricalGearFlankMicroGeometry
    from ._1135 import MeshedCylindricalGearMicroGeometry
    from ._1136 import MicroGeometryLeadToleranceChartView
    from ._1137 import MicroGeometryViewingOptions
    from ._1138 import ModificationForCustomer102CAD
    from ._1139 import ParabolicCylindricalGearTriangularEndModification
    from ._1140 import ProfileFormReliefWithDeviation
    from ._1141 import ProfileModificationForCustomer102CAD
    from ._1142 import ProfileReliefSpecificationForCustomer102
    from ._1143 import ProfileReliefWithDeviation
    from ._1144 import ProfileSlopeReliefWithDeviation
    from ._1145 import ReliefWithDeviation
    from ._1146 import SingleCylindricalGearTriangularEndModification
    from ._1147 import TotalLeadReliefWithDeviation
    from ._1148 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1105": ["CylindricalGearBiasModification"],
        "_1106": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1107": ["CylindricalGearFlankMicroGeometry"],
        "_1108": ["CylindricalGearLeadModification"],
        "_1109": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1110": ["CylindricalGearMeshMicroGeometry"],
        "_1111": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1112": ["CylindricalGearMicroGeometry"],
        "_1113": ["CylindricalGearMicroGeometryBase"],
        "_1114": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1115": ["CylindricalGearMicroGeometryMap"],
        "_1116": ["CylindricalGearMicroGeometryPerTooth"],
        "_1117": ["CylindricalGearProfileModification"],
        "_1118": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1119": ["CylindricalGearSetMicroGeometry"],
        "_1120": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1121": ["CylindricalGearToothMicroGeometry"],
        "_1122": ["CylindricalGearTriangularEndModification"],
        "_1123": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1124": ["DrawDefiningGearOrBoth"],
        "_1125": ["GearAlignment"],
        "_1126": ["LeadFormReliefWithDeviation"],
        "_1127": ["LeadModificationForCustomer102CAD"],
        "_1128": ["LeadReliefSpecificationForCustomer102"],
        "_1129": ["LeadReliefWithDeviation"],
        "_1130": ["LeadSlopeReliefWithDeviation"],
        "_1131": ["LinearCylindricalGearTriangularEndModification"],
        "_1132": ["MeasuredMapDataTypes"],
        "_1133": ["MeshAlignment"],
        "_1134": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1135": ["MeshedCylindricalGearMicroGeometry"],
        "_1136": ["MicroGeometryLeadToleranceChartView"],
        "_1137": ["MicroGeometryViewingOptions"],
        "_1138": ["ModificationForCustomer102CAD"],
        "_1139": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1140": ["ProfileFormReliefWithDeviation"],
        "_1141": ["ProfileModificationForCustomer102CAD"],
        "_1142": ["ProfileReliefSpecificationForCustomer102"],
        "_1143": ["ProfileReliefWithDeviation"],
        "_1144": ["ProfileSlopeReliefWithDeviation"],
        "_1145": ["ReliefWithDeviation"],
        "_1146": ["SingleCylindricalGearTriangularEndModification"],
        "_1147": ["TotalLeadReliefWithDeviation"],
        "_1148": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadModificationForCustomer102CAD",
    "LeadReliefSpecificationForCustomer102",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ModificationForCustomer102CAD",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileModificationForCustomer102CAD",
    "ProfileReliefSpecificationForCustomer102",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
