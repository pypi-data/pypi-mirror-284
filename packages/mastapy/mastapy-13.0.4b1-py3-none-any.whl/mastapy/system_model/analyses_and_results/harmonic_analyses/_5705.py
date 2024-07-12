"""AGMAGleasonConicalGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.system_deflections import _2710
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5712,
        _5717,
        _5793,
        _5834,
        _5841,
        _5844,
        _5863,
        _5776,
        _5795,
        _5736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshHarmonicAnalysis")


class AGMAGleasonConicalGearMeshHarmonicAnalysis(_5734.ConicalGearMeshHarmonicAnalysis):
    """AGMAGleasonConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5734.ConicalGearMeshHarmonicAnalysis":
            return self._parent._cast(_5734.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5776.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5795.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(
                _5795.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5736.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(_5736.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5712.BevelDifferentialGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5717.BevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5793.HypoidGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.HypoidGearMeshHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5834.SpiralBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5841.StraightBevelDiffGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5841,
            )

            return self._parent._cast(_5841.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5844.StraightBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "_5863.ZerolBevelGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5863,
            )

            return self._parent._cast(_5863.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "_2710.AGMAGleasonConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection

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
    ) -> "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis(self)
