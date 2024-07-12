"""ConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5903,
        _5905,
        _5909,
        _5912,
        _5917,
        _5922,
        _5924,
        _5927,
        _5930,
        _5933,
        _5938,
        _5940,
        _5944,
        _5946,
        _5948,
        _5954,
        _5959,
        _5963,
        _5965,
        _5967,
        _5970,
        _5973,
        _5981,
        _5983,
        _5990,
        _5993,
        _5997,
        _6000,
        _6003,
        _6006,
        _6009,
        _6018,
        _6024,
        _6027,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundHarmonicAnalysis")


class ConnectionCompoundHarmonicAnalysis(_7560.ConnectionCompoundAnalysis):
    """ConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundHarmonicAnalysis")

    class _Cast_ConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
            parent: "ConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(
                _5903.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(
                _5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5909.BeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(
                _5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5917.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5922.ClutchConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5924.CoaxialConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5927.ConceptCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(
                _5927.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5930.ConceptGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5933.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5938.CouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5940.CVTBeltConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5946.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5948.CylindricalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(_5948.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5954.FaceGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5959.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5963.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(
                _5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(
                _5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(
                _5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5981.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5983.PlanetaryConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5990.RingPinsToDiscConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5993.RollingRingConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_5997.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(
                _5997.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6003.SpringDamperConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(
                _6003.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(
                _6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6009.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(
                _6009.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6018.TorqueConverterConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6018,
            )

            return self._parent._cast(
                _6018.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6024.WormGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6024,
            )

            return self._parent._cast(_6024.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6027,
            )

            return self._parent._cast(_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
        ) -> "ConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5736.ConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis]

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
    ) -> "List[_5736.ConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis]

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
    ) -> "ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis":
        return self._Cast_ConnectionCompoundHarmonicAnalysis(self)
