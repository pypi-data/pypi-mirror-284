"""ComplexVector"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR = python_net_import("SMT.MastaAPI.MathUtility", "ComplexVector")

if TYPE_CHECKING:
    from mastapy.math_utility import _1515, _1516, _1532


__docformat__ = "restructuredtext en"
__all__ = ("ComplexVector",)


Self = TypeVar("Self", bound="ComplexVector")


class ComplexVector(_1512.ComplexMatrix):
    """ComplexVector

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComplexVector")

    class _Cast_ComplexVector:
        """Special nested class for casting ComplexVector to subclasses."""

        def __init__(
            self: "ComplexVector._Cast_ComplexVector", parent: "ComplexVector"
        ):
            self._parent = parent

        @property
        def complex_matrix(
            self: "ComplexVector._Cast_ComplexVector",
        ) -> "_1512.ComplexMatrix":
            return self._parent._cast(_1512.ComplexMatrix)

        @property
        def generic_matrix(
            self: "ComplexVector._Cast_ComplexVector",
        ) -> "_1532.GenericMatrix":
            from mastapy.math_utility import _1532

            return self._parent._cast(_1532.GenericMatrix)

        @property
        def complex_vector_3d(
            self: "ComplexVector._Cast_ComplexVector",
        ) -> "_1515.ComplexVector3D":
            from mastapy.math_utility import _1515

            return self._parent._cast(_1515.ComplexVector3D)

        @property
        def complex_vector_6d(
            self: "ComplexVector._Cast_ComplexVector",
        ) -> "_1516.ComplexVector6D":
            from mastapy.math_utility import _1516

            return self._parent._cast(_1516.ComplexVector6D)

        @property
        def complex_vector(
            self: "ComplexVector._Cast_ComplexVector",
        ) -> "ComplexVector":
            return self._parent

        def __getattr__(self: "ComplexVector._Cast_ComplexVector", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComplexVector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComplexVector._Cast_ComplexVector":
        return self._Cast_ComplexVector(self)
