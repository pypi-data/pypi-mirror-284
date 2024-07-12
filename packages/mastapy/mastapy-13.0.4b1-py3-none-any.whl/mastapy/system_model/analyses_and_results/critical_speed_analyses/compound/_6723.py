"""ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6761,
        _6731,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundCriticalSpeedAnalysis")


class ConceptCouplingConnectionCompoundCriticalSpeedAnalysis(
    _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
):
    """ConceptCouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
            parent: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6734.CouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2364.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2364.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

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
    ) -> "List[_6590.ConceptCouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6590.ConceptCouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundCriticalSpeedAnalysis(self)
