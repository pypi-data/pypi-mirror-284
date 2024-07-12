"""CVTPulleyCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4552,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CVTPulleyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6878
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4503,
        _4541,
        _4489,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CVTPulleyCompoundParametricStudyTool")


class CVTPulleyCompoundParametricStudyTool(_4552.PulleyCompoundParametricStudyTool):
    """CVTPulleyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundParametricStudyTool")

    class _Cast_CVTPulleyCompoundParametricStudyTool:
        """Special nested class for casting CVTPulleyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
            parent: "CVTPulleyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def pulley_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_4552.PulleyCompoundParametricStudyTool":
            return self._parent._cast(_4552.PulleyCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_4503.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_4541.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
        ) -> "CVTPulleyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6878.CVTPulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase

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
    ) -> "List[_4359.CVTPulleyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTPulleyParametricStudyTool]

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
    ) -> "List[_4359.CVTPulleyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CVTPulleyParametricStudyTool]

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
    ) -> "CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool":
        return self._Cast_CVTPulleyCompoundParametricStudyTool(self)
