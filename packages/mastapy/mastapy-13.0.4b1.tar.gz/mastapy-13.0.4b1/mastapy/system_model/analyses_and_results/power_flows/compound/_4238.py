"""CylindricalPlanetGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CylindricalPlanetGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4104
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4246,
        _4265,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundPowerFlow")


class CylindricalPlanetGearCompoundPowerFlow(_4235.CylindricalGearCompoundPowerFlow):
    """CylindricalPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundPowerFlow"
    )

    class _Cast_CylindricalPlanetGearCompoundPowerFlow:
        """Special nested class for casting CylindricalPlanetGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
            parent: "CylindricalPlanetGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_4235.CylindricalGearCompoundPowerFlow":
            return self._parent._cast(_4235.CylindricalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_4246.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
        ) -> "CylindricalPlanetGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4104.CylindricalPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4104.CylindricalPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearCompoundPowerFlow._Cast_CylindricalPlanetGearCompoundPowerFlow":
        return self._Cast_CylindricalPlanetGearCompoundPowerFlow(self)
