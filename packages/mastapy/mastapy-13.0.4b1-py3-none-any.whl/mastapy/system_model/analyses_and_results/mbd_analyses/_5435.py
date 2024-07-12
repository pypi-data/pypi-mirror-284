"""ConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5486,
        _5400,
        _5401,
        _5408,
        _5410,
        _5415,
        _5420,
        _5424,
        _5426,
        _5429,
        _5432,
        _5437,
        _5440,
        _5444,
        _5446,
        _5447,
        _5453,
        _5458,
        _5463,
        _5470,
        _5471,
        _5474,
        _5477,
        _5489,
        _5492,
        _5499,
        _5501,
        _5508,
        _5511,
        _5514,
        _5517,
        _5520,
        _5529,
        _5538,
        _5541,
    )
    from mastapy.math_utility.convergence import _1593
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectionMultibodyDynamicsAnalysis")


class ConnectionMultibodyDynamicsAnalysis(_7563.ConnectionTimeSeriesLoadAnalysisCase):
    """ConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionMultibodyDynamicsAnalysis")

    class _Cast_ConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
            parent: "ConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5400.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(
                _5400.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5408.BeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5410.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(
                _5410.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5415.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5420.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5424.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5426.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5429.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5432.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5437.CouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5440.CVTBeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5444.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(
                _5444.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5446.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5447.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5453.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(_5453.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5458.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(_5458.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5463.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5471.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5474.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(
                _5474.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5477.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5489.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5492.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5499.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5501.RollingRingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5508.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5511.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5514.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(
                _5514.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5517.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(
                _5517.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5520.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(
                _5520.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5529.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(
                _5529.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5538.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5538

            return self._parent._cast(_5538.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5541.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5541

            return self._parent._cast(_5541.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "ConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self: Self) -> "_2292.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2292.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def multibody_dynamics_analysis(self: Self) -> "_5486.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1593.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis"
    ):
        return self._Cast_ConnectionMultibodyDynamicsAnalysis(self)
