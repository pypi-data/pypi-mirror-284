"""AbstractAssemblyCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6435,
        _6436,
        _6439,
        _6442,
        _6447,
        _6449,
        _6450,
        _6455,
        _6460,
        _6463,
        _6466,
        _6470,
        _6472,
        _6478,
        _6484,
        _6486,
        _6489,
        _6493,
        _6497,
        _6500,
        _6503,
        _6509,
        _6513,
        _6520,
        _6523,
        _6527,
        _6530,
        _6531,
        _6536,
        _6539,
        _6542,
        _6546,
        _6554,
        _6557,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundDynamicAnalysis")


class AbstractAssemblyCompoundDynamicAnalysis(_6508.PartCompoundDynamicAnalysis):
    """AbstractAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
            parent: "AbstractAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6435.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(
                _6435.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6436.AssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.AssemblyCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6439.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6442.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(
                _6442.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6447.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6449.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6450.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6455.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6460.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6463.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6466.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6470.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6472.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6478.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(_6478.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6484.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6486.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6489.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6493.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6497.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(
                _6497.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6500.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(
                _6500.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6503.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(
                _6503.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6509.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(
                _6509.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6513.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6520.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6523.RootAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.RootAssemblyCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6527.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6530.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6531.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6536.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(
                _6536.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6539.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6539,
            )

            return self._parent._cast(_6539.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6542.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6542,
            )

            return self._parent._cast(_6542.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6546.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6546,
            )

            return self._parent._cast(_6546.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6554.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6554,
            )

            return self._parent._cast(_6554.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "_6557.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6557,
            )

            return self._parent._cast(_6557.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "AbstractAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6298.AbstractAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis]

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
    ) -> "List[_6298.AbstractAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis]

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
    ) -> "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis":
        return self._Cast_AbstractAssemblyCompoundDynamicAnalysis(self)
