"""BevelGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7306,
        _7397,
        _7403,
        _7406,
        _7425,
        _7327,
        _7355,
        _7361,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshAdvancedSystemDeflection")


class BevelGearMeshAdvancedSystemDeflection(
    _7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
):
    """BevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshAdvancedSystemDeflection"
    )

    class _Cast_BevelGearMeshAdvancedSystemDeflection:
        """Special nested class for casting BevelGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
            parent: "BevelGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            return self._parent._cast(
                _7299.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7327.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7355.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7361.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(
                _7361.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7306.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(
                _7306.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7397.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7403.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(
                _7403.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7406.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(
                _7406.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7425.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "BevelGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearMeshAdvancedSystemDeflection.TYPE"
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
    ) -> "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection":
        return self._Cast_BevelGearMeshAdvancedSystemDeflection(self)
