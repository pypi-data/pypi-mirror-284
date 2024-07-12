"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1233 import AbstractGearAnalysis
    from ._1234 import AbstractGearMeshAnalysis
    from ._1235 import AbstractGearSetAnalysis
    from ._1236 import GearDesignAnalysis
    from ._1237 import GearImplementationAnalysis
    from ._1238 import GearImplementationAnalysisDutyCycle
    from ._1239 import GearImplementationDetail
    from ._1240 import GearMeshDesignAnalysis
    from ._1241 import GearMeshImplementationAnalysis
    from ._1242 import GearMeshImplementationAnalysisDutyCycle
    from ._1243 import GearMeshImplementationDetail
    from ._1244 import GearSetDesignAnalysis
    from ._1245 import GearSetGroupDutyCycle
    from ._1246 import GearSetImplementationAnalysis
    from ._1247 import GearSetImplementationAnalysisAbstract
    from ._1248 import GearSetImplementationAnalysisDutyCycle
    from ._1249 import GearSetImplementationDetail
else:
    import_structure = {
        "_1233": ["AbstractGearAnalysis"],
        "_1234": ["AbstractGearMeshAnalysis"],
        "_1235": ["AbstractGearSetAnalysis"],
        "_1236": ["GearDesignAnalysis"],
        "_1237": ["GearImplementationAnalysis"],
        "_1238": ["GearImplementationAnalysisDutyCycle"],
        "_1239": ["GearImplementationDetail"],
        "_1240": ["GearMeshDesignAnalysis"],
        "_1241": ["GearMeshImplementationAnalysis"],
        "_1242": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1243": ["GearMeshImplementationDetail"],
        "_1244": ["GearSetDesignAnalysis"],
        "_1245": ["GearSetGroupDutyCycle"],
        "_1246": ["GearSetImplementationAnalysis"],
        "_1247": ["GearSetImplementationAnalysisAbstract"],
        "_1248": ["GearSetImplementationAnalysisDutyCycle"],
        "_1249": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
