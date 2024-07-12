"""Customer102DataSheetChangeLog"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOMER_102_DATA_SHEET_CHANGE_LOG = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Customer102DataSheetChangeLog"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1011


__docformat__ = "restructuredtext en"
__all__ = ("Customer102DataSheetChangeLog",)


Self = TypeVar("Self", bound="Customer102DataSheetChangeLog")


class Customer102DataSheetChangeLog(_0.APIBase):
    """Customer102DataSheetChangeLog

    This is a mastapy class.
    """

    TYPE = _CUSTOMER_102_DATA_SHEET_CHANGE_LOG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Customer102DataSheetChangeLog")

    class _Cast_Customer102DataSheetChangeLog:
        """Special nested class for casting Customer102DataSheetChangeLog to subclasses."""

        def __init__(
            self: "Customer102DataSheetChangeLog._Cast_Customer102DataSheetChangeLog",
            parent: "Customer102DataSheetChangeLog",
        ):
            self._parent = parent

        @property
        def customer_102_data_sheet_change_log(
            self: "Customer102DataSheetChangeLog._Cast_Customer102DataSheetChangeLog",
        ) -> "Customer102DataSheetChangeLog":
            return self._parent

        def __getattr__(
            self: "Customer102DataSheetChangeLog._Cast_Customer102DataSheetChangeLog",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Customer102DataSheetChangeLog.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def customer_102_data_sheet_change_log_items(
        self: Self,
    ) -> "List[_1011.Customer102DataSheetChangeLogItem]":
        """List[mastapy.gears.gear_designs.cylindrical.Customer102DataSheetChangeLogItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Customer102DataSheetChangeLogItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_entry_to_change_log(self: Self):
        """Method does not return."""
        self.wrapped.AddEntryToChangeLog()

    @property
    def cast_to(
        self: Self,
    ) -> "Customer102DataSheetChangeLog._Cast_Customer102DataSheetChangeLog":
        return self._Cast_Customer102DataSheetChangeLog(self)
