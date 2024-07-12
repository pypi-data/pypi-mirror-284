"""AbstractAssemblySteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3084,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3009,
        _3011,
        _3014,
        _3016,
        _3021,
        _3023,
        _3027,
        _3032,
        _3034,
        _3037,
        _3043,
        _3046,
        _3047,
        _3052,
        _3059,
        _3062,
        _3064,
        _3068,
        _3072,
        _3075,
        _3078,
        _3087,
        _3089,
        _3096,
        _3099,
        _3103,
        _3105,
        _3109,
        _3114,
        _3117,
        _3124,
        _3127,
        _3132,
        _3135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponse")


class AbstractAssemblySteadyStateSynchronousResponse(
    _3084.PartSteadyStateSynchronousResponse
):
    """AbstractAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
            parent: "AbstractAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3009.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3011.AssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(_3011.AssemblySteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3014.BeltDriveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3016.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(
                _3016.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3021.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(_3021.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3023.BoltedJointSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.BoltedJointSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3027.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3027,
            )

            return self._parent._cast(_3027.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3032.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(
                _3032.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3034.ConceptGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3037.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(
                _3037.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3043.CouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(_3043.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3046.CVTSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3047.CycloidalAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3052.CylindricalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3059.FaceGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(_3059.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3062.FlexiblePinAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3064.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(_3064.GearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3068.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3072.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3075.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3078.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(
                _3078.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3087.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(
                _3087.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3089.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3096.RollingRingAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3099.RootAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(_3099.RootAssemblySteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3103.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3105.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3109.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(_3109.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3114.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3117.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3117,
            )

            return self._parent._cast(
                _3117.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3124.SynchroniserSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3124,
            )

            return self._parent._cast(_3124.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3127.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3127,
            )

            return self._parent._cast(
                _3127.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3132.WormGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3132,
            )

            return self._parent._cast(_3132.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3135.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3135,
            )

            return self._parent._cast(
                _3135.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "AbstractAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponse(self)
