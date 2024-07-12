"""PartLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6919, _6826
from mastapy.system_model.analyses_and_results import _2678
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6827,
        _6828,
        _6829,
        _6830,
        _6835,
        _6837,
        _6840,
        _6841,
        _6843,
        _6844,
        _6846,
        _6847,
        _6848,
        _6849,
        _6851,
        _6852,
        _6853,
        _6855,
        _6856,
        _6859,
        _6861,
        _6862,
        _6863,
        _6865,
        _6866,
        _6870,
        _6872,
        _6874,
        _6875,
        _6877,
        _6878,
        _6879,
        _6881,
        _6883,
        _6887,
        _6888,
        _6891,
        _6905,
        _6906,
        _6908,
        _6909,
        _6910,
        _6912,
        _6917,
        _6918,
        _6927,
        _6929,
        _6934,
        _6936,
        _6937,
        _6939,
        _6940,
        _6942,
        _6943,
        _6944,
        _6946,
        _6948,
        _6952,
        _6953,
        _6955,
        _6957,
        _6960,
        _6961,
        _6962,
        _6965,
        _6967,
        _6969,
        _6970,
        _6971,
        _6972,
        _6974,
        _6975,
        _6977,
        _6979,
        _6980,
        _6981,
        _6983,
        _6984,
        _6986,
        _6987,
        _6988,
        _6989,
        _6990,
        _6991,
        _6992,
        _6995,
        _6996,
        _6997,
        _7002,
        _7003,
        _7004,
        _7006,
        _7007,
        _7009,
    )
    from mastapy.electric_machines.harmonic_load_data import _1398
    from mastapy.system_model.analyses_and_results import _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartLoadCase",)


Self = TypeVar("Self", bound="PartLoadCase")


class PartLoadCase(_2678.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartLoadCase")

    class _Cast_PartLoadCase:
        """Special nested class for casting PartLoadCase to subclasses."""

        def __init__(self: "PartLoadCase._Cast_PartLoadCase", parent: "PartLoadCase"):
            self._parent = parent

        @property
        def part_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2678.PartAnalysis":
            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6829.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6830.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6835.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6837.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6840.AssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AssemblyLoadCase)

        @property
        def bearing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6841.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.BearingLoadCase)

        @property
        def belt_drive_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6843.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6844.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6846.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6847.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6848.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6849.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6851.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6852.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BoltedJointLoadCase)

        @property
        def bolt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6853.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6855.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ClutchHalfLoadCase)

        @property
        def clutch_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6856.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.ClutchLoadCase)

        @property
        def component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6861.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6862.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6863.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6865.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6870.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConicalGearSetLoadCase)

        @property
        def connector_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6872.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6874.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.CouplingHalfLoadCase)

        @property
        def coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6875.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6877.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(_6877.CVTLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6878.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6879.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6879

            return self._parent._cast(_6879.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6881.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6883.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6887.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6888.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6891.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6905.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6906.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6906

            return self._parent._cast(_6906.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6908.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6909.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6910.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6917.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6918.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(_6918.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6927.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6929.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6934.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6936.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(
                _6936.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(
                _6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(
                _6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(
                _6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6943.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6944.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6948.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6952.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6953.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6955.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6957.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6960.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6961.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6962.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6965.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6967.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6969.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.RollingRingLoadCase)

        @property
        def root_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6970.RootAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6971.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6972.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6975.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6977.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6979.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6980.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6981.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6983.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6984.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6986.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6987.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6988.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6989.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6990.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6991.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6992.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6995.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6996.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6997.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7002.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7002

            return self._parent._cast(_7002.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7003.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7003

            return self._parent._cast(_7003.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7004.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7004

            return self._parent._cast(_7004.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7006.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7006

            return self._parent._cast(_7006.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7007.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7009.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.ZerolBevelGearSetLoadCase)

        @property
        def part_load_case(self: "PartLoadCase._Cast_PartLoadCase") -> "PartLoadCase":
            return self._parent

        def __getattr__(self: "PartLoadCase._Cast_PartLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]"""
        temp = self.wrapped.HarmonicExcitationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @harmonic_excitation_type.setter
    @enforce_parameter_types
    def harmonic_excitation_type(self: Self, value: "_6919.HarmonicExcitationType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HarmonicExcitationType = value

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = (
            self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "_6826.StaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            value
        )

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "bool"
    ):
        self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            bool(value) if value is not None else False
        )

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
    def static_load_case(self: Self) -> "_6826.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6827.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_this_load_case(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForThisLoadCase()

    def get_harmonic_load_data_for_import(self: Self) -> "_1398.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartLoadCase._Cast_PartLoadCase":
        return self._Cast_PartLoadCase(self)
