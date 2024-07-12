"""StraightBevelGearSetCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5027,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4990,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5117,
        _5118,
        _5015,
        _5043,
        _5069,
        _5107,
        _5009,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelGearSetCompoundModalAnalysisAtAStiffness")


class StraightBevelGearSetCompoundModalAnalysisAtAStiffness(
    _5027.BevelGearSetCompoundModalAnalysisAtAStiffness
):
    """StraightBevelGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
            parent: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.BevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5027.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5107.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2568.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

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
    ) -> "List[_4990.StraightBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearSetModalAnalysisAtAStiffness]

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
    def straight_bevel_gears_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5117.StraightBevelGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.StraightBevelGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5118.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4990.StraightBevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearSetModalAnalysisAtAStiffness]

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
    ) -> "StraightBevelGearSetCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelGearSetCompoundModalAnalysisAtAStiffness(self)
