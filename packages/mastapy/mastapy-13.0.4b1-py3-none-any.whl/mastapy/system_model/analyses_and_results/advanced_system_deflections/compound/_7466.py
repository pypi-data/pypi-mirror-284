"""CouplingHalfCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7334,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7450,
        _7455,
        _7469,
        _7509,
        _7515,
        _7519,
        _7531,
        _7541,
        _7542,
        _7543,
        _7546,
        _7547,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundAdvancedSystemDeflection")


class CouplingHalfCompoundAdvancedSystemDeflection(
    _7504.MountableComponentCompoundAdvancedSystemDeflection
):
    """CouplingHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
            parent: "CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7450.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7455.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(
                _7455.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7469.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(_7469.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7509.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7515.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(_7515.PulleyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7519.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(_7519.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7531.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7541.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7542.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7543.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7543,
            )

            return self._parent._cast(
                _7543.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7546.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7546,
            )

            return self._parent._cast(
                _7546.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7547.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7547,
            )

            return self._parent._cast(
                _7547.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CouplingHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7334.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "List[_7334.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingHalfCompoundAdvancedSystemDeflection(self)
