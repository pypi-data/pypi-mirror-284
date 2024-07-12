"""CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5033,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4922,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5106,
        _5012,
        _5044,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(
    _5033.CoaxialConnectionCompoundModalAnalysisAtAStiffness
):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5033.CoaxialConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5033.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5106.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4922.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4922.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
