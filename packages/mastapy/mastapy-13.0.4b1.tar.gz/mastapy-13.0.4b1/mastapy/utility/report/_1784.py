"""CustomReportItemContainerCollectionBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1781
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainerCollectionBase"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1777, _1783, _1794


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainerCollectionBase",)


Self = TypeVar("Self", bound="CustomReportItemContainerCollectionBase")


class CustomReportItemContainerCollectionBase(_1781.CustomReportItem):
    """CustomReportItemContainerCollectionBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CustomReportItemContainerCollectionBase"
    )

    class _Cast_CustomReportItemContainerCollectionBase:
        """Special nested class for casting CustomReportItemContainerCollectionBase to subclasses."""

        def __init__(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
            parent: "CustomReportItemContainerCollectionBase",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
        ) -> "_1781.CustomReportItem":
            return self._parent._cast(_1781.CustomReportItem)

        @property
        def custom_report_columns(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
        ) -> "_1777.CustomReportColumns":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportColumns)

        @property
        def custom_report_item_container_collection(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
        ) -> "_1783.CustomReportItemContainerCollection":
            from mastapy.utility.report import _1783

            return self._parent._cast(_1783.CustomReportItemContainerCollection)

        @property
        def custom_report_tabs(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
        ) -> "_1794.CustomReportTabs":
            from mastapy.utility.report import _1794

            return self._parent._cast(_1794.CustomReportTabs)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
        ) -> "CustomReportItemContainerCollectionBase":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase",
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
        self: Self, instance_to_wrap: "CustomReportItemContainerCollectionBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase":
        return self._Cast_CustomReportItemContainerCollectionBase(self)
