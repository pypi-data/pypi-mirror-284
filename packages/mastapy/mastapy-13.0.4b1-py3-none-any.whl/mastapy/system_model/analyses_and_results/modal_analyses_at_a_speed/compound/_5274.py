"""AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5302,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5281,
        _5286,
        _5332,
        _5369,
        _5375,
        _5378,
        _5396,
        _5328,
        _5366,
        _5268,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed(
    _5302.ConicalGearSetCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5302.ConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5302.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5268.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5281.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5286.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5332.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5375.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5378.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(
                _5378.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5396.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5396,
            )

            return self._parent._cast(
                _5396.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5144.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]

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
    ) -> "List[_5144.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]

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
    ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed(self)
