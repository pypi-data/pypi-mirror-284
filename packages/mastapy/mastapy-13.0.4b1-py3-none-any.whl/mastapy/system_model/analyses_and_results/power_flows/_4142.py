"""PointLoadPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4181
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PointLoadPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2491
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadPowerFlow",)


Self = TypeVar("Self", bound="PointLoadPowerFlow")


class PointLoadPowerFlow(_4181.VirtualComponentPowerFlow):
    """PointLoadPowerFlow

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadPowerFlow")

    class _Cast_PointLoadPowerFlow:
        """Special nested class for casting PointLoadPowerFlow to subclasses."""

        def __init__(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
            parent: "PointLoadPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4181.VirtualComponentPowerFlow":
            return self._parent._cast(_4181.VirtualComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def point_load_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "PointLoadPowerFlow":
            return self._parent

        def __getattr__(self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2491.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PointLoadPowerFlow._Cast_PointLoadPowerFlow":
        return self._Cast_PointLoadPowerFlow(self)
