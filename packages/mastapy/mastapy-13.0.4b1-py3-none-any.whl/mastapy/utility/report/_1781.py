"""CustomReportItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItem"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1045
    from mastapy.utility.report import (
        _1760,
        _1768,
        _1769,
        _1770,
        _1771,
        _1772,
        _1773,
        _1774,
        _1776,
        _1777,
        _1778,
        _1779,
        _1780,
        _1782,
        _1783,
        _1784,
        _1785,
        _1787,
        _1788,
        _1789,
        _1790,
        _1792,
        _1793,
        _1794,
        _1795,
        _1797,
        _1798,
        _1800,
    )
    from mastapy.utility_gui.charts import _1874, _1875
    from mastapy.bearings.bearing_results import _1966, _1967, _1970, _1978
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2870,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4738,
        _4742,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItem",)


Self = TypeVar("Self", bound="CustomReportItem")


class CustomReportItem(_0.APIBase):
    """CustomReportItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItem")

    class _Cast_CustomReportItem:
        """Special nested class for casting CustomReportItem to subclasses."""

        def __init__(
            self: "CustomReportItem._Cast_CustomReportItem", parent: "CustomReportItem"
        ):
            self._parent = parent

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1045.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1045

            return self._parent._cast(_1045.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1760.AdHocCustomTable":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1768.CustomChart":
            from mastapy.utility.report import _1768

            return self._parent._cast(_1768.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1769.CustomDrawing":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1770.CustomGraphic":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1771.CustomImage":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomImage)

        @property
        def custom_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1772.CustomReport":
            from mastapy.utility.report import _1772

            return self._parent._cast(_1772.CustomReport)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1773.CustomReportCadDrawing":
            from mastapy.utility.report import _1773

            return self._parent._cast(_1773.CustomReportCadDrawing)

        @property
        def custom_report_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1774.CustomReportChart":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportChart)

        @property
        def custom_report_column(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1776.CustomReportColumn":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportColumn)

        @property
        def custom_report_columns(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1777.CustomReportColumns":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportColumns)

        @property
        def custom_report_definition_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1778.CustomReportDefinitionItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportDefinitionItem)

        @property
        def custom_report_horizontal_line(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1779.CustomReportHorizontalLine":
            from mastapy.utility.report import _1779

            return self._parent._cast(_1779.CustomReportHorizontalLine)

        @property
        def custom_report_html_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1780.CustomReportHtmlItem":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomReportHtmlItem)

        @property
        def custom_report_item_container(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1782.CustomReportItemContainer":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.CustomReportItemContainer)

        @property
        def custom_report_item_container_collection(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1783.CustomReportItemContainerCollection":
            from mastapy.utility.report import _1783

            return self._parent._cast(_1783.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1784.CustomReportItemContainerCollectionBase":
            from mastapy.utility.report import _1784

            return self._parent._cast(_1784.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1785.CustomReportItemContainerCollectionItem":
            from mastapy.utility.report import _1785

            return self._parent._cast(_1785.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1787.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1788.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1788

            return self._parent._cast(_1788.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_named_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1790.CustomReportNamedItem":
            from mastapy.utility.report import _1790

            return self._parent._cast(_1790.CustomReportNamedItem)

        @property
        def custom_report_status_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1792.CustomReportStatusItem":
            from mastapy.utility.report import _1792

            return self._parent._cast(_1792.CustomReportStatusItem)

        @property
        def custom_report_tab(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1793.CustomReportTab":
            from mastapy.utility.report import _1793

            return self._parent._cast(_1793.CustomReportTab)

        @property
        def custom_report_tabs(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1794.CustomReportTabs":
            from mastapy.utility.report import _1794

            return self._parent._cast(_1794.CustomReportTabs)

        @property
        def custom_report_text(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1795.CustomReportText":
            from mastapy.utility.report import _1795

            return self._parent._cast(_1795.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1797.CustomSubReport":
            from mastapy.utility.report import _1797

            return self._parent._cast(_1797.CustomSubReport)

        @property
        def custom_table(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1798.CustomTable":
            from mastapy.utility.report import _1798

            return self._parent._cast(_1798.CustomTable)

        @property
        def dynamic_custom_report_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1800.DynamicCustomReportItem":
            from mastapy.utility.report import _1800

            return self._parent._cast(_1800.DynamicCustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1874.CustomLineChart":
            from mastapy.utility_gui.charts import _1874

            return self._parent._cast(_1874.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1875.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1875

            return self._parent._cast(_1875.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1966.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1967.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1970.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_1978.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1978

            return self._parent._cast(_1978.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_2870.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2870,
            )

            return self._parent._cast(_2870.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4407.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4738.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4738,
            )

            return self._parent._cast(_4738.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "_4742.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4742,
            )

            return self._parent._cast(_4742.PerModeResultsReport)

        @property
        def custom_report_item(
            self: "CustomReportItem._Cast_CustomReportItem",
        ) -> "CustomReportItem":
            return self._parent

        def __getattr__(self: "CustomReportItem._Cast_CustomReportItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    @enforce_parameter_types
    def is_main_report_item(self: Self, value: "bool"):
        self.wrapped.IsMainReportItem = bool(value) if value is not None else False

    @property
    def item_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ItemType

        if temp is None:
            return ""

        return temp

    def add_condition(self: Self):
        """Method does not return."""
        self.wrapped.AddCondition()

    @property
    def cast_to(self: Self) -> "CustomReportItem._Cast_CustomReportItem":
        return self._Cast_CustomReportItem(self)
