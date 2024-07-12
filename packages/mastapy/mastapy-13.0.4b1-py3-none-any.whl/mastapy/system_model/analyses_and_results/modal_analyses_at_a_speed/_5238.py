"""SpiralBevelGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5142,
        _5170,
        _5196,
        _5203,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshModalAnalysisAtASpeed")


class SpiralBevelGearMeshModalAnalysisAtASpeed(
    _5154.BevelGearMeshModalAnalysisAtASpeed
):
    """SpiralBevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshModalAnalysisAtASpeed"
    )

    class _Cast_SpiralBevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
            parent: "SpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5154.BevelGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5154.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(
                _5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5170.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5196.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5203.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(
                _5203.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "SpiralBevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "SpiralBevelGearMeshModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed":
        return self._Cast_SpiralBevelGearMeshModalAnalysisAtASpeed(self)
