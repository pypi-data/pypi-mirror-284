"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1828 import NamedTuple1
    from ._1829 import NamedTuple2
    from ._1830 import NamedTuple3
    from ._1831 import NamedTuple4
    from ._1832 import NamedTuple5
    from ._1833 import NamedTuple6
    from ._1834 import NamedTuple7
else:
    import_structure = {
        "_1828": ["NamedTuple1"],
        "_1829": ["NamedTuple2"],
        "_1830": ["NamedTuple3"],
        "_1831": ["NamedTuple4"],
        "_1832": ["NamedTuple5"],
        "_1833": ["NamedTuple6"],
        "_1834": ["NamedTuple7"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "NamedTuple1",
    "NamedTuple2",
    "NamedTuple3",
    "NamedTuple4",
    "NamedTuple5",
    "NamedTuple6",
    "NamedTuple7",
)
