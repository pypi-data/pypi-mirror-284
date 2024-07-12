"""KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2339
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6331,
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
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis")


class KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis(
    _6367.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_6367.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            return self._parent._cast(
                _6367.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_6331.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_6359.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_6365.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(
                _6365.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_6333.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2339.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis(self)
