"""MountableComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "MountableComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.modal_analyses import _4679
    from mastapy.system_model.analyses_and_results.system_deflections import _2803
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5704,
        _5708,
        _5711,
        _5714,
        _5715,
        _5716,
        _5722,
        _5728,
        _5730,
        _5733,
        _5737,
        _5739,
        _5743,
        _5748,
        _5751,
        _5768,
        _5774,
        _5792,
        _5796,
        _5799,
        _5802,
        _5805,
        _5806,
        _5808,
        _5811,
        _5816,
        _5817,
        _5818,
        _5819,
        _5821,
        _5825,
        _5828,
        _5833,
        _5837,
        _5840,
        _5843,
        _5846,
        _5847,
        _5848,
        _5850,
        _5851,
        _5854,
        _5855,
        _5857,
        _5858,
        _5859,
        _5862,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysis")


class MountableComponentHarmonicAnalysis(_5726.ComponentHarmonicAnalysis):
    """MountableComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentHarmonicAnalysis")

    class _Cast_MountableComponentHarmonicAnalysis:
        """Special nested class for casting MountableComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
            parent: "MountableComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5704.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5708.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5711.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5714.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5715.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5716.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelGearHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5722.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5728.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5730.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5733.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5737.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(_5737.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5739.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(_5739.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5743.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.CVTPulleyHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5748.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5751.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5768.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5768,
            )

            return self._parent._cast(_5768.FaceGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5774.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.GearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5792.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(
                _5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(
                _5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(
                _5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5805.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5806.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.MeasurementComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5808.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5811.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5816.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5817.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5818.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5819.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5821.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5825.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.RollingRingHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5828.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5833.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5837.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5840.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5843.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5846.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5847.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5848.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5850.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5851.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5854.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5854,
            )

            return self._parent._cast(_5854.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5855.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5857.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5857,
            )

            return self._parent._cast(_5857.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5858.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5858,
            )

            return self._parent._cast(_5858.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5859.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5859,
            )

            return self._parent._cast(_5859.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5862.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5862,
            )

            return self._parent._cast(_5862.ZerolBevelGearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "MountableComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4679.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2803.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

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
    ) -> "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis":
        return self._Cast_MountableComponentHarmonicAnalysis(self)
