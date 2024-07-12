"""WormGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5196
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _7005
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5203,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearMeshModalAnalysisAtASpeed")


class WormGearMeshModalAnalysisAtASpeed(_5196.GearMeshModalAnalysisAtASpeed):
    """WormGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshModalAnalysisAtASpeed")

    class _Cast_WormGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting WormGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
            parent: "WormGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_5196.GearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5196.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_5203.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(
                _5203.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "WormGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "WormGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed":
        return self._Cast_WormGearMeshModalAnalysisAtASpeed(self)
