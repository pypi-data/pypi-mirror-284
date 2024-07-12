"""LoadedRollerElementChartReporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_ELEMENT_CHART_REPORTER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedRollerElementChartReporter"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1787, _1788, _1789, _1781


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerElementChartReporter",)


Self = TypeVar("Self", bound="LoadedRollerElementChartReporter")


class LoadedRollerElementChartReporter(_1774.CustomReportChart):
    """LoadedRollerElementChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_ELEMENT_CHART_REPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerElementChartReporter")

    class _Cast_LoadedRollerElementChartReporter:
        """Special nested class for casting LoadedRollerElementChartReporter to subclasses."""

        def __init__(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
            parent: "LoadedRollerElementChartReporter",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "_1774.CustomReportChart":
            return self._parent._cast(_1774.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "_1787.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "_1788.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1788

            return self._parent._cast(_1788.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def loaded_roller_element_chart_reporter(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
        ) -> "LoadedRollerElementChartReporter":
            return self._parent

        def __getattr__(
            self: "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerElementChartReporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def only_show_roller_with_highest_load(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OnlyShowRollerWithHighestLoad

        if temp is None:
            return False

        return temp

    @only_show_roller_with_highest_load.setter
    @enforce_parameter_types
    def only_show_roller_with_highest_load(self: Self, value: "bool"):
        self.wrapped.OnlyShowRollerWithHighestLoad = (
            bool(value) if value is not None else False
        )

    @property
    def start_y_axis_at_zero(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.StartYAxisAtZero

        if temp is None:
            return False

        return temp

    @start_y_axis_at_zero.setter
    @enforce_parameter_types
    def start_y_axis_at_zero(self: Self, value: "bool"):
        self.wrapped.StartYAxisAtZero = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter":
        return self._Cast_LoadedRollerElementChartReporter(self)
