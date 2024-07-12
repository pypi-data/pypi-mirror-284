"""ZerolBevelGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ZerolBevelGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2574
    from mastapy.system_model.analyses_and_results.power_flows import _4187
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4314,
        _4315,
        _4194,
        _4222,
        _4248,
        _4286,
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundPowerFlow")


class ZerolBevelGearSetCompoundPowerFlow(_4206.BevelGearSetCompoundPowerFlow):
    """ZerolBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundPowerFlow")

    class _Cast_ZerolBevelGearSetCompoundPowerFlow:
        """Special nested class for casting ZerolBevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
            parent: "ZerolBevelGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4206.BevelGearSetCompoundPowerFlow":
            return self._parent._cast(_4206.BevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4222.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4248.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
        ) -> "ZerolBevelGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2574.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2574.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4187.ZerolBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow]

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
    def zerol_bevel_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4314.ZerolBevelGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4315.ZerolBevelGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4187.ZerolBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetCompoundPowerFlow._Cast_ZerolBevelGearSetCompoundPowerFlow":
        return self._Cast_ZerolBevelGearSetCompoundPowerFlow(self)
