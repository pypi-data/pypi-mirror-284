"""CouplingConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4090
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4210,
        _4215,
        _4269,
        _4291,
        _4306,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundPowerFlow")


class CouplingConnectionCompoundPowerFlow(
    _4253.InterMountableComponentConnectionCompoundPowerFlow
):
    """CouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionCompoundPowerFlow")

    class _Cast_CouplingConnectionCompoundPowerFlow:
        """Special nested class for casting CouplingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
            parent: "CouplingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4210.ClutchConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4215.ConceptCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4269.PartToPartShearCouplingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(
                _4269.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def spring_damper_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4291.SpringDamperConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.SpringDamperConnectionCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "_4306.TorqueConverterConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4306,
            )

            return self._parent._cast(_4306.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "CouplingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4090.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    ) -> "List[_4090.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    ) -> (
        "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow"
    ):
        return self._Cast_CouplingConnectionCompoundPowerFlow(self)
