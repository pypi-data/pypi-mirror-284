"""WormGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "WormGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.worm import _376
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _7005
    from mastapy.system_model.analyses_and_results.power_flows import _4182
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2788,
        _2748,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="WormGearMeshSystemDeflection")


class WormGearMeshSystemDeflection(_2780.GearMeshSystemDeflection):
    """WormGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshSystemDeflection")

    class _Cast_WormGearMeshSystemDeflection:
        """Special nested class for casting WormGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
            parent: "WormGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_system_deflection(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2780.GearMeshSystemDeflection":
            return self._parent._cast(_2780.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(
                _2788.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_system_deflection(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
        ) -> "WormGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_376.WormGearMeshRating":
        """mastapy.gears.rating.worm.WormGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_376.WormGearMeshRating":
        """mastapy.gears.rating.worm.WormGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2349.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7005.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4182.WormGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.WormGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshSystemDeflection._Cast_WormGearMeshSystemDeflection":
        return self._Cast_WormGearMeshSystemDeflection(self)
