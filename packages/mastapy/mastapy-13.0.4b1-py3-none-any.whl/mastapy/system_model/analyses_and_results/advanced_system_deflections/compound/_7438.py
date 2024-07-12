"""BevelDifferentialGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7443,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7305,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7441,
        _7442,
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
__all__ = ("BevelDifferentialGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundAdvancedSystemDeflection")


class BevelDifferentialGearCompoundAdvancedSystemDeflection(
    _7443.BevelGearCompoundAdvancedSystemDeflection
):
    """BevelDifferentialGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
            parent: "BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7443.BevelGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7443.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7459.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "BevelDifferentialGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7305.BevelDifferentialGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearAdvancedSystemDeflection]

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
    ) -> "List[_7305.BevelDifferentialGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearAdvancedSystemDeflection]

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
    ) -> "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection(self)
