"""HypoidGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5905
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "HypoidGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5933,
        _5959,
        _5965,
        _5935,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundHarmonicAnalysis")


class HypoidGearMeshCompoundHarmonicAnalysis(
    _5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
):
    """HypoidGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_HypoidGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting HypoidGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
            parent: "HypoidGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5933.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5959.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "HypoidGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_5793.HypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis]

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
    ) -> "List[_5793.HypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis]

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
    ) -> "HypoidGearMeshCompoundHarmonicAnalysis._Cast_HypoidGearMeshCompoundHarmonicAnalysis":
        return self._Cast_HypoidGearMeshCompoundHarmonicAnalysis(self)
