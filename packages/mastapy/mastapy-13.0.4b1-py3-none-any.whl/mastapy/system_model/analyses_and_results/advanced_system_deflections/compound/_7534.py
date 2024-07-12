"""StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7445,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7404,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7532,
        _7533,
        _7433,
        _7461,
        _7487,
        _7525,
        _7427,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundAdvancedSystemDeflection")


class StraightBevelDiffGearSetCompoundAdvancedSystemDeflection(
    _7445.BevelGearSetCompoundAdvancedSystemDeflection
):
    """StraightBevelDiffGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
            parent: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7445.BevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7445.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7461.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(
                _7461.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7487.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7427.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2566.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_7404.StraightBevelDiffGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearSetAdvancedSystemDeflection]

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
    def straight_bevel_diff_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7533.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7404.StraightBevelDiffGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearSetAdvancedSystemDeflection]

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
    ) -> "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelDiffGearSetCompoundAdvancedSystemDeflection(self)
