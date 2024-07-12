"""ConceptGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4247
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConceptGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.power_flows import _4082
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4253,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearMeshCompoundPowerFlow")


class ConceptGearMeshCompoundPowerFlow(_4247.GearMeshCompoundPowerFlow):
    """ConceptGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshCompoundPowerFlow")

    class _Cast_ConceptGearMeshCompoundPowerFlow:
        """Special nested class for casting ConceptGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
            parent: "ConceptGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4247.GearMeshCompoundPowerFlow":
            return self._parent._cast(_4247.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
        ) -> "ConceptGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2325.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2325.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4082.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

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
    def connection_analysis_cases(self: Self) -> "List[_4082.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshCompoundPowerFlow._Cast_ConceptGearMeshCompoundPowerFlow":
        return self._Cast_ConceptGearMeshCompoundPowerFlow(self)
