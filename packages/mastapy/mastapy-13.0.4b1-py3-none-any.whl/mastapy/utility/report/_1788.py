"""CustomReportMultiPropertyItemBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1789
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItemBase"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1045
    from mastapy.utility.report import _1774, _1787, _1798, _1781
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
__all__ = ("CustomReportMultiPropertyItemBase",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItemBase")


class CustomReportMultiPropertyItemBase(_1789.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItemBase")

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            parent: "CustomReportMultiPropertyItemBase",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1789.CustomReportNameableItem":
            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1045.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1045

            return self._parent._cast(_1045.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1774.CustomReportChart":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1787.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportMultiPropertyItem)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1798.CustomTable":
            from mastapy.utility.report import _1798

            return self._parent._cast(_1798.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1874.CustomLineChart":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1875.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1875

            return self._parent._cast(_1875.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1966.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1970.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1978.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1978

            return self._parent._cast(_1978.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_2870.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2870,
            )

            return self._parent._cast(_2870.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4738.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4738,
            )

            return self._parent._cast(_4738.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4742.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4742,
            )

            return self._parent._cast(_4742.PerModeResultsReport)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "CustomReportMultiPropertyItemBase":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
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
        self: Self, instance_to_wrap: "CustomReportMultiPropertyItemBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase":
        return self._Cast_CustomReportMultiPropertyItemBase(self)
