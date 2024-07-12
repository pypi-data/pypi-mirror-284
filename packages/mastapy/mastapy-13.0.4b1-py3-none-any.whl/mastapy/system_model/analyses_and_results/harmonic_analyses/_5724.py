"""CoaxialConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CoaxialConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.system_deflections import _2735
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5745,
        _5703,
        _5736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionHarmonicAnalysis")


class CoaxialConnectionHarmonicAnalysis(
    _5829.ShaftToMountableComponentConnectionHarmonicAnalysis
):
    """CoaxialConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionHarmonicAnalysis")

    class _Cast_CoaxialConnectionHarmonicAnalysis:
        """Special nested class for casting CoaxialConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
            parent: "CoaxialConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_5829.ShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5829.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(
                _5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "_5745.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(
                _5745.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def coaxial_connection_harmonic_analysis(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
        ) -> "CoaxialConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6858.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "_2735.CoaxialConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection

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
    ) -> "CoaxialConnectionHarmonicAnalysis._Cast_CoaxialConnectionHarmonicAnalysis":
        return self._Cast_CoaxialConnectionHarmonicAnalysis(self)
