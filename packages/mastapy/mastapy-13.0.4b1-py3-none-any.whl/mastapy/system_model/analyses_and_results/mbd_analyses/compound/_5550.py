"""AbstractAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5629
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5556,
        _5557,
        _5560,
        _5563,
        _5568,
        _5570,
        _5571,
        _5576,
        _5581,
        _5584,
        _5587,
        _5591,
        _5593,
        _5599,
        _5605,
        _5607,
        _5610,
        _5614,
        _5618,
        _5621,
        _5624,
        _5630,
        _5634,
        _5641,
        _5644,
        _5648,
        _5651,
        _5652,
        _5657,
        _5660,
        _5663,
        _5667,
        _5675,
        _5678,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundMultibodyDynamicsAnalysis")


class AbstractAssemblyCompoundMultibodyDynamicsAnalysis(
    _5629.PartCompoundMultibodyDynamicsAnalysis
):
    """AbstractAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(_5557.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(_5560.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5568.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5571.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5576.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5587.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5591.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5593.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5618.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(
                _5618.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5621.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5624.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5652.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5660.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5660,
            )

            return self._parent._cast(
                _5660.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5663.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5663,
            )

            return self._parent._cast(
                _5663.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5667.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5667,
            )

            return self._parent._cast(
                _5667.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5675.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5675,
            )

            return self._parent._cast(
                _5675.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5678.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5678,
            )

            return self._parent._cast(
                _5678.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5397.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5397.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis(self)
