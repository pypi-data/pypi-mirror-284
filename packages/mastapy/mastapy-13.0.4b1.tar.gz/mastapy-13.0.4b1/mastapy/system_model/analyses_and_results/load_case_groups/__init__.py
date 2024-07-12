"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5679 import AbstractDesignStateLoadCaseGroup
    from ._5680 import AbstractLoadCaseGroup
    from ._5681 import AbstractStaticLoadCaseGroup
    from ._5682 import ClutchEngagementStatus
    from ._5683 import ConceptSynchroGearEngagementStatus
    from ._5684 import DesignState
    from ._5685 import DutyCycle
    from ._5686 import GenericClutchEngagementStatus
    from ._5687 import LoadCaseGroupHistograms
    from ._5688 import SubGroupInSingleDesignState
    from ._5689 import SystemOptimisationGearSet
    from ._5690 import SystemOptimiserGearSetOptimisation
    from ._5691 import SystemOptimiserTargets
    from ._5692 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5679": ["AbstractDesignStateLoadCaseGroup"],
        "_5680": ["AbstractLoadCaseGroup"],
        "_5681": ["AbstractStaticLoadCaseGroup"],
        "_5682": ["ClutchEngagementStatus"],
        "_5683": ["ConceptSynchroGearEngagementStatus"],
        "_5684": ["DesignState"],
        "_5685": ["DutyCycle"],
        "_5686": ["GenericClutchEngagementStatus"],
        "_5687": ["LoadCaseGroupHistograms"],
        "_5688": ["SubGroupInSingleDesignState"],
        "_5689": ["SystemOptimisationGearSet"],
        "_5690": ["SystemOptimiserGearSetOptimisation"],
        "_5691": ["SystemOptimiserTargets"],
        "_5692": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
