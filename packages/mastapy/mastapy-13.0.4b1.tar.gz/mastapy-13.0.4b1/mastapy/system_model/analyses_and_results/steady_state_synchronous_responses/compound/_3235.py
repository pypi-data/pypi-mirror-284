"""SpecialisedAssemblyCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3137,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3103,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3143,
        _3147,
        _3150,
        _3155,
        _3157,
        _3158,
        _3163,
        _3168,
        _3171,
        _3174,
        _3178,
        _3180,
        _3186,
        _3192,
        _3194,
        _3197,
        _3201,
        _3205,
        _3208,
        _3211,
        _3217,
        _3221,
        _3228,
        _3238,
        _3239,
        _3244,
        _3247,
        _3250,
        _3254,
        _3262,
        _3265,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundSteadyStateSynchronousResponse"
)


class SpecialisedAssemblyCompoundSteadyStateSynchronousResponse(
    _3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse
):
    """SpecialisedAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SpecialisedAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3147.BeltDriveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3150.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.BoltedJointCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3168.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.CouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(_3178.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3180.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3186.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3192.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3194.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3205.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3208.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3211.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3217.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3221.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3228.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3238.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3244.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3247.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3247,
            )

            return self._parent._cast(
                _3247.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3250.SynchroniserCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3250,
            )

            return self._parent._cast(
                _3250.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3254.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3254,
            )

            return self._parent._cast(
                _3254.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3262.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3262,
            )

            return self._parent._cast(
                _3262.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3265.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3265,
            )

            return self._parent._cast(
                _3265.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3103.SpecialisedAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpecialisedAssemblySteadyStateSynchronousResponse]

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
    ) -> "List[_3103.SpecialisedAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpecialisedAssemblySteadyStateSynchronousResponse]

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
    ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse(
            self
        )
