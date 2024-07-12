"""AbstractAssemblyCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6775,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6564
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6702,
        _6703,
        _6706,
        _6709,
        _6714,
        _6716,
        _6717,
        _6722,
        _6727,
        _6730,
        _6733,
        _6737,
        _6739,
        _6745,
        _6751,
        _6753,
        _6756,
        _6760,
        _6764,
        _6767,
        _6770,
        _6776,
        _6780,
        _6787,
        _6790,
        _6794,
        _6797,
        _6798,
        _6803,
        _6806,
        _6809,
        _6813,
        _6821,
        _6824,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundCriticalSpeedAnalysis")


class AbstractAssemblyCompoundCriticalSpeedAnalysis(
    _6775.PartCompoundCriticalSpeedAnalysis
):
    """AbstractAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
            parent: "AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6703.AssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6706.BeltDriveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(
                _6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6714.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6716.BoltedJointCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6717.ClutchCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6722.ConceptCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(
                _6722.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6727.ConceptGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(_6727.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6730.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6733.CouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6737.CVTCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6739.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(
                _6739.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6745.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6751.FaceGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6753.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6756.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6760.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6764.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(
                _6764.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6767.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6770.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6776.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6787.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6790.RootAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(_6790.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6798.SpringDamperCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(
                _6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6809.SynchroniserCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6809,
            )

            return self._parent._cast(_6809.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6813.TorqueConverterCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6813,
            )

            return self._parent._cast(
                _6813.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6821.WormGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6821,
            )

            return self._parent._cast(_6821.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6824,
            )

            return self._parent._cast(
                _6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6564.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    ) -> "List[_6564.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis(self)
