"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4737 import CalculateFullFEResultsForMode
    from ._4738 import CampbellDiagramReport
    from ._4739 import ComponentPerModeResult
    from ._4740 import DesignEntityModalAnalysisGroupResults
    from ._4741 import ModalCMSResultsForModeAndFE
    from ._4742 import PerModeResultsReport
    from ._4743 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4744 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4745 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4746 import ShaftPerModeResult
    from ._4747 import SingleExcitationResultsModalAnalysis
    from ._4748 import SingleModeResults
else:
    import_structure = {
        "_4737": ["CalculateFullFEResultsForMode"],
        "_4738": ["CampbellDiagramReport"],
        "_4739": ["ComponentPerModeResult"],
        "_4740": ["DesignEntityModalAnalysisGroupResults"],
        "_4741": ["ModalCMSResultsForModeAndFE"],
        "_4742": ["PerModeResultsReport"],
        "_4743": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4744": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4745": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4746": ["ShaftPerModeResult"],
        "_4747": ["SingleExcitationResultsModalAnalysis"],
        "_4748": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)
