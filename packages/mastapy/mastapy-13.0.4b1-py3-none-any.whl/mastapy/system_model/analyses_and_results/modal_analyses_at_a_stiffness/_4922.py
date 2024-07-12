"""CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4902,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2355
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4977,
        _4881,
        _4913,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness"
)


class CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness(
    _4902.CoaxialConnectionModalAnalysisAtAStiffness
):
    """CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
            parent: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4902.CoaxialConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4902.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4977.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(
                _4977.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4881.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(
                _4881.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4913.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness(
                self
            )
        )
