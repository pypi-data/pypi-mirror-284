"""ComponentCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4618
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4750,
        _4751,
        _4753,
        _4757,
        _4760,
        _4763,
        _4764,
        _4765,
        _4768,
        _4772,
        _4777,
        _4778,
        _4781,
        _4785,
        _4788,
        _4791,
        _4794,
        _4796,
        _4799,
        _4800,
        _4801,
        _4802,
        _4805,
        _4807,
        _4810,
        _4811,
        _4815,
        _4818,
        _4821,
        _4824,
        _4825,
        _4826,
        _4827,
        _4831,
        _4834,
        _4835,
        _4836,
        _4837,
        _4838,
        _4841,
        _4844,
        _4845,
        _4848,
        _4853,
        _4854,
        _4857,
        _4860,
        _4861,
        _4863,
        _4864,
        _4865,
        _4868,
        _4869,
        _4870,
        _4871,
        _4872,
        _4875,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundModalAnalysis")


class ComponentCompoundModalAnalysis(_4828.PartCompoundModalAnalysis):
    """ComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundModalAnalysis")

    class _Cast_ComponentCompoundModalAnalysis:
        """Special nested class for casting ComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
            parent: "ComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4750.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4751.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4753.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4757.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.BearingCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4760.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4763.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(
                _4763.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4764.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(
                _4764.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4765.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.BevelGearCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4768.BoltCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.BoltCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4772.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4777.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4778.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4781.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.ConicalGearCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4785.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.ConnectorCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4788.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4791.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4794.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4796.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(_4796.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4799.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(_4799.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4800.DatumCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4801.ExternalCADModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(_4801.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4802.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.FaceGearCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4805.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.FEPartCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4807.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.GearCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4810.GuideDxfModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(_4810.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4811.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4815.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(
                _4815.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4818.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(
                _4818.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4821.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(
                _4821.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4824.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4825.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4827.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4831.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(
                _4831.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planet_carrier_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4834.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4835.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4836.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4837.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4838.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4841.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.RollingRingCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4844.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4845.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4848.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4853.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4854.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(_4854.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4857.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(_4857.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4860.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4860,
            )

            return self._parent._cast(
                _4860.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4861.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4863.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4863,
            )

            return self._parent._cast(_4863.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4864.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4865.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4865,
            )

            return self._parent._cast(_4865.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4868.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4868,
            )

            return self._parent._cast(_4868.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4869.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4869,
            )

            return self._parent._cast(_4869.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4870.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4870,
            )

            return self._parent._cast(_4870.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4871.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4871,
            )

            return self._parent._cast(_4871.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4872.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4872,
            )

            return self._parent._cast(_4872.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4875.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4875,
            )

            return self._parent._cast(_4875.ZerolBevelGearCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "ComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4618.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4618.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis":
        return self._Cast_ComponentCompoundModalAnalysis(self)
