"""ConnectorCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4541,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConnectorCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4472,
        _4542,
        _4560,
        _4489,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConnectorCompoundParametricStudyTool")


class ConnectorCompoundParametricStudyTool(
    _4541.MountableComponentCompoundParametricStudyTool
):
    """ConnectorCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundParametricStudyTool")

    class _Cast_ConnectorCompoundParametricStudyTool:
        """Special nested class for casting ConnectorCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
            parent: "ConnectorCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4541.MountableComponentCompoundParametricStudyTool":
            return self._parent._cast(
                _4541.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4472.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.BearingCompoundParametricStudyTool)

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4542.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(_4542.OilSealCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "_4560.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(
                _4560.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def connector_compound_parametric_study_tool(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
        ) -> "ConnectorCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConnectorCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4353.ConnectorParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectorParametricStudyTool]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4353.ConnectorParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectorParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundParametricStudyTool._Cast_ConnectorCompoundParametricStudyTool":
        return self._Cast_ConnectorCompoundParametricStudyTool(self)
