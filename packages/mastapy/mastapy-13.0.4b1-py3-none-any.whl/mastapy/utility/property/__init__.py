"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1854 import EnumWithSelectedValue
    from ._1856 import DeletableCollectionMember
    from ._1857 import DutyCyclePropertySummary
    from ._1858 import DutyCyclePropertySummaryForce
    from ._1859 import DutyCyclePropertySummaryPercentage
    from ._1860 import DutyCyclePropertySummarySmallAngle
    from ._1861 import DutyCyclePropertySummaryStress
    from ._1862 import DutyCyclePropertySummaryVeryShortLength
    from ._1863 import EnumWithBoolean
    from ._1864 import NamedRangeWithOverridableMinAndMax
    from ._1865 import TypedObjectsWithOption
else:
    import_structure = {
        "_1854": ["EnumWithSelectedValue"],
        "_1856": ["DeletableCollectionMember"],
        "_1857": ["DutyCyclePropertySummary"],
        "_1858": ["DutyCyclePropertySummaryForce"],
        "_1859": ["DutyCyclePropertySummaryPercentage"],
        "_1860": ["DutyCyclePropertySummarySmallAngle"],
        "_1861": ["DutyCyclePropertySummaryStress"],
        "_1862": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1863": ["EnumWithBoolean"],
        "_1864": ["NamedRangeWithOverridableMinAndMax"],
        "_1865": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
