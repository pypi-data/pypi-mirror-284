"""AGMAGleasonConicalGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4059
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4201,
        _4206,
        _4252,
        _4289,
        _4295,
        _4298,
        _4316,
        _4248,
        _4286,
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundPowerFlow")


class AGMAGleasonConicalGearSetCompoundPowerFlow(_4222.ConicalGearSetCompoundPowerFlow):
    """AGMAGleasonConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4222.ConicalGearSetCompoundPowerFlow":
            return self._parent._cast(_4222.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4248.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4206.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4252.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4059.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4059.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow(self)
