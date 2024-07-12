"""SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6160,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6129,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6166,
        _6170,
        _6173,
        _6178,
        _6180,
        _6181,
        _6186,
        _6191,
        _6194,
        _6197,
        _6201,
        _6203,
        _6209,
        _6215,
        _6217,
        _6220,
        _6224,
        _6228,
        _6231,
        _6234,
        _6240,
        _6244,
        _6251,
        _6261,
        _6262,
        _6267,
        _6270,
        _6273,
        _6277,
        _6285,
        _6288,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"
)


class SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6166.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6170.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6173.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6178.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6180.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6181.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6186.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6191.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6194.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6197.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6201.CVTCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6203.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6209.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6215.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6217.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6228.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6228,
            )

            return self._parent._cast(
                _6228.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6231.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6234.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6240.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6251.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6261.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6262.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6267.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6270.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6270,
            )

            return self._parent._cast(
                _6270.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6273.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6273,
            )

            return self._parent._cast(
                _6273.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6277.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6277,
            )

            return self._parent._cast(
                _6277.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6285.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6285,
            )

            return self._parent._cast(
                _6285.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6288.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6288,
            )

            return self._parent._cast(
                _6288.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
