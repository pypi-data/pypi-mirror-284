"""AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5300,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5143,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5279,
        _5282,
        _5283,
        _5284,
        _5330,
        _5367,
        _5373,
        _5376,
        _5379,
        _5380,
        _5394,
        _5326,
        _5345,
        _5293,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed(
    _5300.ConicalGearCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5300.ConicalGearCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5300.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5326.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5279.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(
                _5279.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5282.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5283.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(
                _5283.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5284.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5330.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5367.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5373.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(
                _5373.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5376.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5376,
            )

            return self._parent._cast(
                _5376.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5379.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5379,
            )

            return self._parent._cast(
                _5379.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5380.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5380,
            )

            return self._parent._cast(
                _5380.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "_5394.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5394,
            )

            return self._parent._cast(_5394.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearModalAnalysisAtASpeed]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed(self)
