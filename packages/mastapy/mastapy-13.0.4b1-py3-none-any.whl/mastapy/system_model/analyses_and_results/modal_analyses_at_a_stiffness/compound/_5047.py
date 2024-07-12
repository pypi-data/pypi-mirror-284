"""CouplingConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5074,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4915,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5031,
        _5036,
        _5090,
        _5112,
        _5127,
        _5044,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundModalAnalysisAtAStiffness")


class CouplingConnectionCompoundModalAnalysisAtAStiffness(
    _5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """CouplingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5074.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ClutchConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.SpringDamperConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5127.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5127,
            )

            return self._parent._cast(
                _5127.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CouplingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4915.CouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4915.CouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "CouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CouplingConnectionCompoundModalAnalysisAtAStiffness(self)
