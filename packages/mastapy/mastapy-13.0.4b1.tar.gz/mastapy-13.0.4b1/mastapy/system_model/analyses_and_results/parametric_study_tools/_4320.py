"""AbstractShaftToMountableComponentConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
        "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2285
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4341,
        _4361,
        _4363,
        _4418,
        _4432,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionParametricStudyTool",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionParametricStudyTool"
)


class AbstractShaftToMountableComponentConnectionParametricStudyTool(
    _4352.ConnectionParametricStudyTool
):
    """AbstractShaftToMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
            parent: "AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4341.CoaxialConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CoaxialConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4361.CycloidalDiscCentralBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(
                _4361.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4363.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(
                _4363.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4418.PlanetaryConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.PlanetaryConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "_4432.ShaftToMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(
                _4432.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "AbstractShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2285.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionParametricStudyTool(
                self
            )
        )
