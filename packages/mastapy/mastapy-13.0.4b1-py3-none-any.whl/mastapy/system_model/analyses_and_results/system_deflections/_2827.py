"""SpecialisedAssemblySystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpecialisedAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.power_flows import _4156
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2711,
        _2721,
        _2723,
        _2728,
        _2730,
        _2734,
        _2740,
        _2742,
        _2746,
        _2752,
        _2755,
        _2756,
        _2763,
        _2764,
        _2765,
        _2776,
        _2779,
        _2781,
        _2785,
        _2790,
        _2793,
        _2796,
        _2809,
        _2818,
        _2829,
        _2833,
        _2835,
        _2838,
        _2845,
        _2851,
        _2858,
        _2861,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblySystemDeflection")


class SpecialisedAssemblySystemDeflection(_2706.AbstractAssemblySystemDeflection):
    """SpecialisedAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblySystemDeflection")

    class _Cast_SpecialisedAssemblySystemDeflection:
        """Special nested class for casting SpecialisedAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
            parent: "SpecialisedAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2706.AbstractAssemblySystemDeflection":
            return self._parent._cast(_2706.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2711.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2721.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2723.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2728.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2730.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2734.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2740.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2742.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2746.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2752.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2755.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2756.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2763.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2764.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2765.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2776.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(_2776.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2779.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2781.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2785.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2793.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2796.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2809.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2818.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.RollingRingAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2829.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2833.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2835.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2838.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2845.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2851.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2851,
            )

            return self._parent._cast(_2851.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2858.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2861.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.ZerolBevelGearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "SpecialisedAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblySystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4156.SpecialisedAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection"
    ):
        return self._Cast_SpecialisedAssemblySystemDeflection(self)
