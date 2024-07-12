"""HypoidGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _441
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4085,
        _4114,
        _4121,
        _4088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearMeshPowerFlow")


class HypoidGearMeshPowerFlow(_4057.AGMAGleasonConicalGearMeshPowerFlow):
    """HypoidGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshPowerFlow")

    class _Cast_HypoidGearMeshPowerFlow:
        """Special nested class for casting HypoidGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
            parent: "HypoidGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4057.AGMAGleasonConicalGearMeshPowerFlow":
            return self._parent._cast(_4057.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4085.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4114.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "HypoidGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_441.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_441.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6928.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow":
        return self._Cast_HypoidGearMeshPowerFlow(self)
