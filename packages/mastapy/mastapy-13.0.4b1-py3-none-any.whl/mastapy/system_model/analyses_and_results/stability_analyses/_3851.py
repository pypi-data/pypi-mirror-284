"""InterMountableComponentConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3819
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "InterMountableComponentConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3788,
        _3793,
        _3795,
        _3800,
        _3805,
        _3810,
        _3813,
        _3816,
        _3821,
        _3825,
        _3832,
        _3839,
        _3844,
        _3848,
        _3852,
        _3855,
        _3858,
        _3866,
        _3876,
        _3878,
        _3885,
        _3888,
        _3894,
        _3897,
        _3906,
        _3912,
        _3915,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionStabilityAnalysis")


class InterMountableComponentConnectionStabilityAnalysis(
    _3819.ConnectionStabilityAnalysis
):
    """InterMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionStabilityAnalysis"
    )

    class _Cast_InterMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting InterMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
            parent: "InterMountableComponentConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3788.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3793.BeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3795.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3800.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3805.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3810.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3813.ConceptGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3816.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConicalGearMeshStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3821.CouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3825.CVTBeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.CVTBeltConnectionStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3832.CylindricalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(_3832.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3839.FaceGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3844.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3848.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.HypoidGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3852.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(
                _3852.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3855.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(
                _3855.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3858.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(
                _3858.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3866.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(
                _3866.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3876.RingPinsToDiscConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3878.RollingRingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.RollingRingConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3885.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3888.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3894.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3897.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3906.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3906,
            )

            return self._parent._cast(_3906.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3912.WormGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3912,
            )

            return self._parent._cast(_3912.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "_3915.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
        ) -> "InterMountableComponentConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis":
        return self._Cast_InterMountableComponentConnectionStabilityAnalysis(self)
