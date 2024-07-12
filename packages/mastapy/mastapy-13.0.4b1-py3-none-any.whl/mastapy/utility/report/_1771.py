"""CustomImage"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_IMAGE = python_net_import("SMT.MastaAPI.Utility.Report", "CustomImage")

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1967
    from mastapy.utility.report import _1778, _1789, _1781


__docformat__ = "restructuredtext en"
__all__ = ("CustomImage",)


Self = TypeVar("Self", bound="CustomImage")


class CustomImage(_1770.CustomGraphic):
    """CustomImage

    This is a mastapy class.
    """

    TYPE = _CUSTOM_IMAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomImage")

    class _Cast_CustomImage:
        """Special nested class for casting CustomImage to subclasses."""

        def __init__(self: "CustomImage._Cast_CustomImage", parent: "CustomImage"):
            self._parent = parent

        @property
        def custom_graphic(
            self: "CustomImage._Cast_CustomImage",
        ) -> "_1770.CustomGraphic":
            return self._parent._cast(_1770.CustomGraphic)

        @property
        def custom_report_definition_item(
            self: "CustomImage._Cast_CustomImage",
        ) -> "_1778.CustomReportDefinitionItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomImage._Cast_CustomImage",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomImage._Cast_CustomImage",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomImage._Cast_CustomImage",
        ) -> "_1967.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingChartReporter)

        @property
        def custom_image(self: "CustomImage._Cast_CustomImage") -> "CustomImage":
            return self._parent

        def __getattr__(self: "CustomImage._Cast_CustomImage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomImage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomImage._Cast_CustomImage":
        return self._Cast_CustomImage(self)
