"""StraightBevelPlanetGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7532,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7408,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7443,
        _7431,
        _7459,
        _7485,
        _7504,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundAdvancedSystemDeflection")


class StraightBevelPlanetGearCompoundAdvancedSystemDeflection(
    _7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection
):
    """StraightBevelPlanetGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelPlanetGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
            parent: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7443.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7459.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "StraightBevelPlanetGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7408.StraightBevelPlanetGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelPlanetGearAdvancedSystemDeflection]

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
    ) -> "List[_7408.StraightBevelPlanetGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelPlanetGearAdvancedSystemDeflection]

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
    ) -> "StraightBevelPlanetGearCompoundAdvancedSystemDeflection._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelPlanetGearCompoundAdvancedSystemDeflection(self)
