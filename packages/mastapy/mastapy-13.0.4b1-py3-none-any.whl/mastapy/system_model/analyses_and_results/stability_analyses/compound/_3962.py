"""CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3829
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4015,
        _3921,
        _3953,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis(
    _3942.CoaxialConnectionCompoundStabilityAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_3942.CoaxialConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3942.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3921.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(
                _3921.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3829.CycloidalDiscCentralBearingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CycloidalDiscCentralBearingConnectionStabilityAnalysis]

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
    ) -> "List[_3829.CycloidalDiscCentralBearingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CycloidalDiscCentralBearingConnectionStabilityAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis(
                self
            )
        )
