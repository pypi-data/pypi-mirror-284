"""KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.system_deflections import _2797
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2904,
        _2931,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection(
    _2939.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2939.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            return self._parent._cast(
                _2939.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2797.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2797.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection(
                self
            )
        )
