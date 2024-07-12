"""VirtualComponentAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "VirtualComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7372,
        _7373,
        _7383,
        _7384,
        _7419,
        _7319,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentAdvancedSystemDeflection")


class VirtualComponentAdvancedSystemDeflection(
    _7374.MountableComponentAdvancedSystemDeflection
):
    """VirtualComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentAdvancedSystemDeflection"
    )

    class _Cast_VirtualComponentAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
            parent: "VirtualComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7374.MountableComponentAdvancedSystemDeflection":
            return self._parent._cast(_7374.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7372.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7373.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def point_load_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7383.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7384.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(_7384.PowerLoadAdvancedSystemDeflection)

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7419.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7419,
            )

            return self._parent._cast(_7419.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "VirtualComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "VirtualComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection":
        return self._Cast_VirtualComponentAdvancedSystemDeflection(self)
