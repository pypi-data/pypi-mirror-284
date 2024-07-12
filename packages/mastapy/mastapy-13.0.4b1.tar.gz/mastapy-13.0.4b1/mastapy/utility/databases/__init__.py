"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1842 import Database
    from ._1843 import DatabaseConnectionSettings
    from ._1844 import DatabaseKey
    from ._1845 import DatabaseSettings
    from ._1846 import NamedDatabase
    from ._1847 import NamedDatabaseItem
    from ._1848 import NamedKey
    from ._1849 import SQLDatabase
else:
    import_structure = {
        "_1842": ["Database"],
        "_1843": ["DatabaseConnectionSettings"],
        "_1844": ["DatabaseKey"],
        "_1845": ["DatabaseSettings"],
        "_1846": ["NamedDatabase"],
        "_1847": ["NamedDatabaseItem"],
        "_1848": ["NamedKey"],
        "_1849": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)
