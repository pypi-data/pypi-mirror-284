"""KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7494,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2340
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7369,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7460,
        _7486,
        _7492,
        _7462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection(
    _7494.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7494.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7494.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7460.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7486.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(_7486.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7492.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7462.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7369.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection(
            self
        )
