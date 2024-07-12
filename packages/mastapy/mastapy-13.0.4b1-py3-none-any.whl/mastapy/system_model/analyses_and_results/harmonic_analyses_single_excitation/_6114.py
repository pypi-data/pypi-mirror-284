"""PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6128,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6032,
        _6064,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetaryConnectionHarmonicAnalysisOfSingleExcitation")


class PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(
    _6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(self)
