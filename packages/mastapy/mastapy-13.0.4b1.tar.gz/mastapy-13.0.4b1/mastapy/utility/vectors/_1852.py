"""PlaneVectorFieldData"""

from __future__ import annotations

from typing import TypeVar, List


from mastapy._internal.python_net import python_net_import
from mastapy._internal import conversion
from mastapy import _7574
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_PLANE_VECTOR_FIELD_DATA = python_net_import(
    "SMT.MastaAPI.Utility.Vectors", "PlaneVectorFieldData"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlaneVectorFieldData",)


Self = TypeVar("Self", bound="PlaneVectorFieldData")


class PlaneVectorFieldData(_7574.MarshalByRefObjectPermanent):
    """PlaneVectorFieldData

    This is a mastapy class.
    """

    TYPE = _PLANE_VECTOR_FIELD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlaneVectorFieldData")

    class _Cast_PlaneVectorFieldData:
        """Special nested class for casting PlaneVectorFieldData to subclasses."""

        def __init__(
            self: "PlaneVectorFieldData._Cast_PlaneVectorFieldData",
            parent: "PlaneVectorFieldData",
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "PlaneVectorFieldData._Cast_PlaneVectorFieldData",
        ) -> "_7574.MarshalByRefObjectPermanent":
            return self._parent._cast(_7574.MarshalByRefObjectPermanent)

        @property
        def plane_vector_field_data(
            self: "PlaneVectorFieldData._Cast_PlaneVectorFieldData",
        ) -> "PlaneVectorFieldData":
            return self._parent

        def __getattr__(
            self: "PlaneVectorFieldData._Cast_PlaneVectorFieldData", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlaneVectorFieldData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def titles(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Titles

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def values(self: Self) -> "List[List[float]]":
        """List[List[float]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PlaneVectorFieldData._Cast_PlaneVectorFieldData":
        return self._Cast_PlaneVectorFieldData(self)
