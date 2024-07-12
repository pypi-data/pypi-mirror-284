"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1469 import ContactSpecification
    from ._1470 import CrowningSpecificationMethod
    from ._1471 import CycloidalAssemblyDesign
    from ._1472 import CycloidalDiscDesign
    from ._1473 import CycloidalDiscDesignExporter
    from ._1474 import CycloidalDiscMaterial
    from ._1475 import CycloidalDiscMaterialDatabase
    from ._1476 import CycloidalDiscModificationsSpecification
    from ._1477 import DirectionOfMeasuredModifications
    from ._1478 import GeometryToExport
    from ._1479 import NamedDiscPhase
    from ._1480 import RingPinsDesign
    from ._1481 import RingPinsMaterial
    from ._1482 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1469": ["ContactSpecification"],
        "_1470": ["CrowningSpecificationMethod"],
        "_1471": ["CycloidalAssemblyDesign"],
        "_1472": ["CycloidalDiscDesign"],
        "_1473": ["CycloidalDiscDesignExporter"],
        "_1474": ["CycloidalDiscMaterial"],
        "_1475": ["CycloidalDiscMaterialDatabase"],
        "_1476": ["CycloidalDiscModificationsSpecification"],
        "_1477": ["DirectionOfMeasuredModifications"],
        "_1478": ["GeometryToExport"],
        "_1479": ["NamedDiscPhase"],
        "_1480": ["RingPinsDesign"],
        "_1481": ["RingPinsMaterial"],
        "_1482": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
