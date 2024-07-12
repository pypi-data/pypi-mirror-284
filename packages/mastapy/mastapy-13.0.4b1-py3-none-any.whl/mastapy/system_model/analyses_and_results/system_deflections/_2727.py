"""BevelGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.power_flows import _4069
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2722,
        _2828,
        _2834,
        _2837,
        _2860,
        _2745,
        _2780,
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
__all__ = ("BevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshSystemDeflection")


class BevelGearMeshSystemDeflection(_2710.AGMAGleasonConicalGearMeshSystemDeflection):
    """BevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshSystemDeflection")

    class _Cast_BevelGearMeshSystemDeflection:
        """Special nested class for casting BevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            parent: "BevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2710.AGMAGleasonConicalGearMeshSystemDeflection":
            return self._parent._cast(_2710.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2745.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2780.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(
                _2788.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2722.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.BevelDifferentialGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2828.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2834.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2837.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "_2860.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.ZerolBevelGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "BevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshSystemDeflection.TYPE"):
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
    def power_flow_results(self: Self) -> "_4069.BevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow

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
    ) -> "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection":
        return self._Cast_BevelGearMeshSystemDeflection(self)
