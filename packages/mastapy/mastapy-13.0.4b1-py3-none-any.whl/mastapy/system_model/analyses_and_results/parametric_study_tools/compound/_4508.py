"""CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4488,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4561,
        _4467,
        _4499,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"
)


class CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
    _4488.CoaxialConnectionCompoundParametricStudyTool
):
    """CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
            parent: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4488.CoaxialConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4488.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_4499.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4361.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4361.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
                self
            )
        )
