"""SpecialisedAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpecialisedAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.system_deflections import _2827
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4599,
        _4603,
        _4606,
        _4611,
        _4612,
        _4616,
        _4621,
        _4624,
        _4627,
        _4633,
        _4635,
        _4637,
        _4643,
        _4652,
        _4654,
        _4658,
        _4662,
        _4666,
        _4669,
        _4672,
        _4686,
        _4688,
        _4695,
        _4706,
        _4709,
        _4712,
        _4715,
        _4719,
        _4723,
        _4733,
        _4736,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysis")


class SpecialisedAssemblyModalAnalysis(_4593.AbstractAssemblyModalAnalysis):
    """SpecialisedAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysis")

    class _Cast_SpecialisedAssemblyModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            parent: "SpecialisedAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4599.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4603.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4606.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4611.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4612.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4616.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4621.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4624.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4627.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4633.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4635.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4637.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4643.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4652.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(_4652.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4654.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4658.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4662.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(
                _4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4669.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(
                _4669.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4672.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(
                _4672.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4686.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4688.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4695.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.RollingRingAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4706.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4709.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4712.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4715.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4719.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4723.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4733.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4733

            return self._parent._cast(_4733.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4736.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4736

            return self._parent._cast(_4736.ZerolBevelGearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "SpecialisedAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2827.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

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
    ) -> "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis":
        return self._Cast_SpecialisedAssemblyModalAnalysis(self)
