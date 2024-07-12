"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1194 import ConceptGearDesign
    from ._1195 import ConceptGearMeshDesign
    from ._1196 import ConceptGearSetDesign
else:
    import_structure = {
        "_1194": ["ConceptGearDesign"],
        "_1195": ["ConceptGearMeshDesign"],
        "_1196": ["ConceptGearSetDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDesign",
    "ConceptGearMeshDesign",
    "ConceptGearSetDesign",
)
