"""MountableComponentCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4489,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "MountableComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4468,
        _4472,
        _4475,
        _4478,
        _4479,
        _4480,
        _4487,
        _4492,
        _4493,
        _4496,
        _4500,
        _4503,
        _4506,
        _4511,
        _4514,
        _4517,
        _4522,
        _4526,
        _4530,
        _4533,
        _4536,
        _4539,
        _4540,
        _4542,
        _4546,
        _4549,
        _4550,
        _4551,
        _4552,
        _4553,
        _4556,
        _4560,
        _4563,
        _4568,
        _4569,
        _4572,
        _4575,
        _4576,
        _4578,
        _4579,
        _4580,
        _4583,
        _4584,
        _4585,
        _4586,
        _4587,
        _4590,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="MountableComponentCompoundParametricStudyTool")


class MountableComponentCompoundParametricStudyTool(
    _4489.ComponentCompoundParametricStudyTool
):
    """MountableComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundParametricStudyTool"
    )

    class _Cast_MountableComponentCompoundParametricStudyTool:
        """Special nested class for casting MountableComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
            parent: "MountableComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4468.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(
                _4468.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bearing_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4472.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.BearingCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4475.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(
                _4475.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4478.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(
                _4478.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4479.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(
                _4479.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4480.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.BevelGearCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4487.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4492.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(
                _4492.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4493.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(_4493.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4496.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.ConicalGearCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4500.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4503.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4506.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(_4506.CVTPulleyCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4511.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4514.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def face_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4517.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.FaceGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4522.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.GearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4526.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4530.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(
                _4530.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4533.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4536.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4539.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4540.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4542.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(_4542.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4546.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4549.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(_4549.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4550.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(_4550.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4551.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(_4551.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4552.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(_4552.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4553.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4556.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.RollingRingCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4560.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(
                _4560.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4563.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(_4563.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4568.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4569.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4569,
            )

            return self._parent._cast(
                _4569.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4572.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4572,
            )

            return self._parent._cast(
                _4572.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4575.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4575,
            )

            return self._parent._cast(
                _4575.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4576.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4576,
            )

            return self._parent._cast(
                _4576.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4578.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4578,
            )

            return self._parent._cast(_4578.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4579.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4579,
            )

            return self._parent._cast(_4579.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4580.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4580,
            )

            return self._parent._cast(
                _4580.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4583.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4583,
            )

            return self._parent._cast(
                _4583.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4584.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4584,
            )

            return self._parent._cast(
                _4584.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4585.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4585,
            )

            return self._parent._cast(_4585.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4586.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4586,
            )

            return self._parent._cast(_4586.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4587.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4587,
            )

            return self._parent._cast(_4587.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4590.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4590,
            )

            return self._parent._cast(_4590.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "MountableComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
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
        instance_to_wrap: "MountableComponentCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4402.MountableComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool]

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
    ) -> "List[_4402.MountableComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool]

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
    ) -> "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool":
        return self._Cast_MountableComponentCompoundParametricStudyTool(self)
