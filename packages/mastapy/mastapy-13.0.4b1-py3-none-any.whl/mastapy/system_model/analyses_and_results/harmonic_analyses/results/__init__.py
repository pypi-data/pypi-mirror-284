"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5865 import ConnectedComponentType
    from ._5866 import ExcitationSourceSelection
    from ._5867 import ExcitationSourceSelectionBase
    from ._5868 import ExcitationSourceSelectionGroup
    from ._5869 import HarmonicSelection
    from ._5870 import ModalContributionDisplayMethod
    from ._5871 import ModalContributionFilteringMethod
    from ._5872 import ResultLocationSelectionGroup
    from ._5873 import ResultLocationSelectionGroups
    from ._5874 import ResultNodeSelection
else:
    import_structure = {
        "_5865": ["ConnectedComponentType"],
        "_5866": ["ExcitationSourceSelection"],
        "_5867": ["ExcitationSourceSelectionBase"],
        "_5868": ["ExcitationSourceSelectionGroup"],
        "_5869": ["HarmonicSelection"],
        "_5870": ["ModalContributionDisplayMethod"],
        "_5871": ["ModalContributionFilteringMethod"],
        "_5872": ["ResultLocationSelectionGroup"],
        "_5873": ["ResultLocationSelectionGroups"],
        "_5874": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
