"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1557 import AbstractOptimisable
    from ._1558 import DesignSpaceSearchStrategyDatabase
    from ._1559 import InputSetter
    from ._1560 import Optimisable
    from ._1561 import OptimisationHistory
    from ._1562 import OptimizationInput
    from ._1563 import OptimizationVariable
    from ._1564 import ParetoOptimisationFilter
    from ._1565 import ParetoOptimisationInput
    from ._1566 import ParetoOptimisationOutput
    from ._1567 import ParetoOptimisationStrategy
    from ._1568 import ParetoOptimisationStrategyBars
    from ._1569 import ParetoOptimisationStrategyChartInformation
    from ._1570 import ParetoOptimisationStrategyDatabase
    from ._1571 import ParetoOptimisationVariable
    from ._1572 import ParetoOptimisationVariableBase
    from ._1573 import PropertyTargetForDominantCandidateSearch
    from ._1574 import ReportingOptimizationInput
    from ._1575 import SpecifyOptimisationInputAs
    from ._1576 import TargetingPropertyTo
else:
    import_structure = {
        "_1557": ["AbstractOptimisable"],
        "_1558": ["DesignSpaceSearchStrategyDatabase"],
        "_1559": ["InputSetter"],
        "_1560": ["Optimisable"],
        "_1561": ["OptimisationHistory"],
        "_1562": ["OptimizationInput"],
        "_1563": ["OptimizationVariable"],
        "_1564": ["ParetoOptimisationFilter"],
        "_1565": ["ParetoOptimisationInput"],
        "_1566": ["ParetoOptimisationOutput"],
        "_1567": ["ParetoOptimisationStrategy"],
        "_1568": ["ParetoOptimisationStrategyBars"],
        "_1569": ["ParetoOptimisationStrategyChartInformation"],
        "_1570": ["ParetoOptimisationStrategyDatabase"],
        "_1571": ["ParetoOptimisationVariable"],
        "_1572": ["ParetoOptimisationVariableBase"],
        "_1573": ["PropertyTargetForDominantCandidateSearch"],
        "_1574": ["ReportingOptimizationInput"],
        "_1575": ["SpecifyOptimisationInputAs"],
        "_1576": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
