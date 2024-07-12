"""ComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6829,
        _6830,
        _6835,
        _6841,
        _6844,
        _6847,
        _6848,
        _6849,
        _6853,
        _6855,
        _6861,
        _6863,
        _6866,
        _6872,
        _6874,
        _6878,
        _6881,
        _6883,
        _6888,
        _6891,
        _6905,
        _6906,
        _6909,
        _6912,
        _6918,
        _6927,
        _6934,
        _6937,
        _6940,
        _6943,
        _6944,
        _6946,
        _6948,
        _6952,
        _6957,
        _6960,
        _6961,
        _6962,
        _6965,
        _6969,
        _6971,
        _6972,
        _6975,
        _6979,
        _6981,
        _6984,
        _6987,
        _6988,
        _6989,
        _6991,
        _6992,
        _6996,
        _6997,
        _7002,
        _7003,
        _7004,
        _7007,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentLoadCase",)


Self = TypeVar("Self", bound="ComponentLoadCase")


class ComponentLoadCase(_6950.PartLoadCase):
    """ComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentLoadCase")

    class _Cast_ComponentLoadCase:
        """Special nested class for casting ComponentLoadCase to subclasses."""

        def __init__(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
            parent: "ComponentLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6950.PartLoadCase":
            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6829.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6830.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6835.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6841.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6844.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6847.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6848.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6849.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelGearLoadCase)

        @property
        def bolt_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6853.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6855.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6861.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6863.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6872.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6874.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6878.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.CVTPulleyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6881.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6883.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6888.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6891.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6905.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6906.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6906

            return self._parent._cast(_6906.FaceGearLoadCase)

        @property
        def fe_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6909.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.FEPartLoadCase)

        @property
        def gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6918.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(_6918.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6927.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6934.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(
                _6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6943.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6944.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6948.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6952.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6957.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6960.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6961.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6962.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6965.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6969.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6971.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6972.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.ShaftLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6975.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6979.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6981.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6984.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6987.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6988.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6989.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6991.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6992.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6996.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6997.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_7002.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7002

            return self._parent._cast(_7002.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_7003.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7003

            return self._parent._cast(_7003.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_7004.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7004

            return self._parent._cast(_7004.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_7007.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.ZerolBevelGearLoadCase)

        @property
        def component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "ComponentLoadCase":
            return self._parent

        def __getattr__(self: "ComponentLoadCase._Cast_ComponentLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def is_connected_to_ground(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsConnectedToGround

        if temp is None:
            return False

        return temp

    @property
    def is_torsionally_free(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTorsionallyFree

        if temp is None:
            return False

        return temp

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2464.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentLoadCase._Cast_ComponentLoadCase":
        return self._Cast_ComponentLoadCase(self)
