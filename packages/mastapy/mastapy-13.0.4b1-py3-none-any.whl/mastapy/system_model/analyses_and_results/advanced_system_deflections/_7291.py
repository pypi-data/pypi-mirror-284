"""AbstractAssemblyAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AbstractAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7300,
        _7301,
        _7304,
        _7307,
        _7312,
        _7314,
        _7315,
        _7320,
        _7325,
        _7328,
        _7332,
        _7335,
        _7338,
        _7344,
        _7351,
        _7353,
        _7356,
        _7360,
        _7364,
        _7367,
        _7370,
        _7377,
        _7381,
        _7389,
        _7391,
        _7395,
        _7398,
        _7399,
        _7404,
        _7407,
        _7410,
        _7414,
        _7423,
        _7426,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblyAdvancedSystemDeflection")


class AbstractAssemblyAdvancedSystemDeflection(_7376.PartAdvancedSystemDeflection):
    """AbstractAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyAdvancedSystemDeflection"
    )

    class _Cast_AbstractAssemblyAdvancedSystemDeflection:
        """Special nested class for casting AbstractAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
            parent: "AbstractAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(
                _7300.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7301.AssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.AssemblyAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7304.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7307.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(
                _7307.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7312.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7314.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7315.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7320.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7325.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7328.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConicalGearSetAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7332.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.CouplingAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7335.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.CVTAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7338.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7344.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7351.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.FaceGearSetAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7353.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7356.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.GearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7360.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7364.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(
                _7364.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7367.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(
                _7367.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7370.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7377.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(
                _7377.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7381.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7389.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7391.RootAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.RootAssemblyAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7395.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7398.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7399.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.SpringDamperAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7404.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(
                _7404.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7410.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.SynchroniserAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7414.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7414,
            )

            return self._parent._cast(_7414.TorqueConverterAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7423.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7423,
            )

            return self._parent._cast(_7423.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7426.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "AbstractAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractAssemblyAdvancedSystemDeflection.TYPE"
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
    ) -> "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection":
        return self._Cast_AbstractAssemblyAdvancedSystemDeflection(self)
