"""SpecialisedAssemblyCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5900
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5831
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5906,
        _5910,
        _5913,
        _5918,
        _5920,
        _5921,
        _5926,
        _5931,
        _5934,
        _5937,
        _5941,
        _5943,
        _5949,
        _5955,
        _5957,
        _5960,
        _5964,
        _5968,
        _5971,
        _5974,
        _5980,
        _5984,
        _5991,
        _6001,
        _6002,
        _6007,
        _6010,
        _6013,
        _6017,
        _6025,
        _6028,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundHarmonicAnalysis")


class SpecialisedAssemblyCompoundHarmonicAnalysis(
    _5900.AbstractAssemblyCompoundHarmonicAnalysis
):
    """SpecialisedAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundHarmonicAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundHarmonicAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
            parent: "SpecialisedAssemblyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5900.AbstractAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5900.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5906.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(
                _5906.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5910.BeltDriveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5913.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(
                _5913.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5918.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5920.BoltedJointCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5921.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.ClutchCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5926.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5931.ConceptGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5934.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5937.CouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.CouplingCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5941.CVTCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.CVTCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5943.CycloidalAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(_5943.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5949.CylindricalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(_5949.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5955.FaceGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5957.FlexiblePinAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5960.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.GearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5964.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5968.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(
                _5968.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5971.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(
                _5971.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5974.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(
                _5974.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5980.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(
                _5980.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5984.PlanetaryGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_5991.RollingRingAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6001.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6002.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.SpringDamperCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6007.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(
                _6007.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6010.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6010,
            )

            return self._parent._cast(
                _6010.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6013.SynchroniserCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6013,
            )

            return self._parent._cast(_6013.SynchroniserCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6017.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6017,
            )

            return self._parent._cast(_6017.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6025.WormGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6025,
            )

            return self._parent._cast(_6025.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "_6028.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6028,
            )

            return self._parent._cast(_6028.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
        ) -> "SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5831.SpecialisedAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis]

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
    ) -> "List[_5831.SpecialisedAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundHarmonicAnalysis._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundHarmonicAnalysis(self)
