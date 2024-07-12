"""ExternalCADModelCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4489,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ExternalCADModelCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundParametricStudyTool")


class ExternalCADModelCompoundParametricStudyTool(
    _4489.ComponentCompoundParametricStudyTool
):
    """ExternalCADModelCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundParametricStudyTool"
    )

    class _Cast_ExternalCADModelCompoundParametricStudyTool:
        """Special nested class for casting ExternalCADModelCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
            parent: "ExternalCADModelCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
        ) -> "ExternalCADModelCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ExternalCADModelCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6905.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "List[_4376.ExternalCADModelParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ExternalCADModelParametricStudyTool]

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
    ) -> "List[_4376.ExternalCADModelParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ExternalCADModelParametricStudyTool]

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
    ) -> "ExternalCADModelCompoundParametricStudyTool._Cast_ExternalCADModelCompoundParametricStudyTool":
        return self._Cast_ExternalCADModelCompoundParametricStudyTool(self)
