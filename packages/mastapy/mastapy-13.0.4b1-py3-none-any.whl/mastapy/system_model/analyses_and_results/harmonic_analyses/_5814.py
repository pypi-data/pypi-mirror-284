"""PlanetaryConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PlanetaryConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2810
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5703, _5736
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionHarmonicAnalysis")


class PlanetaryConnectionHarmonicAnalysis(
    _5829.ShaftToMountableComponentConnectionHarmonicAnalysis
):
    """PlanetaryConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionHarmonicAnalysis")

    class _Cast_PlanetaryConnectionHarmonicAnalysis:
        """Special nested class for casting PlanetaryConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
            parent: "PlanetaryConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5829.ShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5829.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(
                _5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "PlanetaryConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6954.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2810.PlanetaryConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis"
    ):
        return self._Cast_PlanetaryConnectionHarmonicAnalysis(self)
