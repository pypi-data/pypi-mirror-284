"""BevelGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7433,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7312,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7440,
        _7528,
        _7534,
        _7537,
        _7555,
        _7461,
        _7487,
        _7525,
        _7427,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSetCompoundAdvancedSystemDeflection")


class BevelGearSetCompoundAdvancedSystemDeflection(
    _7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
):
    """BevelGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
            parent: "BevelGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7461.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(
                _7461.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7487.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7427.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7440.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7528.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7534.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7537.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7537,
            )

            return self._parent._cast(
                _7537.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7555.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7555,
            )

            return self._parent._cast(
                _7555.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "BevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7312.BevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7312.BevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearSetAdvancedSystemDeflection]

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
    ) -> "BevelGearSetCompoundAdvancedSystemDeflection._Cast_BevelGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_BevelGearSetCompoundAdvancedSystemDeflection(self)
