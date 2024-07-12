"""SpiralBevelGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SpiralBevelGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2828
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5705,
        _5734,
        _5776,
        _5795,
        _5736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshHarmonicAnalysis")


class SpiralBevelGearMeshHarmonicAnalysis(_5717.BevelGearMeshHarmonicAnalysis):
    """SpiralBevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshHarmonicAnalysis")

    class _Cast_SpiralBevelGearMeshHarmonicAnalysis:
        """Special nested class for casting SpiralBevelGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
            parent: "SpiralBevelGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5717.BevelGearMeshHarmonicAnalysis":
            return self._parent._cast(_5717.BevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5705.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5734.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(_5734.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5776.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5795.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(
                _5795.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
        ) -> "SpiralBevelGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6976.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

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
    ) -> "_2828.SpiralBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection

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
        "SpiralBevelGearMeshHarmonicAnalysis._Cast_SpiralBevelGearMeshHarmonicAnalysis"
    ):
        return self._Cast_SpiralBevelGearMeshHarmonicAnalysis(self)
