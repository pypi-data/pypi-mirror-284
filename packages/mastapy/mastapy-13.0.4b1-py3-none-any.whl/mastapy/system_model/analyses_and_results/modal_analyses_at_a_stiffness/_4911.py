"""ConicalGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4938,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConicalGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4883,
        _4890,
        _4892,
        _4893,
        _4895,
        _4942,
        _4946,
        _4949,
        _4952,
        _4980,
        _4986,
        _4989,
        _4991,
        _4992,
        _5007,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConicalGearModalAnalysisAtAStiffness")


class ConicalGearModalAnalysisAtAStiffness(_4938.GearModalAnalysisAtAStiffness):
    """ConicalGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearModalAnalysisAtAStiffness")

    class _Cast_ConicalGearModalAnalysisAtAStiffness:
        """Special nested class for casting ConicalGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
            parent: "ConicalGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4938.GearModalAnalysisAtAStiffness":
            return self._parent._cast(_4938.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(
                _4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4890.BevelDifferentialGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(
                _4890.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(
                _4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4893.BevelDifferentialSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(
                _4893.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4895.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.BevelGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4942.HypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.HypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4946.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4949.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4952.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(
                _4952.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4980.SpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4986.StraightBevelDiffGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4986,
            )

            return self._parent._cast(
                _4986.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4989.StraightBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4989,
            )

            return self._parent._cast(_4989.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4991.StraightBevelPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4991,
            )

            return self._parent._cast(
                _4991.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_4992.StraightBevelSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(
                _4992.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "_5007.ZerolBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5007,
            )

            return self._parent._cast(_5007.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
        ) -> "ConicalGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConicalGearModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearModalAnalysisAtAStiffness._Cast_ConicalGearModalAnalysisAtAStiffness":
        return self._Cast_ConicalGearModalAnalysisAtAStiffness(self)
