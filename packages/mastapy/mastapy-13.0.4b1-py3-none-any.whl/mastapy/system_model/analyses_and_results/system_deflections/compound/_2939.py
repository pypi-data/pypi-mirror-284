"""KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2791
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2942,
        _2945,
        _2931,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection(
    _2904.ConicalGearCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2942.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "_2945.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(
                _2945.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2791.KlingelnbergCycloPalloidConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2791.KlingelnbergCycloPalloidConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection(
            self
        )
