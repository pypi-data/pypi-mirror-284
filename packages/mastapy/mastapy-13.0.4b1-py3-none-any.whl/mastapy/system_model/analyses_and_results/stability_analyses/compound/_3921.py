"""AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3787
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3942,
        _3962,
        _3964,
        _4001,
        _4015,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
)


class AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis(
    _3953.ConnectionCompoundStabilityAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3942.CoaxialConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3962.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3964.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4001.PlanetaryConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "List[_3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis(
            self
        )
