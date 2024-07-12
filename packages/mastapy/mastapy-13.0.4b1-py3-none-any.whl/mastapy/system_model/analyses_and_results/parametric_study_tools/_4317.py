"""AbstractAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4323,
        _4324,
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
        _4429,
        _4433,
        _4436,
        _4439,
        _4442,
        _4445,
        _4449,
        _4453,
        _4460,
        _4463,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractAssemblyParametricStudyTool")


class AbstractAssemblyParametricStudyTool(_4414.PartParametricStudyTool):
    """AbstractAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyParametricStudyTool")

    class _Cast_AbstractAssemblyParametricStudyTool:
        """Special nested class for casting AbstractAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
            parent: "AbstractAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4323.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(
                _4323.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4324.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.AssemblyParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4327.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4330.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4335.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4336.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4340.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4345.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4348.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4348,
            )

            return self._parent._cast(_4348.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4351.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4351,
            )

            return self._parent._cast(_4351.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4356.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4358.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4360.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4366.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4379.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4381.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4384.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4388.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4388,
            )

            return self._parent._cast(_4388.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(
                _4392.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(
                _4398.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4417.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4419.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4426.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.RollingRingAssemblyParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4429.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.RootAssemblyParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4436.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4439.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4442.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4445.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4445,
            )

            return self._parent._cast(_4445.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4449.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4453.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4453,
            )

            return self._parent._cast(_4453.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4460.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4460,
            )

            return self._parent._cast(_4460.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "_4463.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4463,
            )

            return self._parent._cast(_4463.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
        ) -> "AbstractAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> (
        "AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool"
    ):
        return self._Cast_AbstractAssemblyParametricStudyTool(self)
