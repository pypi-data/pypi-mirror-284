"""StraightBevelSunGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5245
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2570
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5155,
        _5143,
        _5171,
        _5197,
        _5216,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelSunGearModalAnalysisAtASpeed")


class StraightBevelSunGearModalAnalysisAtASpeed(
    _5245.StraightBevelDiffGearModalAnalysisAtASpeed
):
    """StraightBevelSunGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelSunGearModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelSunGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
            parent: "StraightBevelSunGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5245.StraightBevelDiffGearModalAnalysisAtASpeed":
            return self._parent._cast(_5245.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5155.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5171.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5197.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "StraightBevelSunGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed":
        return self._Cast_StraightBevelSunGearModalAnalysisAtASpeed(self)
