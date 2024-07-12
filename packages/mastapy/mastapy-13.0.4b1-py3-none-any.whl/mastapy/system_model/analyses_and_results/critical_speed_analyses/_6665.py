"""SpecialisedAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6570,
        _6574,
        _6577,
        _6582,
        _6584,
        _6586,
        _6591,
        _6595,
        _6598,
        _6602,
        _6608,
        _6610,
        _6616,
        _6622,
        _6624,
        _6627,
        _6631,
        _6635,
        _6638,
        _6641,
        _6648,
        _6651,
        _6658,
        _6668,
        _6670,
        _6674,
        _6677,
        _6680,
        _6685,
        _6692,
        _6695,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCriticalSpeedAnalysis")


class SpecialisedAssemblyCriticalSpeedAnalysis(
    _6564.AbstractAssemblyCriticalSpeedAnalysis
):
    """SpecialisedAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_SpecialisedAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting SpecialisedAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
            parent: "SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(
                _6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def belt_drive_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6574.BeltDriveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6577.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(
                _6577.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6582.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6584.BoltedJointCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6586.ClutchCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6591.ConceptCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6595.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6598.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6602.CouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.CouplingCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6608.CVTCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.CVTCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6610.CycloidalAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6616.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(_6616.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6622.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.FaceGearSetCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6624.FlexiblePinAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6627.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.GearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6631.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6635.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(
                _6635.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6638.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6641.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6648.PartToPartShearCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(
                _6648.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6651.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6658.RollingRingAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6668.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6670.SpringDamperCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.SpringDamperCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6674.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(
                _6674.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6677.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6680.SynchroniserCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.SynchroniserCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6685.TorqueConverterCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6685,
            )

            return self._parent._cast(_6685.TorqueConverterCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6692.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6692,
            )

            return self._parent._cast(_6692.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6695.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2496.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

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
    ) -> "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis":
        return self._Cast_SpecialisedAssemblyCriticalSpeedAnalysis(self)
