"""CustomReportMultiPropertyItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.utility.report import _1788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1791, _1774, _1798, _1789, _1781
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1045
    from mastapy.utility_gui.charts import _1874, _1875
    from mastapy.bearings.bearing_results import _1966, _1970, _1978
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2870,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4738,
        _4742,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportMultiPropertyItem",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItem")
TItem = TypeVar("TItem", bound="_1791.CustomReportPropertyItem")


class CustomReportMultiPropertyItem(
    _1788.CustomReportMultiPropertyItemBase, Generic[TItem]
):
    """CustomReportMultiPropertyItem

    This is a mastapy class.

    Generic Types:
        TItem
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItem")

    class _Cast_CustomReportMultiPropertyItem:
        """Special nested class for casting CustomReportMultiPropertyItem to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
            parent: "CustomReportMultiPropertyItem",
        ):
            self._parent = parent

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1788.CustomReportMultiPropertyItemBase":
            return self._parent._cast(_1788.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1045.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1045

            return self._parent._cast(_1045.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1774.CustomReportChart":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportChart)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1798.CustomTable":
            from mastapy.utility.report import _1798

            return self._parent._cast(_1798.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1874.CustomLineChart":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1875.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1875

            return self._parent._cast(_1875.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1966.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1970.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_1978.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1978

            return self._parent._cast(_1978.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_2870.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2870,
            )

            return self._parent._cast(_2870.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_4738.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4738,
            )

            return self._parent._cast(_4738.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "_4742.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4742,
            )

            return self._parent._cast(_4742.PerModeResultsReport)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "CustomReportMultiPropertyItem":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportMultiPropertyItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem":
        return self._Cast_CustomReportMultiPropertyItem(self)
