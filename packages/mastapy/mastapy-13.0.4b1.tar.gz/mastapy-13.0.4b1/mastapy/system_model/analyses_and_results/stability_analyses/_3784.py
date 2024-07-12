"""AbstractAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3789,
        _3791,
        _3794,
        _3796,
        _3801,
        _3803,
        _3807,
        _3812,
        _3814,
        _3817,
        _3823,
        _3827,
        _3828,
        _3833,
        _3840,
        _3843,
        _3845,
        _3849,
        _3853,
        _3856,
        _3859,
        _3868,
        _3870,
        _3877,
        _3880,
        _3884,
        _3886,
        _3890,
        _3895,
        _3898,
        _3905,
        _3908,
        _3913,
        _3916,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyStabilityAnalysis")


class AbstractAssemblyStabilityAnalysis(_3865.PartStabilityAnalysis):
    """AbstractAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyStabilityAnalysis")

    class _Cast_AbstractAssemblyStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
            parent: "AbstractAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3789.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3791.AssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.AssemblyStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3794.BeltDriveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3796.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3801.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3803.BoltedJointStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3807.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3812.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3814.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3817.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3823.CouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3827.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3828.CycloidalAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3833.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(_3833.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3840.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3843.FlexiblePinAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3849.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3853.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(
                _3853.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3856.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(
                _3856.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3859.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(
                _3859.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3868.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3870.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3877.RollingRingAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.RollingRingAssemblyStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3880.RootAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.RootAssemblyStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3886.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3890.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3895.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3895,
            )

            return self._parent._cast(_3895.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3898.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3905.SynchroniserStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3905,
            )

            return self._parent._cast(_3905.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3908.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3908,
            )

            return self._parent._cast(_3908.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3913.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3913,
            )

            return self._parent._cast(_3913.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3916.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3916,
            )

            return self._parent._cast(_3916.ZerolBevelGearSetStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "AbstractAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyStabilityAnalysis.TYPE"
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
    ) -> "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis":
        return self._Cast_AbstractAssemblyStabilityAnalysis(self)
