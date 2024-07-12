"""SpecialisedAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpecialisedAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4323,
        _4327,
        _4330,
        _4335,
        _4336,
        _4340,
        _4345,
        _4348,
        _4351,
        _4356,
        _4358,
        _4360,
        _4366,
        _4379,
        _4381,
        _4384,
        _4388,
        _4392,
        _4395,
        _4398,
        _4417,
        _4419,
        _4426,
        _4436,
        _4439,
        _4442,
        _4445,
        _4449,
        _4453,
        _4460,
        _4463,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyParametricStudyTool")


class SpecialisedAssemblyParametricStudyTool(_4317.AbstractAssemblyParametricStudyTool):
    """SpecialisedAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
            parent: "SpecialisedAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4323.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(
                _4323.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def belt_drive_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4327.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4330.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4335.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4336.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4340.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4345.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4348.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4348,
            )

            return self._parent._cast(_4348.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4351.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4351,
            )

            return self._parent._cast(_4351.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4356.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4358.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4360.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4366.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4379.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4381.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4384.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4388.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4388,
            )

            return self._parent._cast(_4388.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(
                _4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(
                _4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4417.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4419.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4426.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.RollingRingAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4436.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4439.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4442.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4445.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4445,
            )

            return self._parent._cast(_4445.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4449.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4453.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4453,
            )

            return self._parent._cast(_4453.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4460.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4460,
            )

            return self._parent._cast(_4460.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "_4463.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4463,
            )

            return self._parent._cast(_4463.ZerolBevelGearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "SpecialisedAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2496.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool":
        return self._Cast_SpecialisedAssemblyParametricStudyTool(self)
