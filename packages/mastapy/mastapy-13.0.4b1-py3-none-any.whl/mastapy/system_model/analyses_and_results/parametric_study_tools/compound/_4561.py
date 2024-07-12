"""ShaftToMountableComponentConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4467,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4432
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4488,
        _4508,
        _4547,
        _4499,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundParametricStudyTool"
)


class ShaftToMountableComponentConnectionCompoundParametricStudyTool(
    _4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
):
    """ShaftToMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
            parent: "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_4499.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_4488.CoaxialConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "_4547.PlanetaryConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4432.ShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4432.ShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool":
        return (
            self._Cast_ShaftToMountableComponentConnectionCompoundParametricStudyTool(
                self
            )
        )
