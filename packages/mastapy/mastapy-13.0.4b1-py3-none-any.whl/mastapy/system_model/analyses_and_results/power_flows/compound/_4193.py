"""AGMAGleasonConicalGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4057
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4200,
        _4205,
        _4251,
        _4288,
        _4294,
        _4297,
        _4315,
        _4247,
        _4253,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundPowerFlow")


class AGMAGleasonConicalGearMeshCompoundPowerFlow(
    _4221.ConicalGearMeshCompoundPowerFlow
):
    """AGMAGleasonConicalGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4221.ConicalGearMeshCompoundPowerFlow":
            return self._parent._cast(_4221.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4247.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4200.BevelDifferentialGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4205.BevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4251.HypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.HypoidGearMeshCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4288.SpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4294.StraightBevelDiffGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4297.StraightBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "_4315.ZerolBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4315,
            )

            return self._parent._cast(_4315.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4057.AGMAGleasonConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearMeshPowerFlow]

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
    ) -> "List[_4057.AGMAGleasonConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearMeshPowerFlow]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow(self)
