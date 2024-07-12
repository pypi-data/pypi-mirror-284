"""CouplingHalfCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2751
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2895,
        _2900,
        _2914,
        _2955,
        _2961,
        _2965,
        _2978,
        _2988,
        _2989,
        _2990,
        _2993,
        _2994,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundSystemDeflection")


class CouplingHalfCompoundSystemDeflection(
    _2950.MountableComponentCompoundSystemDeflection
):
    """CouplingHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundSystemDeflection")

    class _Cast_CouplingHalfCompoundSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
            parent: "CouplingHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2895.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2900.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2914.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.CVTPulleyCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2955.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2961.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.PulleyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2965.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.RollingRingCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2978.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.SpringDamperHalfCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2988.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2988,
            )

            return self._parent._cast(_2988.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2989.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2990.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2990,
            )

            return self._parent._cast(_2990.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2993.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2993,
            )

            return self._parent._cast(_2993.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2994.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2994,
            )

            return self._parent._cast(
                _2994.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "CouplingHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2751.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

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
    ) -> "List[_2751.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

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
    ) -> "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection":
        return self._Cast_CouplingHalfCompoundSystemDeflection(self)
