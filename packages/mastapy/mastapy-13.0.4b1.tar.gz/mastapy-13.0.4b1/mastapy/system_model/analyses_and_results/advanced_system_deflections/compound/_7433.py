"""AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7461,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7300,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7440,
        _7445,
        _7491,
        _7528,
        _7534,
        _7537,
        _7555,
        _7487,
        _7525,
        _7427,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"
)


class AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
    _7461.ConicalGearSetCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7461.ConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7461.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7487.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7427.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7440.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7445.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7491.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7528.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7534.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7537.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7537,
            )

            return self._parent._cast(
                _7537.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7555.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7555,
            )

            return self._parent._cast(
                _7555.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
            self
        )
