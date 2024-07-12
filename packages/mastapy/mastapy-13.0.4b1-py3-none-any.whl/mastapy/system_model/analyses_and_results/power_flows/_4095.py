"""CVTPulleyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CVTPulleyPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4091,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyPowerFlow",)


Self = TypeVar("Self", bound="CVTPulleyPowerFlow")


class CVTPulleyPowerFlow(_4146.PulleyPowerFlow):
    """CVTPulleyPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyPowerFlow")

    class _Cast_CVTPulleyPowerFlow:
        """Special nested class for casting CVTPulleyPowerFlow to subclasses."""

        def __init__(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
            parent: "CVTPulleyPowerFlow",
        ):
            self._parent = parent

        @property
        def pulley_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4146.PulleyPowerFlow":
            return self._parent._cast(_4146.PulleyPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "CVTPulleyPowerFlow":
            return self._parent

        def __getattr__(self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow":
        return self._Cast_CVTPulleyPowerFlow(self)
