"""SpecialisedAssemblyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpecialisedAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4156
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4194,
        _4198,
        _4201,
        _4206,
        _4208,
        _4209,
        _4214,
        _4219,
        _4222,
        _4225,
        _4229,
        _4231,
        _4237,
        _4243,
        _4245,
        _4248,
        _4252,
        _4256,
        _4259,
        _4262,
        _4268,
        _4272,
        _4279,
        _4289,
        _4290,
        _4295,
        _4298,
        _4301,
        _4305,
        _4313,
        _4316,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundPowerFlow")


class SpecialisedAssemblyCompoundPowerFlow(_4188.AbstractAssemblyCompoundPowerFlow):
    """SpecialisedAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundPowerFlow")

    class _Cast_SpecialisedAssemblyCompoundPowerFlow:
        """Special nested class for casting SpecialisedAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
            parent: "SpecialisedAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4198.BeltDriveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4206.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4208.BoltedJointCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4209.ClutchCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4214.ConceptCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4219.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4222.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4225.CouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4229.CVTCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4231.CycloidalAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4237.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4243.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4245.FlexiblePinAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4248.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4252.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4256.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(
                _4256.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4259.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(
                _4259.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4262.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(
                _4262.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4268.PartToPartShearCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4272.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4279.RollingRingAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.RollingRingAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4290.SpringDamperCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4301.SynchroniserCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4305.TorqueConverterCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4305,
            )

            return self._parent._cast(_4305.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4313.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4313,
            )

            return self._parent._cast(_4313.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "SpecialisedAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4156.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4156.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow":
        return self._Cast_SpecialisedAssemblyCompoundPowerFlow(self)
