"""AGMAGleasonConicalGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4328,
        _4333,
        _4386,
        _4434,
        _4440,
        _4443,
        _4461,
        _4382,
        _4389,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshParametricStudyTool")


class AGMAGleasonConicalGearMeshParametricStudyTool(
    _4349.ConicalGearMeshParametricStudyTool
):
    """AGMAGleasonConicalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearMeshParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
            parent: "AGMAGleasonConicalGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4349.ConicalGearMeshParametricStudyTool":
            return self._parent._cast(_4349.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4382.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4382,
            )

            return self._parent._cast(_4382.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4328.BevelDifferentialGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(
                _4328.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4333.BevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.BevelGearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4386.HypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.HypoidGearMeshParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4434.SpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.SpiralBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4440.StraightBevelDiffGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(
                _4440.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4443.StraightBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4443,
            )

            return self._parent._cast(_4443.StraightBevelGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "_4461.ZerolBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4461,
            )

            return self._parent._cast(_4461.ZerolBevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
        ) -> "AGMAGleasonConicalGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshParametricStudyTool._Cast_AGMAGleasonConicalGearMeshParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearMeshParametricStudyTool(self)
