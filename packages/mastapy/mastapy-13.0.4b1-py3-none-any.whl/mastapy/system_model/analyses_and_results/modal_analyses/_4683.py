"""PartModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "PartModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4675,
        _4593,
        _4594,
        _4595,
        _4598,
        _4599,
        _4600,
        _4601,
        _4603,
        _4605,
        _4606,
        _4607,
        _4608,
        _4610,
        _4611,
        _4612,
        _4613,
        _4615,
        _4616,
        _4618,
        _4620,
        _4621,
        _4623,
        _4624,
        _4626,
        _4627,
        _4629,
        _4632,
        _4633,
        _4635,
        _4636,
        _4637,
        _4639,
        _4642,
        _4643,
        _4644,
        _4645,
        _4649,
        _4651,
        _4652,
        _4653,
        _4654,
        _4657,
        _4658,
        _4659,
        _4661,
        _4662,
        _4665,
        _4666,
        _4668,
        _4669,
        _4671,
        _4672,
        _4673,
        _4674,
        _4679,
        _4681,
        _4685,
        _4686,
        _4688,
        _4689,
        _4690,
        _4691,
        _4692,
        _4693,
        _4695,
        _4697,
        _4698,
        _4699,
        _4700,
        _4703,
        _4705,
        _4706,
        _4708,
        _4709,
        _4711,
        _4712,
        _4714,
        _4715,
        _4716,
        _4717,
        _4718,
        _4719,
        _4720,
        _4721,
        _4723,
        _4724,
        _4725,
        _4726,
        _4727,
        _4732,
        _4733,
        _4735,
        _4736,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4747,
        _4745,
        _4748,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2806
    from mastapy.system_model.drawing import _2271
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartModalAnalysis",)


Self = TypeVar("Self", bound="PartModalAnalysis")


class PartModalAnalysis(_7569.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartModalAnalysis")

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
            parent: "PartModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4594.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4595.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4598.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4599.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4600.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4601.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4603.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4605.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4606.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4607.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4608.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4610.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4611.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4612.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4613.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4615.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4616.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4620.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4621.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4623.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4624.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4626.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4627.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4629.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4632.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4633.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4635.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4636.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4637.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4639.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4642.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(_4642.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4643.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4644.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4645.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4649.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4651.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4652.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(_4652.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4653.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4654.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4657.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4658.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4659.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4661.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4662.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4665.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(
                _4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4668.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4669.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(
                _4669.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4672.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(
                _4672.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4673.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4674.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4681.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4685.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4686.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4688.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4689.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4690.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4691.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4692.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4693.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4695.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4697.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4698.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4699.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4700.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4705.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4706.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4708.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4709.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4711.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4712.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4714.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4715.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4716.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4717.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4718.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4719.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4720.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4721.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4721

            return self._parent._cast(_4721.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4723.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4724.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4724

            return self._parent._cast(_4724.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4725.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4726.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4727.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4732.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4732

            return self._parent._cast(_4732.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4733.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4733

            return self._parent._cast(_4733.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4735.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4736.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4736

            return self._parent._cast(_4736.ZerolBevelGearSetModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "PartModalAnalysis":
            return self._parent

        def __getattr__(self: "PartModalAnalysis._Cast_PartModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2488.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis(self: Self) -> "_4675.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: Self,
    ) -> "List[_4747.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_excitation_details(
        self: Self,
    ) -> "List[_4745.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_modes(self: Self) -> "List[_4748.SingleModeResults]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleModeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_excitation_details(
        self: Self,
    ) -> "List[_4745.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2806.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2271.ModalAnalysisViewable":
        """mastapy.system_model.drawing.ModalAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartModalAnalysis._Cast_PartModalAnalysis":
        return self._Cast_PartModalAnalysis(self)
