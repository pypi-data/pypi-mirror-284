"""SpringDamperConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6669
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6761,
        _6731,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundCriticalSpeedAnalysis")


class SpringDamperConnectionCompoundCriticalSpeedAnalysis(
    _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
):
    """SpringDamperConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
            parent: "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6734.CouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6734.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
        ) -> "SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpringDamperConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2370.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2370.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_6669.SpringDamperConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpringDamperConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6669.SpringDamperConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpringDamperConnectionCriticalSpeedAnalysis]

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
    ) -> "SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis(self)
