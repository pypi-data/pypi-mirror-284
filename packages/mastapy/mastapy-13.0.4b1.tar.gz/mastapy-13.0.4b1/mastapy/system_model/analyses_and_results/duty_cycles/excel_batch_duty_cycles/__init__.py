"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6558 import ExcelBatchDutyCycleCreator
    from ._6559 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6560 import ExcelFileDetails
    from ._6561 import ExcelSheet
    from ._6562 import ExcelSheetDesignStateSelector
    from ._6563 import MASTAFileDetails
else:
    import_structure = {
        "_6558": ["ExcelBatchDutyCycleCreator"],
        "_6559": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6560": ["ExcelFileDetails"],
        "_6561": ["ExcelSheet"],
        "_6562": ["ExcelSheetDesignStateSelector"],
        "_6563": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)
