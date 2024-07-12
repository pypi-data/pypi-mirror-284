"""BubbleChartDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility_gui.charts import _1882
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BUBBLE_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "BubbleChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1887, _1879
    from mastapy.utility.report import _1766


__docformat__ = "restructuredtext en"
__all__ = ("BubbleChartDefinition",)


Self = TypeVar("Self", bound="BubbleChartDefinition")


class BubbleChartDefinition(_1882.ScatterChartDefinition):
    """BubbleChartDefinition

    This is a mastapy class.
    """

    TYPE = _BUBBLE_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BubbleChartDefinition")

    class _Cast_BubbleChartDefinition:
        """Special nested class for casting BubbleChartDefinition to subclasses."""

        def __init__(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
            parent: "BubbleChartDefinition",
        ):
            self._parent = parent

        @property
        def scatter_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1882.ScatterChartDefinition":
            return self._parent._cast(_1882.ScatterChartDefinition)

        @property
        def two_d_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1887.TwoDChartDefinition":
            from mastapy.utility_gui.charts import _1887

            return self._parent._cast(_1887.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1879.NDChartDefinition":
            from mastapy.utility_gui.charts import _1879

            return self._parent._cast(_1879.NDChartDefinition)

        @property
        def chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "_1766.ChartDefinition":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition",
        ) -> "BubbleChartDefinition":
            return self._parent

        def __getattr__(
            self: "BubbleChartDefinition._Cast_BubbleChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BubbleChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BubbleChartDefinition._Cast_BubbleChartDefinition":
        return self._Cast_BubbleChartDefinition(self)
