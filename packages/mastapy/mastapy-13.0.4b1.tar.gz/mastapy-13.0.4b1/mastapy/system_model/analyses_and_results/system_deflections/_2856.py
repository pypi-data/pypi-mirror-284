"""VirtualComponentSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "VirtualComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.power_flows import _4181
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2800,
        _2801,
        _2812,
        _2813,
        _2855,
        _2736,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentSystemDeflection")


class VirtualComponentSystemDeflection(_2803.MountableComponentSystemDeflection):
    """VirtualComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentSystemDeflection")

    class _Cast_VirtualComponentSystemDeflection:
        """Special nested class for casting VirtualComponentSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
            parent: "VirtualComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2800.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2801.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.MeasurementComponentSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2812.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2813.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PowerLoadSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "_2855.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2855,
            )

            return self._parent._cast(_2855.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "VirtualComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentSystemDeflection.TYPE"):
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
    def power_flow_results(self: Self) -> "_4181.VirtualComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow

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
    ) -> "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection":
        return self._Cast_VirtualComponentSystemDeflection(self)
