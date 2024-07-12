"""CustomReportChart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportChart"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.utility_gui.charts import _1874
    from mastapy.bearings.bearing_results import _1966, _1970, _1978
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2870,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4738,
        _4742,
    )
    from mastapy.utility.report import _1788, _1789, _1781


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportChart",)


Self = TypeVar("Self", bound="CustomReportChart")


class CustomReportChart(
    _1787.CustomReportMultiPropertyItem["_1775.CustomReportChartItem"]
):
    """CustomReportChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportChart")

    class _Cast_CustomReportChart:
        """Special nested class for casting CustomReportChart to subclasses."""

        def __init__(
            self: "CustomReportChart._Cast_CustomReportChart",
            parent: "CustomReportChart",
        ):
            self._parent = parent

        @property
        def custom_report_multi_property_item(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1787.CustomReportMultiPropertyItem":
            return self._parent._cast(_1787.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1788.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1788

            return self._parent._cast(_1788.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def custom_line_chart(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1874.CustomLineChart":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.CustomLineChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1966.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1970.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_1978.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1978

            return self._parent._cast(_1978.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_2870.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2870,
            )

            return self._parent._cast(_2870.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_4738.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4738,
            )

            return self._parent._cast(_4738.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "_4742.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4742,
            )

            return self._parent._cast(_4742.PerModeResultsReport)

        @property
        def custom_report_chart(
            self: "CustomReportChart._Cast_CustomReportChart",
        ) -> "CustomReportChart":
            return self._parent

        def __getattr__(self: "CustomReportChart._Cast_CustomReportChart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "int"):
        self.wrapped.Height = int(value) if value is not None else 0

    @property
    def width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "int"):
        self.wrapped.Width = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "CustomReportChart._Cast_CustomReportChart":
        return self._Cast_CustomReportChart(self)
