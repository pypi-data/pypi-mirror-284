"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2281 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2282 import ExcitationAnalysisViewOption
    from ._2283 import ModalContributionViewOptions
else:
    import_structure = {
        "_2281": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2282": ["ExcitationAnalysisViewOption"],
        "_2283": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)
