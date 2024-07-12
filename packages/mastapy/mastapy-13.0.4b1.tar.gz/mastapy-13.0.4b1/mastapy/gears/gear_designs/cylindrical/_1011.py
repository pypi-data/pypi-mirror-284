"""Customer102DataSheetChangeLogItem"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOMER_102_DATA_SHEET_CHANGE_LOG_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Customer102DataSheetChangeLogItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("Customer102DataSheetChangeLogItem",)


Self = TypeVar("Self", bound="Customer102DataSheetChangeLogItem")


class Customer102DataSheetChangeLogItem(_0.APIBase):
    """Customer102DataSheetChangeLogItem

    This is a mastapy class.
    """

    TYPE = _CUSTOMER_102_DATA_SHEET_CHANGE_LOG_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Customer102DataSheetChangeLogItem")

    class _Cast_Customer102DataSheetChangeLogItem:
        """Special nested class for casting Customer102DataSheetChangeLogItem to subclasses."""

        def __init__(
            self: "Customer102DataSheetChangeLogItem._Cast_Customer102DataSheetChangeLogItem",
            parent: "Customer102DataSheetChangeLogItem",
        ):
            self._parent = parent

        @property
        def customer_102_data_sheet_change_log_item(
            self: "Customer102DataSheetChangeLogItem._Cast_Customer102DataSheetChangeLogItem",
        ) -> "Customer102DataSheetChangeLogItem":
            return self._parent

        def __getattr__(
            self: "Customer102DataSheetChangeLogItem._Cast_Customer102DataSheetChangeLogItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "Customer102DataSheetChangeLogItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Change

        if temp is None:
            return ""

        return temp

    @change.setter
    @enforce_parameter_types
    def change(self: Self, value: "str"):
        self.wrapped.Change = str(value) if value is not None else ""

    @property
    def engineer(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Engineer

        if temp is None:
            return ""

        return temp

    @engineer.setter
    @enforce_parameter_types
    def engineer(self: Self, value: "str"):
        self.wrapped.Engineer = str(value) if value is not None else ""

    @property
    def rev(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Rev

        if temp is None:
            return ""

        return temp

    @rev.setter
    @enforce_parameter_types
    def rev(self: Self, value: "str"):
        self.wrapped.Rev = str(value) if value is not None else ""

    def remove_revision(self: Self):
        """Method does not return."""
        self.wrapped.RemoveRevision()

    @property
    def cast_to(
        self: Self,
    ) -> "Customer102DataSheetChangeLogItem._Cast_Customer102DataSheetChangeLogItem":
        return self._Cast_Customer102DataSheetChangeLogItem(self)
