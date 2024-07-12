"""CustomReportItemContainerCollectionItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainerCollectionItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1776, _1793, _1781


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainerCollectionItem",)


Self = TypeVar("Self", bound="CustomReportItemContainerCollectionItem")


class CustomReportItemContainerCollectionItem(_1782.CustomReportItemContainer):
    """CustomReportItemContainerCollectionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CustomReportItemContainerCollectionItem"
    )

    class _Cast_CustomReportItemContainerCollectionItem:
        """Special nested class for casting CustomReportItemContainerCollectionItem to subclasses."""

        def __init__(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
            parent: "CustomReportItemContainerCollectionItem",
        ):
            self._parent = parent

        @property
        def custom_report_item_container(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "_1782.CustomReportItemContainer":
            return self._parent._cast(_1782.CustomReportItemContainer)

        @property
        def custom_report_item(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def custom_report_column(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "_1776.CustomReportColumn":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportColumn)

        @property
        def custom_report_tab(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "_1793.CustomReportTab":
            from mastapy.utility.report import _1793

            return self._parent._cast(_1793.CustomReportTab)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
        ) -> "CustomReportItemContainerCollectionItem":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem",
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
        self: Self, instance_to_wrap: "CustomReportItemContainerCollectionItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem":
        return self._Cast_CustomReportItemContainerCollectionItem(self)
