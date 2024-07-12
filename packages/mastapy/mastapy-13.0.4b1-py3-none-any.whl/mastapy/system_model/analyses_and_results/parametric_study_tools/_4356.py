"""CouplingParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4433
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4340,
        _4345,
        _4417,
        _4439,
        _4453,
        _4317,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingParametricStudyTool")


class CouplingParametricStudyTool(_4433.SpecialisedAssemblyParametricStudyTool):
    """CouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingParametricStudyTool")

    class _Cast_CouplingParametricStudyTool:
        """Special nested class for casting CouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            parent: "CouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4340.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4345.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.ConceptCouplingParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4417.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.PartToPartShearCouplingParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4439.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.SpringDamperParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "_4453.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4453,
            )

            return self._parent._cast(_4453.TorqueConverterParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "CouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool":
        return self._Cast_CouplingParametricStudyTool(self)
