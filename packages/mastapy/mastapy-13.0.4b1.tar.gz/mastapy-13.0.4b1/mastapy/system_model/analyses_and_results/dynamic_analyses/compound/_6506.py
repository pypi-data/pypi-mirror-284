"""MountableComponentCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "MountableComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6433,
        _6437,
        _6440,
        _6443,
        _6444,
        _6445,
        _6452,
        _6457,
        _6458,
        _6461,
        _6465,
        _6468,
        _6471,
        _6476,
        _6479,
        _6482,
        _6487,
        _6491,
        _6495,
        _6498,
        _6501,
        _6504,
        _6505,
        _6507,
        _6511,
        _6514,
        _6515,
        _6516,
        _6517,
        _6518,
        _6521,
        _6525,
        _6528,
        _6533,
        _6534,
        _6537,
        _6540,
        _6541,
        _6543,
        _6544,
        _6545,
        _6548,
        _6549,
        _6550,
        _6551,
        _6552,
        _6555,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundDynamicAnalysis")


class MountableComponentCompoundDynamicAnalysis(_6454.ComponentCompoundDynamicAnalysis):
    """MountableComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundDynamicAnalysis"
    )

    class _Cast_MountableComponentCompoundDynamicAnalysis:
        """Special nested class for casting MountableComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
            parent: "MountableComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6433.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(
                _6433.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bearing_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6437.BearingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.BearingCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6440.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(
                _6440.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6443.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(
                _6443.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6444.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(
                _6444.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6445.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.BevelGearCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6452.ClutchHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.ClutchHalfCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6457.ConceptCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6458.ConceptGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.ConceptGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6461.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.ConicalGearCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6465.ConnectorCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6468.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6471.CVTPulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6476.CylindricalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(_6476.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6479.CylindricalPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def face_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6482.FaceGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.FaceGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6487.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.GearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6491.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6495.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(
                _6495.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6498.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6501.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6504.MassDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6505.MeasurementComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6507.OilSealCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(_6507.OilSealCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6511.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6514.PlanetCarrierCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6515.PointLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(_6515.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6516.PowerLoadCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6517.PulleyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6518.RingPinsCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6521.RollingRingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.RollingRingCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6525.ShaftHubConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6528.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6533.SpringDamperHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6534.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(
                _6534.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6537.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6537,
            )

            return self._parent._cast(_6537.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6541.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6541,
            )

            return self._parent._cast(_6541.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6543.SynchroniserHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(_6543.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6544.SynchroniserPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6544,
            )

            return self._parent._cast(_6544.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6545.SynchroniserSleeveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6545,
            )

            return self._parent._cast(_6545.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6548.TorqueConverterPumpCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6548,
            )

            return self._parent._cast(_6548.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6549.TorqueConverterTurbineCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6549,
            )

            return self._parent._cast(
                _6549.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6550.UnbalancedMassCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6550,
            )

            return self._parent._cast(_6550.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6551.VirtualComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6551,
            )

            return self._parent._cast(_6551.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6552.WormGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6552,
            )

            return self._parent._cast(_6552.WormGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "_6555.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6555,
            )

            return self._parent._cast(_6555.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
        ) -> "MountableComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6377.MountableComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis]

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
    ) -> "List[_6377.MountableComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis]

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
    ) -> "MountableComponentCompoundDynamicAnalysis._Cast_MountableComponentCompoundDynamicAnalysis":
        return self._Cast_MountableComponentCompoundDynamicAnalysis(self)
