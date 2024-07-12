"""SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3525,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3530,
        _3535,
        _3537,
        _3542,
        _3544,
        _3548,
        _3553,
        _3555,
        _3558,
        _3564,
        _3567,
        _3568,
        _3573,
        _3579,
        _3582,
        _3584,
        _3588,
        _3592,
        _3595,
        _3598,
        _3607,
        _3609,
        _3616,
        _3625,
        _3629,
        _3632,
        _3635,
        _3642,
        _3645,
        _3650,
        _3653,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"
)


class SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed(
    _3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
):
    """SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3530.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3535.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3537.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3544.BoltedJointSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3548.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(
                _3548.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3553.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3555.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3558.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.CouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3567.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(_3567.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3568.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3584.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3588.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3592.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3595.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3598.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3609.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3625.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3632.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.SynchroniserSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3642,
            )

            return self._parent._cast(
                _3642.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3645.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3645,
            )

            return self._parent._cast(
                _3645.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3650.WormGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3650,
            )

            return self._parent._cast(
                _3650.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3653.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3653,
            )

            return self._parent._cast(
                _3653.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2496.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed(
            self
        )
