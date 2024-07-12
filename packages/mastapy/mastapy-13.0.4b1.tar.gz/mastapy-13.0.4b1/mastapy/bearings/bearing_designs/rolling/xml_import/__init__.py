"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2196 import AbstractXmlVariableAssignment
    from ._2197 import BearingImportFile
    from ._2198 import RollingBearingImporter
    from ._2199 import XmlBearingTypeMapping
    from ._2200 import XMLVariableAssignment
else:
    import_structure = {
        "_2196": ["AbstractXmlVariableAssignment"],
        "_2197": ["BearingImportFile"],
        "_2198": ["RollingBearingImporter"],
        "_2199": ["XmlBearingTypeMapping"],
        "_2200": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)
