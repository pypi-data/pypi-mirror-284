"""MountableComponentDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "MountableComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6302,
        _6306,
        _6309,
        _6312,
        _6313,
        _6314,
        _6321,
        _6326,
        _6327,
        _6330,
        _6334,
        _6337,
        _6340,
        _6345,
        _6348,
        _6353,
        _6358,
        _6362,
        _6366,
        _6369,
        _6372,
        _6375,
        _6376,
        _6378,
        _6382,
        _6385,
        _6386,
        _6387,
        _6388,
        _6389,
        _6393,
        _6396,
        _6399,
        _6404,
        _6405,
        _6408,
        _6411,
        _6412,
        _6414,
        _6415,
        _6416,
        _6419,
        _6420,
        _6421,
        _6422,
        _6423,
        _6426,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentDynamicAnalysis")


class MountableComponentDynamicAnalysis(_6323.ComponentDynamicAnalysis):
    """MountableComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentDynamicAnalysis")

    class _Cast_MountableComponentDynamicAnalysis:
        """Special nested class for casting MountableComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
            parent: "MountableComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6302.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6306.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.BearingDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6309.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6312.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6313.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6314.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.BevelGearDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6321.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6326.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6327.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.ConceptGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6330.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConicalGearDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6334.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.ConnectorDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6337.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.CouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6340.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.CVTPulleyDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6345.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6348.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.CylindricalPlanetGearDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6353.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.FaceGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6358.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.GearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6362.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6366.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(
                _6366.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6369.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(
                _6369.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6372.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(
                _6372.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6375.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6376.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.MeasurementComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6378.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6382.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6385.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6386.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6387.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6388.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6389.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6393.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.RollingRingDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6396.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.ShaftHubConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6399.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.SpiralBevelGearDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6404.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6405.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6408.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6411.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6411

            return self._parent._cast(_6411.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6412.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6414.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6415.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6416.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6419.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6420.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6420

            return self._parent._cast(_6420.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6421.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6422.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6422

            return self._parent._cast(_6422.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6423.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6423

            return self._parent._cast(_6423.WormGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6426.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426

            return self._parent._cast(_6426.ZerolBevelGearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "MountableComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentDynamicAnalysis.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis":
        return self._Cast_MountableComponentDynamicAnalysis(self)
