"""ConicalGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4322,
        _4329,
        _4331,
        _4332,
        _4334,
        _4387,
        _4391,
        _4394,
        _4397,
        _4435,
        _4441,
        _4444,
        _4446,
        _4447,
        _4462,
        _4402,
        _4342,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearParametricStudyTool")


class ConicalGearParametricStudyTool(_4383.GearParametricStudyTool):
    """ConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearParametricStudyTool")

    class _Cast_ConicalGearParametricStudyTool:
        """Special nested class for casting ConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
            parent: "ConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4383.GearParametricStudyTool":
            return self._parent._cast(_4383.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4402.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4342.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4322.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4329.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4331.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(
                _4331.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4332.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4334.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.BevelGearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4387.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4387,
            )

            return self._parent._cast(_4387.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4391.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4394.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4397.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4435.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4441.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4444.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4446.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4447.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelSunGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "_4462.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4462,
            )

            return self._parent._cast(_4462.ZerolBevelGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
        ) -> "ConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearParametricStudyTool.TYPE"):
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
    def planetaries(self: Self) -> "List[ConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool]

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
    ) -> "ConicalGearParametricStudyTool._Cast_ConicalGearParametricStudyTool":
        return self._Cast_ConicalGearParametricStudyTool(self)
