"""ConceptGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4658
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConceptGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6865
    from mastapy.system_model.analyses_and_results.system_deflections import _2742
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4623,
        _4622,
        _4703,
        _4593,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetModalAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetModalAnalysis")


class ConceptGearSetModalAnalysis(_4658.GearSetModalAnalysis):
    """ConceptGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetModalAnalysis")

    class _Cast_ConceptGearSetModalAnalysis:
        """Special nested class for casting ConceptGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
            parent: "ConceptGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_4658.GearSetModalAnalysis":
            return self._parent._cast(_4658.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "ConceptGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6865.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2742.ConceptGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_modal_analysis(
        self: Self,
    ) -> "List[_4623.ConceptGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4622.ConceptGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis":
        return self._Cast_ConceptGearSetModalAnalysis(self)
