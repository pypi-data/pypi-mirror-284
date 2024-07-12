"""ClutchHalfParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ClutchHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6855
    from mastapy.system_model.analyses_and_results.system_deflections import _2733
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4402,
        _4342,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfParametricStudyTool",)


Self = TypeVar("Self", bound="ClutchHalfParametricStudyTool")


class ClutchHalfParametricStudyTool(_4355.CouplingHalfParametricStudyTool):
    """ClutchHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfParametricStudyTool")

    class _Cast_ClutchHalfParametricStudyTool:
        """Special nested class for casting ClutchHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
            parent: "ClutchHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_4355.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4355.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_4402.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_4342.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_parametric_study_tool(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
        ) -> "ClutchHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6855.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2733.ClutchHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchHalfParametricStudyTool._Cast_ClutchHalfParametricStudyTool":
        return self._Cast_ClutchHalfParametricStudyTool(self)
