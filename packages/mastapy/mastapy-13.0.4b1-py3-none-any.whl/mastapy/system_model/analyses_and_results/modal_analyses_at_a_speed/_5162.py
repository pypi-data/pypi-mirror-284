"""CoaxialConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5182,
        _5141,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CoaxialConnectionModalAnalysisAtASpeed")


class CoaxialConnectionModalAnalysisAtASpeed(
    _5236.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
):
    """CoaxialConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionModalAnalysisAtASpeed"
    )

    class _Cast_CoaxialConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
            parent: "CoaxialConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5236.ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5236.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5141.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(
                _5141.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5182.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "CoaxialConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CoaxialConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6858.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed":
        return self._Cast_CoaxialConnectionModalAnalysisAtASpeed(self)
