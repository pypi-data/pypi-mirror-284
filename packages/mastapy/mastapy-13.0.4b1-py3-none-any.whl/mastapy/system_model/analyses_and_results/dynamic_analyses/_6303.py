"""AGMAGleasonConicalGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6310,
        _6315,
        _6363,
        _6400,
        _6406,
        _6409,
        _6427,
        _6359,
        _6365,
        _6333,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshDynamicAnalysis")


class AGMAGleasonConicalGearMeshDynamicAnalysis(_6331.ConicalGearMeshDynamicAnalysis):
    """AGMAGleasonConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
            parent: "AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6331.ConicalGearMeshDynamicAnalysis":
            return self._parent._cast(_6331.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6359.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6365.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(
                _6365.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6333.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6310.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6315.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.BevelGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6363.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.HypoidGearMeshDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6400.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6406.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6409.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "_6427.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6427

            return self._parent._cast(_6427.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis(self)
