"""BevelDifferentialGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.system_deflections import _2722
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
__all__ = ("BevelDifferentialGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshHarmonicAnalysis")


class BevelDifferentialGearMeshHarmonicAnalysis(_5717.BevelGearMeshHarmonicAnalysis):
    """BevelDifferentialGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
            parent: "BevelDifferentialGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5717.BevelGearMeshHarmonicAnalysis":
            return self._parent._cast(_5717.BevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5705.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5734.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(_5734.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5776.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5795.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(
                _5795.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
        ) -> "BevelDifferentialGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6845.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "_2722.BevelDifferentialGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection

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
    ) -> "BevelDifferentialGearMeshHarmonicAnalysis._Cast_BevelDifferentialGearMeshHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearMeshHarmonicAnalysis(self)
