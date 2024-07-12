"""PlanetaryGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PlanetaryGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4140
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4248,
        _4286,
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundPowerFlow")


class PlanetaryGearSetCompoundPowerFlow(_4237.CylindricalGearSetCompoundPowerFlow):
    """PlanetaryGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetCompoundPowerFlow")

    class _Cast_PlanetaryGearSetCompoundPowerFlow:
        """Special nested class for casting PlanetaryGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
            parent: "PlanetaryGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4237.CylindricalGearSetCompoundPowerFlow":
            return self._parent._cast(_4237.CylindricalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4248.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "PlanetaryGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4140.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

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
    def assembly_analysis_cases(self: Self) -> "List[_4140.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

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
    ) -> "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow":
        return self._Cast_PlanetaryGearSetCompoundPowerFlow(self)
