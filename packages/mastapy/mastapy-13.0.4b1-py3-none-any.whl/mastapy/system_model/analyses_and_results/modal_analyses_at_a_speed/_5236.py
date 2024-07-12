"""ShaftToMountableComponentConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5162,
        _5182,
        _5222,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionModalAnalysisAtASpeed")


class ShaftToMountableComponentConnectionModalAnalysisAtASpeed(
    _5141.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
):
    """ShaftToMountableComponentConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    )

    class _Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed:
        """Special nested class for casting ShaftToMountableComponentConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
            parent: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5141.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5141.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5162.CoaxialConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5182.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5222.PlanetaryConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(_5222.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionModalAnalysisAtASpeed.TYPE",
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
    ) -> "ShaftToMountableComponentConnectionModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
        return self._Cast_ShaftToMountableComponentConnectionModalAnalysisAtASpeed(self)
