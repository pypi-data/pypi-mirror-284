"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1921 import BearingConnectionComponent
    from ._1922 import InternalClearanceClass
    from ._1923 import BearingToleranceClass
    from ._1924 import BearingToleranceDefinitionOptions
    from ._1925 import FitType
    from ._1926 import InnerRingTolerance
    from ._1927 import InnerSupportTolerance
    from ._1928 import InterferenceDetail
    from ._1929 import InterferenceTolerance
    from ._1930 import ITDesignation
    from ._1931 import MountingSleeveDiameterDetail
    from ._1932 import OuterRingTolerance
    from ._1933 import OuterSupportTolerance
    from ._1934 import RaceDetail
    from ._1935 import RaceRoundnessAtAngle
    from ._1936 import RadialSpecificationMethod
    from ._1937 import RingTolerance
    from ._1938 import RoundnessSpecification
    from ._1939 import RoundnessSpecificationType
    from ._1940 import SupportDetail
    from ._1941 import SupportMaterialSource
    from ._1942 import SupportTolerance
    from ._1943 import SupportToleranceLocationDesignation
    from ._1944 import ToleranceCombination
    from ._1945 import TypeOfFit
else:
    import_structure = {
        "_1921": ["BearingConnectionComponent"],
        "_1922": ["InternalClearanceClass"],
        "_1923": ["BearingToleranceClass"],
        "_1924": ["BearingToleranceDefinitionOptions"],
        "_1925": ["FitType"],
        "_1926": ["InnerRingTolerance"],
        "_1927": ["InnerSupportTolerance"],
        "_1928": ["InterferenceDetail"],
        "_1929": ["InterferenceTolerance"],
        "_1930": ["ITDesignation"],
        "_1931": ["MountingSleeveDiameterDetail"],
        "_1932": ["OuterRingTolerance"],
        "_1933": ["OuterSupportTolerance"],
        "_1934": ["RaceDetail"],
        "_1935": ["RaceRoundnessAtAngle"],
        "_1936": ["RadialSpecificationMethod"],
        "_1937": ["RingTolerance"],
        "_1938": ["RoundnessSpecification"],
        "_1939": ["RoundnessSpecificationType"],
        "_1940": ["SupportDetail"],
        "_1941": ["SupportMaterialSource"],
        "_1942": ["SupportTolerance"],
        "_1943": ["SupportToleranceLocationDesignation"],
        "_1944": ["ToleranceCombination"],
        "_1945": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
