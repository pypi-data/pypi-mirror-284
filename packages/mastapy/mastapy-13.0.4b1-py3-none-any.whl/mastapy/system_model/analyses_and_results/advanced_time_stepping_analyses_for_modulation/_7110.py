"""MountableComponentAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.system_deflections import _2803
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7035,
        _7040,
        _7043,
        _7046,
        _7047,
        _7048,
        _7055,
        _7060,
        _7061,
        _7064,
        _7068,
        _7071,
        _7074,
        _7079,
        _7082,
        _7085,
        _7090,
        _7095,
        _7099,
        _7102,
        _7105,
        _7108,
        _7109,
        _7111,
        _7115,
        _7118,
        _7119,
        _7120,
        _7121,
        _7122,
        _7124,
        _7129,
        _7132,
        _7137,
        _7138,
        _7141,
        _7144,
        _7145,
        _7147,
        _7148,
        _7149,
        _7152,
        _7153,
        _7154,
        _7155,
        _7156,
        _7159,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentAdvancedTimeSteppingAnalysisForModulation(
    _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7043.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7046.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7047.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7055.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7060.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7061.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7064.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7068.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7074.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.FaceGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7102.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7105.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7105,
            )

            return self._parent._cast(
                _7105.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7108.MassDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7108,
            )

            return self._parent._cast(
                _7108.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7109.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7111.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7115.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7119.PointLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7120.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7121.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7122.RingPinsAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7124.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7132.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7141.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7141,
            )

            return self._parent._cast(
                _7141.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7144.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7144,
            )

            return self._parent._cast(
                _7144.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7145.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7145,
            )

            return self._parent._cast(
                _7145.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7147,
            )

            return self._parent._cast(
                _7147.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7148.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7148,
            )

            return self._parent._cast(
                _7148.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7149,
            )

            return self._parent._cast(
                _7149.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7152.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7152,
            )

            return self._parent._cast(
                _7152.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7153,
            )

            return self._parent._cast(
                _7153.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7154,
            )

            return self._parent._cast(
                _7154.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7155.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7155,
            )

            return self._parent._cast(
                _7155.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7156.WormGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7156,
            )

            return self._parent._cast(
                _7156.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7159,
            )

            return self._parent._cast(
                _7159.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MountableComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )
