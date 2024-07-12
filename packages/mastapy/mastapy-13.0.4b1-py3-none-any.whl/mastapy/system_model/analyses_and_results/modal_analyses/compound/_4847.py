"""SpecialisedAssemblyCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpecialisedAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4703
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4755,
        _4759,
        _4762,
        _4767,
        _4769,
        _4770,
        _4775,
        _4780,
        _4783,
        _4786,
        _4790,
        _4792,
        _4798,
        _4804,
        _4806,
        _4809,
        _4813,
        _4817,
        _4820,
        _4823,
        _4829,
        _4833,
        _4840,
        _4850,
        _4851,
        _4856,
        _4859,
        _4862,
        _4866,
        _4874,
        _4877,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysis")


class SpecialisedAssemblyCompoundModalAnalysis(
    _4749.AbstractAssemblyCompoundModalAnalysis
):
    """SpecialisedAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
            parent: "SpecialisedAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4755.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(
                _4755.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def belt_drive_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4759.BeltDriveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4762.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(
                _4762.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4767.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4769.BoltedJointCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4770.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4775.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4780.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4783.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4786.CouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4790.CVTCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4792.CycloidalAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4798.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(_4798.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4804.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4806.FlexiblePinAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4809.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4813.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4817.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(
                _4817.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(
                _4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(
                _4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4829.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(
                _4829.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4833.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4840.RollingRingAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4850.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4851.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4856.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(
                _4856.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4859.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4859,
            )

            return self._parent._cast(_4859.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4862.SynchroniserCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4862,
            )

            return self._parent._cast(_4862.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4866.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4866,
            )

            return self._parent._cast(_4866.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4874.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4874,
            )

            return self._parent._cast(_4874.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "_4877.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4877,
            )

            return self._parent._cast(_4877.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4703.SpecialisedAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis]

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
    ) -> "List[_4703.SpecialisedAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysis(self)
