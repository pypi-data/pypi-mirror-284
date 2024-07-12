"""AGMAGleasonConicalGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4329,
        _4331,
        _4332,
        _4334,
        _4387,
        _4435,
        _4441,
        _4444,
        _4446,
        _4447,
        _4462,
        _4383,
        _4402,
        _4342,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearParametricStudyTool")


class AGMAGleasonConicalGearParametricStudyTool(_4350.ConicalGearParametricStudyTool):
    """AGMAGleasonConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
            parent: "AGMAGleasonConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4350.ConicalGearParametricStudyTool":
            return self._parent._cast(_4350.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4383.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4402.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4342.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4329.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4331.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(
                _4331.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4332.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4334.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.BevelGearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4387.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4387,
            )

            return self._parent._cast(_4387.HypoidGearParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4435.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4441.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4444.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4446.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4447.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelSunGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "_4462.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4462,
            )

            return self._parent._cast(_4462.ZerolBevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "AGMAGleasonConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearParametricStudyTool(self)
