"""GearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _368
    from mastapy.system_model.analyses_and_results.power_flows import _4114
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4193,
        _4200,
        _4205,
        _4218,
        _4221,
        _4236,
        _4242,
        _4251,
        _4255,
        _4258,
        _4261,
        _4288,
        _4294,
        _4297,
        _4312,
        _4315,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearMeshCompoundPowerFlow")


class GearMeshCompoundPowerFlow(
    _4253.InterMountableComponentConnectionCompoundPowerFlow
):
    """GearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundPowerFlow")

    class _Cast_GearMeshCompoundPowerFlow:
        """Special nested class for casting GearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
            parent: "GearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4193.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4200.BevelDifferentialGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4205.BevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelGearMeshCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4218.ConceptGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4221.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.ConicalGearMeshCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4236.CylindricalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(_4236.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4242.FaceGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.FaceGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4251.HypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4255.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(
                _4255.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4258.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(
                _4258.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4261.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4288.SpiralBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4294.StraightBevelDiffGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4297.StraightBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4312.WormGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4312,
            )

            return self._parent._cast(_4312.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "_4315.ZerolBevelGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4315,
            )

            return self._parent._cast(_4315.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "GearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_rating(self: Self) -> "_368.MeshDutyCycleRating":
        """mastapy.gears.rating.MeshDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases(self: Self) -> "List[_4114.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

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
    def connection_analysis_cases_ready(self: Self) -> "List[_4114.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

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
    ) -> "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow":
        return self._Cast_GearMeshCompoundPowerFlow(self)
