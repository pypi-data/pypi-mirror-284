"""AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6064,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2285
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6053,
        _6073,
        _6075,
        _6114,
        _6128,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


class AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6064.ConnectionHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6064.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6053.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6073.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6114.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2285.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
