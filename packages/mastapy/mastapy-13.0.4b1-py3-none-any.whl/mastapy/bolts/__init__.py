"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1483 import AxialLoadType
    from ._1484 import BoltedJointMaterial
    from ._1485 import BoltedJointMaterialDatabase
    from ._1486 import BoltGeometry
    from ._1487 import BoltGeometryDatabase
    from ._1488 import BoltMaterial
    from ._1489 import BoltMaterialDatabase
    from ._1490 import BoltSection
    from ._1491 import BoltShankType
    from ._1492 import BoltTypes
    from ._1493 import ClampedSection
    from ._1494 import ClampedSectionMaterialDatabase
    from ._1495 import DetailedBoltDesign
    from ._1496 import DetailedBoltedJointDesign
    from ._1497 import HeadCapTypes
    from ._1498 import JointGeometries
    from ._1499 import JointTypes
    from ._1500 import LoadedBolt
    from ._1501 import RolledBeforeOrAfterHeatTreatment
    from ._1502 import StandardSizes
    from ._1503 import StrengthGrades
    from ._1504 import ThreadTypes
    from ._1505 import TighteningTechniques
else:
    import_structure = {
        "_1483": ["AxialLoadType"],
        "_1484": ["BoltedJointMaterial"],
        "_1485": ["BoltedJointMaterialDatabase"],
        "_1486": ["BoltGeometry"],
        "_1487": ["BoltGeometryDatabase"],
        "_1488": ["BoltMaterial"],
        "_1489": ["BoltMaterialDatabase"],
        "_1490": ["BoltSection"],
        "_1491": ["BoltShankType"],
        "_1492": ["BoltTypes"],
        "_1493": ["ClampedSection"],
        "_1494": ["ClampedSectionMaterialDatabase"],
        "_1495": ["DetailedBoltDesign"],
        "_1496": ["DetailedBoltedJointDesign"],
        "_1497": ["HeadCapTypes"],
        "_1498": ["JointGeometries"],
        "_1499": ["JointTypes"],
        "_1500": ["LoadedBolt"],
        "_1501": ["RolledBeforeOrAfterHeatTreatment"],
        "_1502": ["StandardSizes"],
        "_1503": ["StrengthGrades"],
        "_1504": ["ThreadTypes"],
        "_1505": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
