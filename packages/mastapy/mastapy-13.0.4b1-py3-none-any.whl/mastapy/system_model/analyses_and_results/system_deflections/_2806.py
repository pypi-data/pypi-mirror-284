"""PartSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7568
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.math_utility import _1536
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2846,
        _2706,
        _2707,
        _2708,
        _2711,
        _2712,
        _2713,
        _2719,
        _2721,
        _2723,
        _2724,
        _2725,
        _2726,
        _2728,
        _2729,
        _2730,
        _2731,
        _2733,
        _2734,
        _2736,
        _2739,
        _2740,
        _2742,
        _2743,
        _2746,
        _2747,
        _2749,
        _2751,
        _2752,
        _2754,
        _2755,
        _2756,
        _2759,
        _2763,
        _2764,
        _2765,
        _2766,
        _2767,
        _2768,
        _2771,
        _2772,
        _2773,
        _2776,
        _2777,
        _2778,
        _2779,
        _2781,
        _2782,
        _2783,
        _2785,
        _2786,
        _2790,
        _2791,
        _2793,
        _2794,
        _2796,
        _2797,
        _2800,
        _2801,
        _2803,
        _2805,
        _2808,
        _2809,
        _2811,
        _2812,
        _2813,
        _2814,
        _2815,
        _2818,
        _2820,
        _2821,
        _2822,
        _2825,
        _2827,
        _2829,
        _2830,
        _2832,
        _2833,
        _2835,
        _2836,
        _2838,
        _2839,
        _2840,
        _2841,
        _2842,
        _2843,
        _2844,
        _2845,
        _2850,
        _2851,
        _2852,
        _2855,
        _2856,
        _2858,
        _2859,
        _2861,
        _2862,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.drawing import _2280
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartSystemDeflection",)


Self = TypeVar("Self", bound="PartSystemDeflection")


class PartSystemDeflection(_7568.PartFEAnalysis):
    """PartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartSystemDeflection")

    class _Cast_PartSystemDeflection:
        """Special nested class for casting PartSystemDeflection to subclasses."""

        def __init__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
            parent: "PartSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_fe_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2706.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2707.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2708.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2711.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2713.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2719.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2721.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2723.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2724.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2725.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2726.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2728.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2729.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2730.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2731.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2733.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2734.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2739.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2740.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2742.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2743.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2746.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2747.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2749.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2751.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2752.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2754.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2755.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2756.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2759.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2763.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2764.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2765.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2766.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2767.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2768.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2771.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(_2771.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2772.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(_2772.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2773.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2776.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(_2776.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2777.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2778.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2779.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2781.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2782.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2783.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2785.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2786.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2791.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(
                _2791.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2793.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2794.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(
                _2794.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2796.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2797.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(
                _2797.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2800.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2801.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2805.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2808.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2809.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2811.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2812.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2813.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2814.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2815.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2818.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2820.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2821.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2822.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2825.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2827.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2829.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2830.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2832.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2833.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2835.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2838.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2839.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2840.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2841.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2842.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2843.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2844.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2845.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2850.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2850,
            )

            return self._parent._cast(_2850.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2851.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2851,
            )

            return self._parent._cast(_2851.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2852.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2855.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2855,
            )

            return self._parent._cast(_2855.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2856.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2856,
            )

            return self._parent._cast(_2856.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2858.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2859.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2859,
            )

            return self._parent._cast(_2859.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2861.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2862.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "PartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingAxialForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

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
    def mass_properties_from_node_model(self: Self) -> "_1536.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection(self: Self) -> "_2846.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4135.PartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2280.SystemDeflectionViewable":
        """mastapy.system_model.drawing.SystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartSystemDeflection._Cast_PartSystemDeflection":
        return self._Cast_PartSystemDeflection(self)
