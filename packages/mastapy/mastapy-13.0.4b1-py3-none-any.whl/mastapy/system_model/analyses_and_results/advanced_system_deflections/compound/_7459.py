"""ConicalGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7485,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConicalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _541
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7326,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7431,
        _7438,
        _7441,
        _7442,
        _7443,
        _7489,
        _7493,
        _7496,
        _7499,
        _7526,
        _7532,
        _7535,
        _7538,
        _7539,
        _7553,
        _7504,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearCompoundAdvancedSystemDeflection")


class ConicalGearCompoundAdvancedSystemDeflection(
    _7485.GearCompoundAdvancedSystemDeflection
):
    """ConicalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
            parent: "ConicalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.GearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7485.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7438.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(
                _7438.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7443.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7489.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(_7489.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> (
            "_7493.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7496.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7499.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7526.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7535.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7535,
            )

            return self._parent._cast(
                _7535.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7538.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7538,
            )

            return self._parent._cast(
                _7538.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7539.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7539,
            )

            return self._parent._cast(
                _7539.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7553.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7553,
            )

            return self._parent._cast(
                _7553.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
        ) -> "ConicalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_541.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_duty_cycle_rating(self: Self) -> "_541.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7326.ConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7326.ConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "ConicalGearCompoundAdvancedSystemDeflection._Cast_ConicalGearCompoundAdvancedSystemDeflection":
        return self._Cast_ConicalGearCompoundAdvancedSystemDeflection(self)
