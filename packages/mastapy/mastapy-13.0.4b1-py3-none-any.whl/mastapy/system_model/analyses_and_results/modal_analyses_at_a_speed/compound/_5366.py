"""SpecialisedAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5268,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5237,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5274,
        _5278,
        _5281,
        _5286,
        _5288,
        _5289,
        _5294,
        _5299,
        _5302,
        _5305,
        _5309,
        _5311,
        _5317,
        _5323,
        _5325,
        _5328,
        _5332,
        _5336,
        _5339,
        _5342,
        _5348,
        _5352,
        _5359,
        _5369,
        _5370,
        _5375,
        _5378,
        _5381,
        _5385,
        _5393,
        _5396,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtASpeed")


class SpecialisedAssemblyCompoundModalAnalysisAtASpeed(
    _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
):
    """SpecialisedAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5268.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5274.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5278.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5281.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5286.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5288.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5289.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5289,
            )

            return self._parent._cast(_5289.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5294.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(
                _5294.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5299.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(_5299.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5302.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5305.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5309.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5311.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5317.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5323.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5325.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5332.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5336.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(
                _5336.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5339.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5348.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5352.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5359.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5370.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(_5370.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5375.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5378.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(
                _5378.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5381.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(_5381.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5385.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5385,
            )

            return self._parent._cast(
                _5385.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5393.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5393,
            )

            return self._parent._cast(_5393.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5396.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5396,
            )

            return self._parent._cast(
                _5396.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5237.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5237.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed(self)
