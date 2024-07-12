"""StraightBevelSunGearModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4986,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelSunGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2570
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4895,
        _4883,
        _4911,
        _4938,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelSunGearModalAnalysisAtAStiffness")


class StraightBevelSunGearModalAnalysisAtAStiffness(
    _4986.StraightBevelDiffGearModalAnalysisAtAStiffness
):
    """StraightBevelSunGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelSunGearModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelSunGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
            parent: "StraightBevelSunGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4986.StraightBevelDiffGearModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4986.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4895.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(
                _4883.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4911.ConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(_4911.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4938.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
        ) -> "StraightBevelSunGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelSunGearModalAnalysisAtAStiffness.TYPE",
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
    ) -> "StraightBevelSunGearModalAnalysisAtAStiffness._Cast_StraightBevelSunGearModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelSunGearModalAnalysisAtAStiffness(self)
