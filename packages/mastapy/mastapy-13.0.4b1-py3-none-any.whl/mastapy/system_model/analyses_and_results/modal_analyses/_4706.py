"""SpiralBevelGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpiralBevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2564
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.system_deflections import _2829
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4705,
        _4704,
        _4599,
        _4627,
        _4658,
        _4703,
        _4593,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetModalAnalysis")


class SpiralBevelGearSetModalAnalysis(_4611.BevelGearSetModalAnalysis):
    """SpiralBevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetModalAnalysis")

    class _Cast_SpiralBevelGearSetModalAnalysis:
        """Special nested class for casting SpiralBevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
            parent: "SpiralBevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4611.BevelGearSetModalAnalysis":
            return self._parent._cast(_4611.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4599.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4627.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4658.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
        ) -> "SpiralBevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2564.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6977.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2829.SpiralBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears_modal_analysis(
        self: Self,
    ) -> "List[_4705.SpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4704.SpiralBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetModalAnalysis._Cast_SpiralBevelGearSetModalAnalysis":
        return self._Cast_SpiralBevelGearSetModalAnalysis(self)
