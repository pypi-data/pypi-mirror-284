"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1507 import Range
    from ._1508 import AcousticWeighting
    from ._1509 import AlignmentAxis
    from ._1510 import Axis
    from ._1511 import CirclesOnAxis
    from ._1512 import ComplexMatrix
    from ._1513 import ComplexPartDisplayOption
    from ._1514 import ComplexVector
    from ._1515 import ComplexVector3D
    from ._1516 import ComplexVector6D
    from ._1517 import CoordinateSystem3D
    from ._1518 import CoordinateSystemEditor
    from ._1519 import CoordinateSystemForRotation
    from ._1520 import CoordinateSystemForRotationOrigin
    from ._1521 import DataPrecision
    from ._1522 import DegreeOfFreedom
    from ._1523 import DynamicsResponseScalarResult
    from ._1524 import DynamicsResponseScaling
    from ._1525 import Eigenmode
    from ._1526 import Eigenmodes
    from ._1527 import EulerParameters
    from ._1528 import ExtrapolationOptions
    from ._1529 import FacetedBody
    from ._1530 import FacetedSurface
    from ._1531 import FourierSeries
    from ._1532 import GenericMatrix
    from ._1533 import GriddedSurface
    from ._1534 import HarmonicValue
    from ._1535 import InertiaTensor
    from ._1536 import MassProperties
    from ._1537 import MaxMinMean
    from ._1538 import ComplexMagnitudeMethod
    from ._1539 import MultipleFourierSeriesInterpolator
    from ._1540 import Named2DLocation
    from ._1541 import PIDControlUpdateMethod
    from ._1542 import Quaternion
    from ._1543 import RealMatrix
    from ._1544 import RealVector
    from ._1545 import ResultOptionsFor3DVector
    from ._1546 import RotationAxis
    from ._1547 import RoundedOrder
    from ._1548 import SinCurve
    from ._1549 import SquareMatrix
    from ._1550 import StressPoint
    from ._1551 import TransformMatrix3D
    from ._1552 import TranslationRotation
    from ._1553 import Vector2DListAccessor
    from ._1554 import Vector6D
else:
    import_structure = {
        "_1507": ["Range"],
        "_1508": ["AcousticWeighting"],
        "_1509": ["AlignmentAxis"],
        "_1510": ["Axis"],
        "_1511": ["CirclesOnAxis"],
        "_1512": ["ComplexMatrix"],
        "_1513": ["ComplexPartDisplayOption"],
        "_1514": ["ComplexVector"],
        "_1515": ["ComplexVector3D"],
        "_1516": ["ComplexVector6D"],
        "_1517": ["CoordinateSystem3D"],
        "_1518": ["CoordinateSystemEditor"],
        "_1519": ["CoordinateSystemForRotation"],
        "_1520": ["CoordinateSystemForRotationOrigin"],
        "_1521": ["DataPrecision"],
        "_1522": ["DegreeOfFreedom"],
        "_1523": ["DynamicsResponseScalarResult"],
        "_1524": ["DynamicsResponseScaling"],
        "_1525": ["Eigenmode"],
        "_1526": ["Eigenmodes"],
        "_1527": ["EulerParameters"],
        "_1528": ["ExtrapolationOptions"],
        "_1529": ["FacetedBody"],
        "_1530": ["FacetedSurface"],
        "_1531": ["FourierSeries"],
        "_1532": ["GenericMatrix"],
        "_1533": ["GriddedSurface"],
        "_1534": ["HarmonicValue"],
        "_1535": ["InertiaTensor"],
        "_1536": ["MassProperties"],
        "_1537": ["MaxMinMean"],
        "_1538": ["ComplexMagnitudeMethod"],
        "_1539": ["MultipleFourierSeriesInterpolator"],
        "_1540": ["Named2DLocation"],
        "_1541": ["PIDControlUpdateMethod"],
        "_1542": ["Quaternion"],
        "_1543": ["RealMatrix"],
        "_1544": ["RealVector"],
        "_1545": ["ResultOptionsFor3DVector"],
        "_1546": ["RotationAxis"],
        "_1547": ["RoundedOrder"],
        "_1548": ["SinCurve"],
        "_1549": ["SquareMatrix"],
        "_1550": ["StressPoint"],
        "_1551": ["TransformMatrix3D"],
        "_1552": ["TranslationRotation"],
        "_1553": ["Vector2DListAccessor"],
        "_1554": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
