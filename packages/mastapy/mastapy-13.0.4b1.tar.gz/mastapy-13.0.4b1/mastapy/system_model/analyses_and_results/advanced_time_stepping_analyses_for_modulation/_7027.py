"""AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7112,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.system_deflections import _2706
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7037,
        _7038,
        _7042,
        _7045,
        _7050,
        _7052,
        _7053,
        _7058,
        _7063,
        _7066,
        _7069,
        _7072,
        _7075,
        _7081,
        _7087,
        _7089,
        _7092,
        _7097,
        _7101,
        _7104,
        _7107,
        _7113,
        _7117,
        _7125,
        _7127,
        _7131,
        _7134,
        _7135,
        _7140,
        _7143,
        _7146,
        _7150,
        _7158,
        _7161,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7112.PartAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7038.AssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7050.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.BoltedJointAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.ClutchAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7063.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7066.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.CouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7075.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7075,
            )

            return self._parent._cast(
                _7075.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7081.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7087.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7101.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7104.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7107.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7113.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7127.RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.SpringDamperAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.SynchroniserAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.TorqueConverterAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7150,
            )

            return self._parent._cast(
                _7150.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7158,
            )

            return self._parent._cast(
                _7158.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7161,
            )

            return self._parent._cast(
                _7161.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2706.AbstractAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation(
            self
        )
