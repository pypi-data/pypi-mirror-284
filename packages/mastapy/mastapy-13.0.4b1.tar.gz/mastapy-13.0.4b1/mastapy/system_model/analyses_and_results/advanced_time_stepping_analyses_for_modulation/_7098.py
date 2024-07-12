"""InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7067,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301
    from mastapy.system_model.analyses_and_results.system_deflections import _2788
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7036,
        _7041,
        _7044,
        _7049,
        _7054,
        _7059,
        _7062,
        _7065,
        _7070,
        _7073,
        _7080,
        _7086,
        _7091,
        _7096,
        _7100,
        _7103,
        _7106,
        _7114,
        _7123,
        _7126,
        _7133,
        _7136,
        _7139,
        _7142,
        _7151,
        _7157,
        _7160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7067.ConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7067.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7036.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7041.BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7049.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7059.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7065.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7070.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7073.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7080.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7096.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7106.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7114.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7123.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7133.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7139.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7142.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7142,
            )

            return self._parent._cast(
                _7142.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7151.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7151,
            )

            return self._parent._cast(
                _7151.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7157.WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7157,
            )

            return self._parent._cast(
                _7157.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7160.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7160,
            )

            return self._parent._cast(
                _7160.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection

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
    ) -> "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
