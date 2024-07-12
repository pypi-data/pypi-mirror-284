"""BevelGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.system_deflections import _2729
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4605,
        _4607,
        _4608,
        _4705,
        _4711,
        _4714,
        _4716,
        _4717,
        _4735,
        _4626,
        _4657,
        _4679,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearModalAnalysis")


class BevelGearModalAnalysis(_4598.AGMAGleasonConicalGearModalAnalysis):
    """BevelGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearModalAnalysis")

    class _Cast_BevelGearModalAnalysis:
        """Special nested class for casting BevelGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
            parent: "BevelGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4598.AGMAGleasonConicalGearModalAnalysis":
            return self._parent._cast(_4598.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4626.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4657.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4605.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4607.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4608.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialSunGearModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4705.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4711.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4714.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4716.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4717.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelSunGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "_4735.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.ZerolBevelGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis",
        ) -> "BevelGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2729.BevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearModalAnalysis._Cast_BevelGearModalAnalysis":
        return self._Cast_BevelGearModalAnalysis(self)
