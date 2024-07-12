"""SynchroniserPartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SynchroniserPartPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4171,
        _4174,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserPartPowerFlow")


class SynchroniserPartPowerFlow(_4091.CouplingHalfPowerFlow):
    """SynchroniserPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartPowerFlow")

    class _Cast_SynchroniserPartPowerFlow:
        """Special nested class for casting SynchroniserPartPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
            parent: "SynchroniserPartPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4171.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4174.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserSleevePowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "SynchroniserPartPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow":
        return self._Cast_SynchroniserPartPowerFlow(self)
