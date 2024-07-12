"""ShaftToMountableComponentConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ShaftToMountableComponentConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4341,
        _4361,
        _4418,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionParametricStudyTool")


class ShaftToMountableComponentConnectionParametricStudyTool(
    _4320.AbstractShaftToMountableComponentConnectionParametricStudyTool
):
    """ShaftToMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionParametricStudyTool",
    )

    class _Cast_ShaftToMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting ShaftToMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
            parent: "ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4320.AbstractShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4320.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4341.CoaxialConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CoaxialConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4361.CycloidalDiscCentralBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(
                _4361.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4418.PlanetaryConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.PlanetaryConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "ShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool":
        return self._Cast_ShaftToMountableComponentConnectionParametricStudyTool(self)
