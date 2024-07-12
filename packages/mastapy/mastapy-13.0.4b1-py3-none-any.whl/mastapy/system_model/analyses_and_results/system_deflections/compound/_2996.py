"""VirtualComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "VirtualComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2856
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2948,
        _2949,
        _2959,
        _2960,
        _2995,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundSystemDeflection")


class VirtualComponentCompoundSystemDeflection(
    _2950.MountableComponentCompoundSystemDeflection
):
    """VirtualComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
            parent: "VirtualComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2948.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2949.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(
                _2949.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def point_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2959.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2960.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.PowerLoadCompoundSystemDeflection)

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2995.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2995,
            )

            return self._parent._cast(_2995.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "VirtualComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2856.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    ) -> "List[_2856.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    ) -> "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection":
        return self._Cast_VirtualComponentCompoundSystemDeflection(self)
