"""PlaneScalarFieldData"""

from __future__ import annotations

from typing import TypeVar, List


from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _7574
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_PLANE_SCALAR_FIELD_DATA = python_net_import(
    "SMT.MastaAPI.Utility.Vectors", "PlaneScalarFieldData"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlaneScalarFieldData",)


Self = TypeVar("Self", bound="PlaneScalarFieldData")


class PlaneScalarFieldData(_7574.MarshalByRefObjectPermanent):
    """PlaneScalarFieldData

    This is a mastapy class.
    """

    TYPE = _PLANE_SCALAR_FIELD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlaneScalarFieldData")

    class _Cast_PlaneScalarFieldData:
        """Special nested class for casting PlaneScalarFieldData to subclasses."""

        def __init__(
            self: "PlaneScalarFieldData._Cast_PlaneScalarFieldData",
            parent: "PlaneScalarFieldData",
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "PlaneScalarFieldData._Cast_PlaneScalarFieldData",
        ) -> "_7574.MarshalByRefObjectPermanent":
            return self._parent._cast(_7574.MarshalByRefObjectPermanent)

        @property
        def plane_scalar_field_data(
            self: "PlaneScalarFieldData._Cast_PlaneScalarFieldData",
        ) -> "PlaneScalarFieldData":
            return self._parent

        def __getattr__(
            self: "PlaneScalarFieldData._Cast_PlaneScalarFieldData", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlaneScalarFieldData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XTitle

        if temp is None:
            return ""

        return temp

    @property
    def y_title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YTitle

        if temp is None:
            return ""

        return temp

    @property
    def z_title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZTitle

        if temp is None:
            return ""

        return temp

    @enforce_parameter_types
    def to_regular_gridded_points(
        self: Self, extrapolate: "bool"
    ) -> "List[List[float]]":
        """List[List[float]]

        Args:
            extrapolate (bool)
        """
        extrapolate = bool(extrapolate)
        return conversion.pn_to_mp_list_float_2d(
            self.wrapped.ToRegularGriddedPoints(extrapolate if extrapolate else False)
        )

    def to_irregular_points(self: Self) -> "List[List[float]]":
        """List[List[float]]"""
        return conversion.pn_to_mp_list_float_2d(self.wrapped.ToIrregularPoints())

    @property
    def cast_to(self: Self) -> "PlaneScalarFieldData._Cast_PlaneScalarFieldData":
        return self._Cast_PlaneScalarFieldData(self)
