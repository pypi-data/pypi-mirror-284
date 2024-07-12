"""BeltConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5965
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BeltConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5709
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5940,
        _5935,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCompoundHarmonicAnalysis")


class BeltConnectionCompoundHarmonicAnalysis(
    _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
):
    """BeltConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_BeltConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting BeltConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
            parent: "BeltConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "_5940.CVTBeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
        ) -> "BeltConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2288.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2288.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5709.BeltConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5709.BeltConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundHarmonicAnalysis._Cast_BeltConnectionCompoundHarmonicAnalysis":
        return self._Cast_BeltConnectionCompoundHarmonicAnalysis(self)
