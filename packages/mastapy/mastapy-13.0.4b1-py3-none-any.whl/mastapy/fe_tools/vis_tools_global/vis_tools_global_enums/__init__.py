"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1252 import BeamSectionType
    from ._1253 import ContactPairConstrainedSurfaceType
    from ._1254 import ContactPairReferenceSurfaceType
    from ._1255 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1252": ["BeamSectionType"],
        "_1253": ["ContactPairConstrainedSurfaceType"],
        "_1254": ["ContactPairReferenceSurfaceType"],
        "_1255": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)
