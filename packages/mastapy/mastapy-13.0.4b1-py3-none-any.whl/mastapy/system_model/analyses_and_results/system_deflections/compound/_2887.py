"""BevelDifferentialSunGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2883
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelDifferentialSunGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2726
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2888,
        _2876,
        _2904,
        _2931,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundSystemDeflection")


class BevelDifferentialSunGearCompoundSystemDeflection(
    _2883.BevelDifferentialGearCompoundSystemDeflection
):
    """BevelDifferentialSunGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundSystemDeflection"
    )

    class _Cast_BevelDifferentialSunGearCompoundSystemDeflection:
        """Special nested class for casting BevelDifferentialSunGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
            parent: "BevelDifferentialSunGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2883.BevelDifferentialGearCompoundSystemDeflection":
            return self._parent._cast(
                _2883.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2888.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2876.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "BevelDifferentialSunGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2726.BevelDifferentialSunGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection]

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
    ) -> "List[_2726.BevelDifferentialSunGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection]

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
    ) -> "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection":
        return self._Cast_BevelDifferentialSunGearCompoundSystemDeflection(self)
