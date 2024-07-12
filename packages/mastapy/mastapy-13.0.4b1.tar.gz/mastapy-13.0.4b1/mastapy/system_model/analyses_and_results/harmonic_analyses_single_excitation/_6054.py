"""ComponentHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6110,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6030,
        _6031,
        _6033,
        _6037,
        _6040,
        _6043,
        _6044,
        _6045,
        _6049,
        _6051,
        _6056,
        _6058,
        _6061,
        _6065,
        _6067,
        _6071,
        _6074,
        _6076,
        _6079,
        _6080,
        _6081,
        _6082,
        _6085,
        _6087,
        _6090,
        _6092,
        _6096,
        _6099,
        _6102,
        _6105,
        _6106,
        _6108,
        _6109,
        _6112,
        _6116,
        _6117,
        _6118,
        _6119,
        _6120,
        _6124,
        _6126,
        _6127,
        _6130,
        _6134,
        _6136,
        _6139,
        _6142,
        _6143,
        _6144,
        _6146,
        _6147,
        _6150,
        _6151,
        _6152,
        _6153,
        _6154,
        _6157,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ComponentHarmonicAnalysisOfSingleExcitation")


class ComponentHarmonicAnalysisOfSingleExcitation(
    _6110.PartHarmonicAnalysisOfSingleExcitation
):
    """ComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
            parent: "ComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6030.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(
                _6030.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(_6037.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(
                _6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(_6045.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.BoltHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6067.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.DatumHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(_6080.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6081.ExternalCADModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(_6082.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.FEPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(_6087.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6090.GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(
                _6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(_6105.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6109.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(_6109.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(_6117.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6118.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(_6118.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(_6119.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(_6120.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(_6126.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6127.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6150,
            )

            return self._parent._cast(
                _6150.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6151,
            )

            return self._parent._cast(
                _6151.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6153.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6153,
            )

            return self._parent._cast(
                _6153.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6154,
            )

            return self._parent._cast(_6154.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6157,
            )

            return self._parent._cast(
                _6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "ComponentHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ComponentHarmonicAnalysisOfSingleExcitation(self)
