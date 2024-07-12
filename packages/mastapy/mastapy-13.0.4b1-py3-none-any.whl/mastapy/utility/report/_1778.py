"""CustomReportDefinitionItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1789
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportDefinitionItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import (
        _1760,
        _1768,
        _1769,
        _1770,
        _1771,
        _1780,
        _1792,
        _1795,
        _1797,
        _1781,
    )
    from mastapy.bearings.bearing_results import _1967
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportDefinitionItem",)


Self = TypeVar("Self", bound="CustomReportDefinitionItem")


class CustomReportDefinitionItem(_1789.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_DEFINITION_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportDefinitionItem")

    class _Cast_CustomReportDefinitionItem:
        """Special nested class for casting CustomReportDefinitionItem to subclasses."""

        def __init__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            parent: "CustomReportDefinitionItem",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1789.CustomReportNameableItem":
            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1760.AdHocCustomTable":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1768.CustomChart":
            from mastapy.utility.report import _1768

            return self._parent._cast(_1768.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1769.CustomDrawing":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1770.CustomGraphic":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1771.CustomImage":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomImage)

        @property
        def custom_report_html_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1780.CustomReportHtmlItem":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomReportHtmlItem)

        @property
        def custom_report_status_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1792.CustomReportStatusItem":
            from mastapy.utility.report import _1792

            return self._parent._cast(_1792.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1795.CustomReportText":
            from mastapy.utility.report import _1795

            return self._parent._cast(_1795.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1797.CustomSubReport":
            from mastapy.utility.report import _1797

            return self._parent._cast(_1797.CustomSubReport)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1967.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingChartReporter)

        @property
        def parametric_study_histogram(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_4407.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.ParametricStudyHistogram)

        @property
        def custom_report_definition_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "CustomReportDefinitionItem":
            return self._parent

        def __getattr__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportDefinitionItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem":
        return self._Cast_CustomReportDefinitionItem(self)
