"""RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6095,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2361
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6064,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation"
)


class RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation(
    _6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2361.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6966.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
