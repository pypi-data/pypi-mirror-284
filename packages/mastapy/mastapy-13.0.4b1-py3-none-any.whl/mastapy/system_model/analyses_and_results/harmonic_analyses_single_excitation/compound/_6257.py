"""ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6163,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6128,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6184,
        _6204,
        _6243,
        _6195,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6163.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6163.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6184.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6204.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6243.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6128.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
