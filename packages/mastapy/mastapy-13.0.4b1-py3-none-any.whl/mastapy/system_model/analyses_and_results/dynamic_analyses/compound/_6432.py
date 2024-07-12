"""AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6453,
        _6473,
        _6475,
        _6512,
        _6526,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis"
)


class AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis(
    _6464.ConnectionCompoundDynamicAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6453.CoaxialConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6475.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6512.PlanetaryConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6526.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(
                _6526.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6301.AbstractShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftToMountableComponentConnectionDynamicAnalysis]

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
    ) -> "List[_6301.AbstractShaftToMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftToMountableComponentConnectionDynamicAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis(
            self
        )
