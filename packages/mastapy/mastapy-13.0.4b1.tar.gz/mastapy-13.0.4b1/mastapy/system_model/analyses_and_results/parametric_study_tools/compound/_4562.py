"""SpecialisedAssemblyCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4464,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpecialisedAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4433
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4470,
        _4474,
        _4477,
        _4482,
        _4484,
        _4485,
        _4490,
        _4495,
        _4498,
        _4501,
        _4505,
        _4507,
        _4513,
        _4519,
        _4521,
        _4524,
        _4528,
        _4532,
        _4535,
        _4538,
        _4544,
        _4548,
        _4555,
        _4565,
        _4566,
        _4571,
        _4574,
        _4577,
        _4581,
        _4589,
        _4592,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundParametricStudyTool")


class SpecialisedAssemblyCompoundParametricStudyTool(
    _4464.AbstractAssemblyCompoundParametricStudyTool
):
    """SpecialisedAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyCompoundParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
            parent: "SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4464.AbstractAssemblyCompoundParametricStudyTool":
            return self._parent._cast(_4464.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4470.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4474.BeltDriveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4477.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(
                _4477.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4482.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4484.BoltedJointCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4485.ClutchCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4490.ConceptCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4495.ConceptGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4498.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.ConicalGearSetCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4501.CouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.CouplingCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4505.CVTCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.CVTCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4507.CycloidalAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(
                _4507.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4513.CylindricalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4519.FaceGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.FaceGearSetCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4521.FlexiblePinAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4524.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.GearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4528.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4532.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(
                _4532.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4535.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4538.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4544.PartToPartShearCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4548.PlanetaryGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(_4548.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4555.RollingRingAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4565.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(
                _4565.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4566.SpringDamperCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.SpringDamperCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4571.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4574.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(
                _4574.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4577.SynchroniserCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(_4577.SynchroniserCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4581.TorqueConverterCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4581,
            )

            return self._parent._cast(_4581.TorqueConverterCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4589.WormGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4589,
            )

            return self._parent._cast(_4589.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "_4592.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4592,
            )

            return self._parent._cast(
                _4592.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "SpecialisedAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4433.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4433.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool":
        return self._Cast_SpecialisedAssemblyCompoundParametricStudyTool(self)
