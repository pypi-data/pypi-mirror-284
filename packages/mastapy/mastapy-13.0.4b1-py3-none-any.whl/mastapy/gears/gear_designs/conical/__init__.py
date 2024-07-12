"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1168 import ActiveConicalFlank
    from ._1169 import BacklashDistributionRule
    from ._1170 import ConicalFlanks
    from ._1171 import ConicalGearCutter
    from ._1172 import ConicalGearDesign
    from ._1173 import ConicalGearMeshDesign
    from ._1174 import ConicalGearSetDesign
    from ._1175 import ConicalMachineSettingCalculationMethods
    from ._1176 import ConicalManufactureMethods
    from ._1177 import ConicalMeshedGearDesign
    from ._1178 import ConicalMeshMisalignments
    from ._1179 import CutterBladeType
    from ._1180 import CutterGaugeLengths
    from ._1181 import DummyConicalGearCutter
    from ._1182 import FrontEndTypes
    from ._1183 import GleasonSafetyRequirements
    from ._1184 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1185 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1186 import KlingelnbergFinishingMethods
    from ._1187 import LoadDistributionFactorMethods
    from ._1188 import TopremEntryType
    from ._1189 import TopremLetter
else:
    import_structure = {
        "_1168": ["ActiveConicalFlank"],
        "_1169": ["BacklashDistributionRule"],
        "_1170": ["ConicalFlanks"],
        "_1171": ["ConicalGearCutter"],
        "_1172": ["ConicalGearDesign"],
        "_1173": ["ConicalGearMeshDesign"],
        "_1174": ["ConicalGearSetDesign"],
        "_1175": ["ConicalMachineSettingCalculationMethods"],
        "_1176": ["ConicalManufactureMethods"],
        "_1177": ["ConicalMeshedGearDesign"],
        "_1178": ["ConicalMeshMisalignments"],
        "_1179": ["CutterBladeType"],
        "_1180": ["CutterGaugeLengths"],
        "_1181": ["DummyConicalGearCutter"],
        "_1182": ["FrontEndTypes"],
        "_1183": ["GleasonSafetyRequirements"],
        "_1184": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1185": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1186": ["KlingelnbergFinishingMethods"],
        "_1187": ["LoadDistributionFactorMethods"],
        "_1188": ["TopremEntryType"],
        "_1189": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
