"""SpiralBevelGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2828
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7299,
        _7327,
        _7355,
        _7361,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshAdvancedSystemDeflection")


class SpiralBevelGearMeshAdvancedSystemDeflection(
    _7311.BevelGearMeshAdvancedSystemDeflection
):
    """SpiralBevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshAdvancedSystemDeflection"
    )

    class _Cast_SpiralBevelGearMeshAdvancedSystemDeflection:
        """Special nested class for casting SpiralBevelGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
            parent: "SpiralBevelGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7311.BevelGearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7311.BevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(
                _7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7327.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7355.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7361.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(
                _7361.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
        ) -> "SpiralBevelGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self: Self) -> "_405.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2343.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6976.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2828.SpiralBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshAdvancedSystemDeflection._Cast_SpiralBevelGearMeshAdvancedSystemDeflection":
        return self._Cast_SpiralBevelGearMeshAdvancedSystemDeflection(self)
