"""PartParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1879, _1887, _1885
    from mastapy.system_model.part_model import _2488
    from mastapy.utility_gui import _1870
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4409,
        _4317,
        _4318,
        _4319,
        _4322,
        _4323,
        _4324,
        _4325,
        _4327,
        _4329,
        _4330,
        _4331,
        _4332,
        _4334,
        _4335,
        _4336,
        _4337,
        _4339,
        _4340,
        _4342,
        _4344,
        _4345,
        _4347,
        _4348,
        _4350,
        _4351,
        _4353,
        _4355,
        _4356,
        _4358,
        _4359,
        _4360,
        _4362,
        _4365,
        _4366,
        _4367,
        _4368,
        _4376,
        _4378,
        _4379,
        _4380,
        _4381,
        _4383,
        _4384,
        _4385,
        _4387,
        _4388,
        _4391,
        _4392,
        _4394,
        _4395,
        _4397,
        _4398,
        _4399,
        _4400,
        _4402,
        _4403,
        _4416,
        _4417,
        _4419,
        _4420,
        _4421,
        _4422,
        _4423,
        _4424,
        _4426,
        _4428,
        _4429,
        _4430,
        _4431,
        _4433,
        _4435,
        _4436,
        _4438,
        _4439,
        _4441,
        _4442,
        _4444,
        _4445,
        _4446,
        _4447,
        _4448,
        _4449,
        _4450,
        _4451,
        _4453,
        _4454,
        _4455,
        _4456,
        _4457,
        _4459,
        _4460,
        _4462,
        _4463,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartParametricStudyTool",)


Self = TypeVar("Self", bound="PartParametricStudyTool")


class PartParametricStudyTool(_7566.PartAnalysisCase):
    """PartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartParametricStudyTool")

    class _Cast_PartParametricStudyTool:
        """Special nested class for casting PartParametricStudyTool to subclasses."""

        def __init__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
            parent: "PartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4318.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4319.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4322.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4323.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(
                _4323.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4324.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4325.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4327.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4329.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4330.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4331.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(
                _4331.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4332.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4334.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4335.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4336.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4337.BoltParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4339.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4340.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4342.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4344.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4345.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4347.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4348.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4348,
            )

            return self._parent._cast(_4348.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4350.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4350,
            )

            return self._parent._cast(_4350.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4351.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4351,
            )

            return self._parent._cast(_4351.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4353.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4355.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4356.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4358.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4359.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4360.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4362.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4365.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4366.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4367.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4368.DatumParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(_4368.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4376.ExternalCADModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(_4376.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4378.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4379.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4380.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4381.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4383.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4384.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4385.GuideDxfModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4387.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4387,
            )

            return self._parent._cast(_4387.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4388.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4388,
            )

            return self._parent._cast(_4388.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4391.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(
                _4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4394.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4397.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(
                _4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4399.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4400.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4402.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4403.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4416.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(
                _4416.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4417.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4419.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4420.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4421.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4422.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4423.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4424.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4426.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4428.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4429.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4430.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4431.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4435.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4436.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4438.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4439.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4441.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4442.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4444.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4445.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4445,
            )

            return self._parent._cast(_4445.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4446.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4447.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4447,
            )

            return self._parent._cast(_4447.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4448.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4448,
            )

            return self._parent._cast(_4448.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4449.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4450.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4450,
            )

            return self._parent._cast(_4450.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4451.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4451,
            )

            return self._parent._cast(_4451.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4453.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4453,
            )

            return self._parent._cast(_4453.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4454.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4454,
            )

            return self._parent._cast(_4454.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4455.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4455,
            )

            return self._parent._cast(_4455.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4456.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4456,
            )

            return self._parent._cast(_4456.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4457.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4457,
            )

            return self._parent._cast(_4457.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4459.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4459,
            )

            return self._parent._cast(_4459.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4460.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4460,
            )

            return self._parent._cast(_4460.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4462.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4462,
            )

            return self._parent._cast(_4462.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4463.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4463,
            )

            return self._parent._cast(_4463.ZerolBevelGearSetParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "PartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_of_experiments_chart(self: Self) -> "_1879.NDChartDefinition":
        """mastapy.utility_gui.charts.NDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignOfExperimentsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_2d(self: Self) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart2D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_3d(self: Self) -> "_1885.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def data_logger(self: Self) -> "_1870.DataLoggerWithCharts":
        """mastapy.utility_gui.DataLoggerWithCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool(self: Self) -> "_4409.ParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartParametricStudyTool._Cast_PartParametricStudyTool":
        return self._Cast_PartParametricStudyTool(self)
