"""ConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5553,
        _5555,
        _5559,
        _5562,
        _5567,
        _5572,
        _5574,
        _5577,
        _5580,
        _5583,
        _5588,
        _5590,
        _5594,
        _5596,
        _5598,
        _5604,
        _5609,
        _5613,
        _5615,
        _5617,
        _5620,
        _5623,
        _5631,
        _5633,
        _5640,
        _5643,
        _5647,
        _5650,
        _5653,
        _5656,
        _5659,
        _5668,
        _5674,
        _5677,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundMultibodyDynamicsAnalysis")


class ConnectionCompoundMultibodyDynamicsAnalysis(_7560.ConnectionCompoundAnalysis):
    """ConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.BeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5577.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5588.CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5594.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5609.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(_5609.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(
                _5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5631.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5633.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5640.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5668.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5668,
            )

            return self._parent._cast(
                _5668.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5674.WormGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5674,
            )

            return self._parent._cast(
                _5674.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5677,
            )

            return self._parent._cast(
                _5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5435.ConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5435.ConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis]

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
    ) -> "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConnectionCompoundMultibodyDynamicsAnalysis(self)
