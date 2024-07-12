"""ZerolBevelGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7445,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2574
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7426,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7553,
        _7554,
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
__all__ = ("ZerolBevelGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundAdvancedSystemDeflection")


class ZerolBevelGearSetCompoundAdvancedSystemDeflection(
    _7445.BevelGearSetCompoundAdvancedSystemDeflection
):
    """ZerolBevelGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
            parent: "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7445.BevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7445.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7461.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(
                _7461.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7487.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7427.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
        ) -> "ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundAdvancedSystemDeflection.TYPE",
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
    ) -> "List[_7426.ZerolBevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearSetAdvancedSystemDeflection]

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
    def zerol_bevel_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7553.ZerolBevelGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7554.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7426.ZerolBevelGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearSetAdvancedSystemDeflection]

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
    ) -> "ZerolBevelGearSetCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_ZerolBevelGearSetCompoundAdvancedSystemDeflection(self)
