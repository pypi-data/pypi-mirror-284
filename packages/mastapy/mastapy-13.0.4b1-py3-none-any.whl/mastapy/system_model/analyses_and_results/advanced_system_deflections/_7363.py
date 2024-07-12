"""KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7366,
        _7369,
        _7355,
        _7361,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection(
    _7327.ConicalGearMeshAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7327.ConicalGearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7327.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7355.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7361.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(
                _7361.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
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
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection(
                self
            )
        )
