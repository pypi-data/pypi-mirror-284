"""SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5009,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4978,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5015,
        _5019,
        _5022,
        _5027,
        _5029,
        _5030,
        _5035,
        _5040,
        _5043,
        _5046,
        _5050,
        _5052,
        _5058,
        _5064,
        _5066,
        _5069,
        _5073,
        _5077,
        _5080,
        _5083,
        _5089,
        _5093,
        _5100,
        _5110,
        _5111,
        _5116,
        _5119,
        _5122,
        _5126,
        _5134,
        _5137,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtAStiffness")


class SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(
    _5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness
):
    """SpecialisedAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5019.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(_5019.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5030.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(_5030.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5035.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5040.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5050.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5052.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(_5069.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5077.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(
                _5077.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5080.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5083.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(
                _5083.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5093.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5100.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5110.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5111.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5116.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5119.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5119,
            )

            return self._parent._cast(
                _5119.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5122.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5122,
            )

            return self._parent._cast(
                _5122.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5126.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5126,
            )

            return self._parent._cast(
                _5126.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5134.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5134,
            )

            return self._parent._cast(
                _5134.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5137.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5137,
            )

            return self._parent._cast(
                _5137.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4978.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

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
    ) -> "List[_4978.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(self)
