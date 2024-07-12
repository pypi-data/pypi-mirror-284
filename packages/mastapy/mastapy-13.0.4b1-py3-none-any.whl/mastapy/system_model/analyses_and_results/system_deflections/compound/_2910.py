"""CouplingConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2750
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2894,
        _2899,
        _2954,
        _2977,
        _2992,
        _2907,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundSystemDeflection")


class CouplingConnectionCompoundSystemDeflection(
    _2938.InterMountableComponentConnectionCompoundSystemDeflection
):
    """CouplingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundSystemDeflection"
    )

    class _Cast_CouplingConnectionCompoundSystemDeflection:
        """Special nested class for casting CouplingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
            parent: "CouplingConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2938.InterMountableComponentConnectionCompoundSystemDeflection":
            return self._parent._cast(
                _2938.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2907.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2894.ClutchConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ClutchConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2899.ConceptCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(
                _2899.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2954.PartToPartShearCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(
                _2954.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2977.SpringDamperConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(
                _2977.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "_2992.TorqueConverterConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2992,
            )

            return self._parent._cast(
                _2992.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def coupling_connection_compound_system_deflection(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
        ) -> "CouplingConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2750.CouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2750.CouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection":
        return self._Cast_CouplingConnectionCompoundSystemDeflection(self)
