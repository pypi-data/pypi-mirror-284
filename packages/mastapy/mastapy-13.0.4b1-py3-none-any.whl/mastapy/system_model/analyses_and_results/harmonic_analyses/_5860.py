"""WormGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "WormGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _7005
    from mastapy.system_model.analyses_and_results.system_deflections import _2857
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5795, _5736
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshHarmonicAnalysis")


class WormGearMeshHarmonicAnalysis(_5776.GearMeshHarmonicAnalysis):
    """WormGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshHarmonicAnalysis")

    class _Cast_WormGearMeshHarmonicAnalysis:
        """Special nested class for casting WormGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
            parent: "WormGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_5776.GearMeshHarmonicAnalysis":
            return self._parent._cast(_5776.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_5795.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(
                _5795.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
        ) -> "WormGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2349.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7005.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2857.WormGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection

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
    ) -> "WormGearMeshHarmonicAnalysis._Cast_WormGearMeshHarmonicAnalysis":
        return self._Cast_WormGearMeshHarmonicAnalysis(self)
