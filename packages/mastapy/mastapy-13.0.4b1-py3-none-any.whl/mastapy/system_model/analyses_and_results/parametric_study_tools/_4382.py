"""GearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "GearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4321,
        _4328,
        _4333,
        _4346,
        _4349,
        _4364,
        _4377,
        _4386,
        _4390,
        _4393,
        _4396,
        _4434,
        _4440,
        _4443,
        _4458,
        _4461,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="GearMeshParametricStudyTool")


class GearMeshParametricStudyTool(
    _4389.InterMountableComponentConnectionParametricStudyTool
):
    """GearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshParametricStudyTool")

    class _Cast_GearMeshParametricStudyTool:
        """Special nested class for casting GearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
            parent: "GearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4321.AGMAGleasonConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(
                _4321.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4328.BevelDifferentialGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(
                _4328.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4333.BevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.BevelGearMeshParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4346.ConceptGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4349.ConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4349,
            )

            return self._parent._cast(_4349.ConicalGearMeshParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4364.CylindricalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4377.FaceGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.FaceGearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4386.HypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.HypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4390.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(
                _4390.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4393.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(
                _4393.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4396.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(
                _4396.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4434.SpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.SpiralBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4440.StraightBevelDiffGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(
                _4440.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4443.StraightBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4443,
            )

            return self._parent._cast(_4443.StraightBevelGearMeshParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4458.WormGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4458,
            )

            return self._parent._cast(_4458.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "_4461.ZerolBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4461,
            )

            return self._parent._cast(_4461.ZerolBevelGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "GearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool":
        return self._Cast_GearMeshParametricStudyTool(self)
