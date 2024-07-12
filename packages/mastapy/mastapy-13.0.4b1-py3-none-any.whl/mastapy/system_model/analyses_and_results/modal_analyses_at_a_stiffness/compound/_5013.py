"""AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4883,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5020,
        _5023,
        _5024,
        _5025,
        _5071,
        _5108,
        _5114,
        _5117,
        _5120,
        _5121,
        _5135,
        _5067,
        _5086,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness")


class AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness(
    _5041.ConicalGearCompoundModalAnalysisAtAStiffness
):
    """AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
            parent: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.ConicalGearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5041.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5108.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5114.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5117.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5120.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5120,
            )

            return self._parent._cast(
                _5120.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5121.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5121,
            )

            return self._parent._cast(
                _5121.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5135.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5135,
            )

            return self._parent._cast(
                _5135.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
        ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AGMAGleasonConicalGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AGMAGleasonConicalGearModalAnalysisAtAStiffness]

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
    ) -> "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness(self)
