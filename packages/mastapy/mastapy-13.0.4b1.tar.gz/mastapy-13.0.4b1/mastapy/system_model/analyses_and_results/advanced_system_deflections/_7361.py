"""InterMountableComponentConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7299,
        _7303,
        _7306,
        _7311,
        _7316,
        _7321,
        _7324,
        _7327,
        _7333,
        _7336,
        _7343,
        _7350,
        _7355,
        _7359,
        _7363,
        _7366,
        _7369,
        _7378,
        _7387,
        _7390,
        _7397,
        _7400,
        _7403,
        _7406,
        _7415,
        _7422,
        _7425,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionAdvancedSystemDeflection"
)


class InterMountableComponentConnectionAdvancedSystemDeflection(
    _7329.ConnectionAdvancedSystemDeflection
):
    """InterMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(
                _7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7303.BeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7306.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(
                _7306.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7311.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(_7311.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7316.ClutchConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7321.ConceptCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(
                _7321.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7324.ConceptGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7327.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7333.CouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7336.CVTBeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7343.CylindricalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7350.FaceGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7355.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7359.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7363.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(
                _7363.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> (
            "_7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7378.PartToPartShearCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7387.RingPinsToDiscConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7390.RollingRingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(
                _7390.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7397.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7400.SpringDamperConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(
                _7400.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7403.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(
                _7403.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7406.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(
                _7406.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7415.TorqueConverterConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7415,
            )

            return self._parent._cast(
                _7415.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7422.WormGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7422,
            )

            return self._parent._cast(_7422.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7425.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedSystemDeflection.TYPE",
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
    ) -> "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
