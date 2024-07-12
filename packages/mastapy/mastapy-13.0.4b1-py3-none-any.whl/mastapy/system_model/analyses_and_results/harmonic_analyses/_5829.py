"""ShaftToMountableComponentConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.system_deflections import _2826
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5724,
        _5745,
        _5814,
        _5736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionHarmonicAnalysis")


class ShaftToMountableComponentConnectionHarmonicAnalysis(
    _5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
):
    """ShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionHarmonicAnalysis"
    )

    class _Cast_ShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
            parent: "ShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5703.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5724.CoaxialConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5745.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(
                _5745.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5814.PlanetaryConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "ShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2826.ShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection

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
    ) -> "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis(self)
