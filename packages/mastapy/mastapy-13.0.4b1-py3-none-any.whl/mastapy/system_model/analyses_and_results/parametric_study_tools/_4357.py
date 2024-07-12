"""CVTBeltConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4326
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CVTBeltConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="CVTBeltConnectionParametricStudyTool")


class CVTBeltConnectionParametricStudyTool(_4326.BeltConnectionParametricStudyTool):
    """CVTBeltConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionParametricStudyTool")

    class _Cast_CVTBeltConnectionParametricStudyTool:
        """Special nested class for casting CVTBeltConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
            parent: "CVTBeltConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def belt_connection_parametric_study_tool(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_4326.BeltConnectionParametricStudyTool":
            return self._parent._cast(_4326.BeltConnectionParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
        ) -> "CVTBeltConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool":
        return self._Cast_CVTBeltConnectionParametricStudyTool(self)
