"""KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.power_flows import _4129
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2747,
        _2782,
        _2803,
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
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection")


class KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection(
    _2791.KlingelnbergCycloPalloidConicalGearSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2791.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            return self._parent._cast(
                _2791.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2747.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2782.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2560.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_409.KlingelnbergCycloPalloidSpiralBevelGearRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection(self)
