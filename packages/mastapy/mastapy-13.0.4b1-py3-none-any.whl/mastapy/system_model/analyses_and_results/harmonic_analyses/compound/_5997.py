"""ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5903
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5829
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5924,
        _5944,
        _5983,
        _5935,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
)


class ShaftToMountableComponentConnectionCompoundHarmonicAnalysis(
    _5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
):
    """ShaftToMountableComponentConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            return self._parent._cast(
                _5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5924.CoaxialConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "_5983.PlanetaryConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5829.ShaftToMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis]

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
    ) -> "List[_5829.ShaftToMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysis(
            self
        )
