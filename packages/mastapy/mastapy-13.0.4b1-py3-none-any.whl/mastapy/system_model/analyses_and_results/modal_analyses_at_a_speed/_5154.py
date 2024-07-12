"""BevelGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5149,
        _5238,
        _5244,
        _5247,
        _5265,
        _5170,
        _5196,
        _5203,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtASpeed")


class BevelGearMeshModalAnalysisAtASpeed(
    _5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
):
    """BevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtASpeed")

    class _Cast_BevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting BevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
            parent: "BevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(
                _5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5170.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5196.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5203.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(
                _5203.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5149.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(
                _5149.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5238.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5244.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(
                _5244.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5247.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5265.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5265,
            )

            return self._parent._cast(_5265.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "BevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed":
        return self._Cast_BevelGearMeshModalAnalysisAtASpeed(self)
