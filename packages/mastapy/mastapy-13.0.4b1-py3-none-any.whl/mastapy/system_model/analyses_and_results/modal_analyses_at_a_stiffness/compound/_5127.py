"""TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5047,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2372
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4997,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5074,
        _5044,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"
)


class TorqueConverterConnectionCompoundModalAnalysisAtAStiffness(
    _5047.CouplingConnectionCompoundModalAnalysisAtAStiffness
):
    """TorqueConverterConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
            parent: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5047.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_4997.TorqueConverterConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.TorqueConverterConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4997.TorqueConverterConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.TorqueConverterConnectionModalAnalysisAtAStiffness]

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
    ) -> "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
