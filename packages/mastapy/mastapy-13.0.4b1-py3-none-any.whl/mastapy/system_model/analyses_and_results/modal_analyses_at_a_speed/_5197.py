"""GearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5143,
        _5150,
        _5152,
        _5153,
        _5155,
        _5168,
        _5171,
        _5186,
        _5188,
        _5192,
        _5201,
        _5205,
        _5208,
        _5211,
        _5239,
        _5245,
        _5248,
        _5250,
        _5251,
        _5263,
        _5266,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearModalAnalysisAtASpeed")


class GearModalAnalysisAtASpeed(_5216.MountableComponentModalAnalysisAtASpeed):
    """GearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearModalAnalysisAtASpeed")

    class _Cast_GearModalAnalysisAtASpeed:
        """Special nested class for casting GearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
            parent: "GearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5150.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5152.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(
                _5152.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5153.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(
                _5153.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5155.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.BevelGearModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5168.ConceptGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5171.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.ConicalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5186.CylindricalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(_5186.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5188.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5192.FaceGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.FaceGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5201.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5205.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5208.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5211.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(
                _5211.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5239.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5245.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5245,
            )

            return self._parent._cast(_5245.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5248.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5248,
            )

            return self._parent._cast(_5248.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5250.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(
                _5250.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5251.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5251,
            )

            return self._parent._cast(_5251.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5263.WormGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5263,
            )

            return self._parent._cast(_5263.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "_5266.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5266,
            )

            return self._parent._cast(_5266.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed",
        ) -> "GearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed":
        return self._Cast_GearModalAnalysisAtASpeed(self)
