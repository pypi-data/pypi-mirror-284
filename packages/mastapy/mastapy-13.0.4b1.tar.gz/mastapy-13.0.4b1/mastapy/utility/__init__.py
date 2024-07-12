"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1595 import Command
    from ._1596 import AnalysisRunInformation
    from ._1597 import DispatcherHelper
    from ._1598 import EnvironmentSummary
    from ._1599 import ExternalFullFEFileOption
    from ._1600 import FileHistory
    from ._1601 import FileHistoryItem
    from ._1602 import FolderMonitor
    from ._1604 import IndependentReportablePropertiesBase
    from ._1605 import InputNamePrompter
    from ._1606 import IntegerRange
    from ._1607 import LoadCaseOverrideOption
    from ._1608 import MethodOutcome
    from ._1609 import MethodOutcomeWithResult
    from ._1610 import MKLVersion
    from ._1611 import NumberFormatInfoSummary
    from ._1612 import PerMachineSettings
    from ._1613 import PersistentSingleton
    from ._1614 import ProgramSettings
    from ._1615 import PushbulletSettings
    from ._1616 import RoundingMethods
    from ._1617 import SelectableFolder
    from ._1618 import SystemDirectory
    from ._1619 import SystemDirectoryPopulator
else:
    import_structure = {
        "_1595": ["Command"],
        "_1596": ["AnalysisRunInformation"],
        "_1597": ["DispatcherHelper"],
        "_1598": ["EnvironmentSummary"],
        "_1599": ["ExternalFullFEFileOption"],
        "_1600": ["FileHistory"],
        "_1601": ["FileHistoryItem"],
        "_1602": ["FolderMonitor"],
        "_1604": ["IndependentReportablePropertiesBase"],
        "_1605": ["InputNamePrompter"],
        "_1606": ["IntegerRange"],
        "_1607": ["LoadCaseOverrideOption"],
        "_1608": ["MethodOutcome"],
        "_1609": ["MethodOutcomeWithResult"],
        "_1610": ["MKLVersion"],
        "_1611": ["NumberFormatInfoSummary"],
        "_1612": ["PerMachineSettings"],
        "_1613": ["PersistentSingleton"],
        "_1614": ["ProgramSettings"],
        "_1615": ["PushbulletSettings"],
        "_1616": ["RoundingMethods"],
        "_1617": ["SelectableFolder"],
        "_1618": ["SystemDirectory"],
        "_1619": ["SystemDirectoryPopulator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Command",
    "AnalysisRunInformation",
    "DispatcherHelper",
    "EnvironmentSummary",
    "ExternalFullFEFileOption",
    "FileHistory",
    "FileHistoryItem",
    "FolderMonitor",
    "IndependentReportablePropertiesBase",
    "InputNamePrompter",
    "IntegerRange",
    "LoadCaseOverrideOption",
    "MethodOutcome",
    "MethodOutcomeWithResult",
    "MKLVersion",
    "NumberFormatInfoSummary",
    "PerMachineSettings",
    "PersistentSingleton",
    "ProgramSettings",
    "PushbulletSettings",
    "RoundingMethods",
    "SelectableFolder",
    "SystemDirectory",
    "SystemDirectoryPopulator",
)
