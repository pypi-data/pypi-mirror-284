"""AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7197,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7030,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7186,
        _7206,
        _7208,
        _7245,
        _7259,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7030.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7030.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
