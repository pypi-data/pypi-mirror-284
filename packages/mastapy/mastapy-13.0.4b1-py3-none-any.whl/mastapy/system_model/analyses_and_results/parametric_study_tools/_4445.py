"""StraightBevelGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "StraightBevelGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6986
    from mastapy.system_model.analyses_and_results.system_deflections import _2838
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4444,
        _4443,
        _4323,
        _4351,
        _4384,
        _4433,
        _4317,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelGearSetParametricStudyTool")


class StraightBevelGearSetParametricStudyTool(_4335.BevelGearSetParametricStudyTool):
    """StraightBevelGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetParametricStudyTool"
    )

    class _Cast_StraightBevelGearSetParametricStudyTool:
        """Special nested class for casting StraightBevelGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
            parent: "StraightBevelGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4335.BevelGearSetParametricStudyTool":
            return self._parent._cast(_4335.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4323.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(
                _4323.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4351.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4351,
            )

            return self._parent._cast(_4351.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4384.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
        ) -> "StraightBevelGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "StraightBevelGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2568.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6986.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2838.StraightBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4444.StraightBevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4443.StraightBevelGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetParametricStudyTool._Cast_StraightBevelGearSetParametricStudyTool":
        return self._Cast_StraightBevelGearSetParametricStudyTool(self)
