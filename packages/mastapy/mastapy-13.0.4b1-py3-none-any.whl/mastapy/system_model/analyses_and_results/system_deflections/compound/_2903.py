"""ConceptGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConceptGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.system_deflections import _2742
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2901,
        _2902,
        _2972,
        _2872,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundSystemDeflection")


class ConceptGearSetCompoundSystemDeflection(_2933.GearSetCompoundSystemDeflection):
    """ConceptGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundSystemDeflection"
    )

    class _Cast_ConceptGearSetCompoundSystemDeflection:
        """Special nested class for casting ConceptGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
            parent: "ConceptGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_system_deflection(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_2933.GearSetCompoundSystemDeflection":
            return self._parent._cast(_2933.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_2972.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_2872.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
        ) -> "ConceptGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptGearSetCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2542.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_2742.ConceptGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection]

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
    def concept_gears_compound_system_deflection(
        self: Self,
    ) -> "List[_2901.ConceptGearCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_system_deflection(
        self: Self,
    ) -> "List[_2902.ConceptGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearMeshCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2742.ConceptGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection]

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
    ) -> "ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection":
        return self._Cast_ConceptGearSetCompoundSystemDeflection(self)
