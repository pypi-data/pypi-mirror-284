"""ConicalGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6569,
        _6576,
        _6581,
        _6630,
        _6634,
        _6637,
        _6640,
        _6667,
        _6673,
        _6676,
        _6694,
        _6632,
        _6599,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCriticalSpeedAnalysis")


class ConicalGearMeshCriticalSpeedAnalysis(_6626.GearMeshCriticalSpeedAnalysis):
    """ConicalGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshCriticalSpeedAnalysis")

    class _Cast_ConicalGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
            parent: "ConicalGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6626.GearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6626.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6632.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(
                _6632.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6599.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6569.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(
                _6569.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6576.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(
                _6576.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6581.BevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(_6581.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6630.HypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6634.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(
                _6634.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6637.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(
                _6637.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6640.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(
                _6640.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6667.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6673.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6673,
            )

            return self._parent._cast(
                _6673.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6676.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6676,
            )

            return self._parent._cast(_6676.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6694.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6694,
            )

            return self._parent._cast(_6694.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
        ) -> "ConicalGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2327.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis":
        return self._Cast_ConicalGearMeshCriticalSpeedAnalysis(self)
