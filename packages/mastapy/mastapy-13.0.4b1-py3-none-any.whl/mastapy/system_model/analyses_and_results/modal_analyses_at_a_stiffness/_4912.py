"""ConicalGearSetModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4939,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConicalGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4884,
        _4891,
        _4896,
        _4943,
        _4947,
        _4950,
        _4953,
        _4981,
        _4987,
        _4990,
        _5008,
        _4978,
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConicalGearSetModalAnalysisAtAStiffness")


class ConicalGearSetModalAnalysisAtAStiffness(_4939.GearSetModalAnalysisAtAStiffness):
    """ConicalGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_ConicalGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting ConicalGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
            parent: "ConicalGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4939.GearSetModalAnalysisAtAStiffness":
            return self._parent._cast(_4939.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4884.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(
                _4884.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4891.BevelDifferentialGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(
                _4891.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4896.BevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4943.HypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4947.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(
                _4947.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4950.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(
                _4950.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> (
            "_4953.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4981.SpiralBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(_4981.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4987.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4987,
            )

            return self._parent._cast(
                _4987.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_4990.StraightBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4990,
            )

            return self._parent._cast(
                _4990.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "_5008.ZerolBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5008,
            )

            return self._parent._cast(_5008.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
        ) -> "ConicalGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConicalGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetModalAnalysisAtAStiffness._Cast_ConicalGearSetModalAnalysisAtAStiffness":
        return self._Cast_ConicalGearSetModalAnalysisAtAStiffness(self)
