"""FaceGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4522,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "FaceGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6906
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4541,
        _4489,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="FaceGearCompoundParametricStudyTool")


class FaceGearCompoundParametricStudyTool(_4522.GearCompoundParametricStudyTool):
    """FaceGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearCompoundParametricStudyTool")

    class _Cast_FaceGearCompoundParametricStudyTool:
        """Special nested class for casting FaceGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
            parent: "FaceGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_compound_parametric_study_tool(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_4522.GearCompoundParametricStudyTool":
            return self._parent._cast(_4522.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_4541.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
        ) -> "FaceGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "FaceGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6906.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4378.FaceGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4378.FaceGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "FaceGearCompoundParametricStudyTool._Cast_FaceGearCompoundParametricStudyTool"
    ):
        return self._Cast_FaceGearCompoundParametricStudyTool(self)
