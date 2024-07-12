"""ShaftDamageResultsTableAndChart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftDamageResultsTableAndChart"
)

if TYPE_CHECKING:
    from mastapy.utility.enums import _1838
    from mastapy.utility.report import _1787, _1788, _1789, _1781


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDamageResultsTableAndChart",)


Self = TypeVar("Self", bound="ShaftDamageResultsTableAndChart")


class ShaftDamageResultsTableAndChart(_1774.CustomReportChart):
    """ShaftDamageResultsTableAndChart

    This is a mastapy class.
    """

    TYPE = _SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftDamageResultsTableAndChart")

    class _Cast_ShaftDamageResultsTableAndChart:
        """Special nested class for casting ShaftDamageResultsTableAndChart to subclasses."""

        def __init__(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
            parent: "ShaftDamageResultsTableAndChart",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "_1774.CustomReportChart":
            return self._parent._cast(_1774.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "_1787.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "_1788.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1788

            return self._parent._cast(_1788.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "_1789.CustomReportNameableItem":
            from mastapy.utility.report import _1789

            return self._parent._cast(_1789.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "_1781.CustomReportItem":
            from mastapy.utility.report import _1781

            return self._parent._cast(_1781.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
        ) -> "ShaftDamageResultsTableAndChart":
            return self._parent

        def __getattr__(
            self: "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftDamageResultsTableAndChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display(self: Self) -> "_1838.TableAndChartOptions":
        """mastapy.utility.enums.TableAndChartOptions"""
        temp = self.wrapped.Display

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.enums._1838", "TableAndChartOptions"
        )(value)

    @display.setter
    @enforce_parameter_types
    def display(self: Self, value: "_1838.TableAndChartOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )
        self.wrapped.Display = value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart":
        return self._Cast_ShaftDamageResultsTableAndChart(self)
