"""VirtualComponentParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "VirtualComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4399,
        _4400,
        _4421,
        _4422,
        _4456,
        _4342,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentParametricStudyTool",)


Self = TypeVar("Self", bound="VirtualComponentParametricStudyTool")


class VirtualComponentParametricStudyTool(_4402.MountableComponentParametricStudyTool):
    """VirtualComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentParametricStudyTool")

    class _Cast_VirtualComponentParametricStudyTool:
        """Special nested class for casting VirtualComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
            parent: "VirtualComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4402.MountableComponentParametricStudyTool":
            return self._parent._cast(_4402.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4342.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4399.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4400.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.MeasurementComponentParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4421.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4422.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.PowerLoadParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "_4456.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4456,
            )

            return self._parent._cast(_4456.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "VirtualComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
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
        self: Self, instance_to_wrap: "VirtualComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> (
        "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool"
    ):
        return self._Cast_VirtualComponentParametricStudyTool(self)
