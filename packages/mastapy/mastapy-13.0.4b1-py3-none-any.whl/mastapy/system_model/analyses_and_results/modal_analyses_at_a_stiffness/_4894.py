"""BevelGearMeshModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4882,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4889,
        _4979,
        _4985,
        _4988,
        _5006,
        _4910,
        _4937,
        _4944,
        _4913,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtAStiffness")


class BevelGearMeshModalAnalysisAtAStiffness(
    _4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
):
    """BevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
            parent: "BevelGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4910.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4937.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4944.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(
                _4944.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4913.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4889.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(
                _4889.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4979.SpiralBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(
                _4979.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4985.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(
                _4985.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4988.StraightBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4988,
            )

            return self._parent._cast(
                _4988.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_5006.ZerolBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5006,
            )

            return self._parent._cast(_5006.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "BevelGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtAStiffness.TYPE"
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
    ) -> "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness":
        return self._Cast_BevelGearMeshModalAnalysisAtAStiffness(self)
