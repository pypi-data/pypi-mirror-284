"""CoaxialConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5365,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5162,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5312,
        _5271,
        _5303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundModalAnalysisAtASpeed")


class CoaxialConnectionCompoundModalAnalysisAtASpeed(
    _5365.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """CoaxialConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CoaxialConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
            parent: "CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5365.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5365.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5312.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CoaxialConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CoaxialConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5162.CoaxialConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CoaxialConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5162.CoaxialConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CoaxialConnectionModalAnalysisAtASpeed]

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
    ) -> "CoaxialConnectionCompoundModalAnalysisAtASpeed._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CoaxialConnectionCompoundModalAnalysisAtASpeed(self)
