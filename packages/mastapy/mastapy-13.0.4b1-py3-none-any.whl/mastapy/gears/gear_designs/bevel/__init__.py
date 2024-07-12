"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1197 import AGMAGleasonConicalGearGeometryMethods
    from ._1198 import BevelGearDesign
    from ._1199 import BevelGearMeshDesign
    from ._1200 import BevelGearSetDesign
    from ._1201 import BevelMeshedGearDesign
    from ._1202 import DrivenMachineCharacteristicGleason
    from ._1203 import EdgeRadiusType
    from ._1204 import FinishingMethods
    from ._1205 import MachineCharacteristicAGMAKlingelnberg
    from ._1206 import PrimeMoverCharacteristicGleason
    from ._1207 import ToothProportionsInputMethod
    from ._1208 import ToothThicknessSpecificationMethod
    from ._1209 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1197": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1198": ["BevelGearDesign"],
        "_1199": ["BevelGearMeshDesign"],
        "_1200": ["BevelGearSetDesign"],
        "_1201": ["BevelMeshedGearDesign"],
        "_1202": ["DrivenMachineCharacteristicGleason"],
        "_1203": ["EdgeRadiusType"],
        "_1204": ["FinishingMethods"],
        "_1205": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1206": ["PrimeMoverCharacteristicGleason"],
        "_1207": ["ToothProportionsInputMethod"],
        "_1208": ["ToothThicknessSpecificationMethod"],
        "_1209": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
