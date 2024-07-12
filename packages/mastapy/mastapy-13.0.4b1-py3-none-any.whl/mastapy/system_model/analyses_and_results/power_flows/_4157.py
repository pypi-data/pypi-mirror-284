"""SpiralBevelGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4069
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SpiralBevelGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4057,
        _4085,
        _4114,
        _4121,
        _4088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshPowerFlow")


class SpiralBevelGearMeshPowerFlow(_4069.BevelGearMeshPowerFlow):
    """SpiralBevelGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshPowerFlow")

    class _Cast_SpiralBevelGearMeshPowerFlow:
        """Special nested class for casting SpiralBevelGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
            parent: "SpiralBevelGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4069.BevelGearMeshPowerFlow":
            return self._parent._cast(_4069.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4057.AGMAGleasonConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4085.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4114.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
        ) -> "SpiralBevelGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_405.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshPowerFlow._Cast_SpiralBevelGearMeshPowerFlow":
        return self._Cast_SpiralBevelGearMeshPowerFlow(self)
