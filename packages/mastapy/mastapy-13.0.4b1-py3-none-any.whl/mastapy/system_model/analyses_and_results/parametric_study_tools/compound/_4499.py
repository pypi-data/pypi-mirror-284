"""ConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1870
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4467,
        _4469,
        _4473,
        _4476,
        _4481,
        _4486,
        _4488,
        _4491,
        _4494,
        _4497,
        _4502,
        _4504,
        _4508,
        _4510,
        _4512,
        _4518,
        _4523,
        _4527,
        _4529,
        _4531,
        _4534,
        _4537,
        _4545,
        _4547,
        _4554,
        _4557,
        _4561,
        _4564,
        _4567,
        _4570,
        _4573,
        _4582,
        _4588,
        _4591,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConnectionCompoundParametricStudyTool")


class ConnectionCompoundParametricStudyTool(_7560.ConnectionCompoundAnalysis):
    """ConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundParametricStudyTool"
    )

    class _Cast_ConnectionCompoundParametricStudyTool:
        """Special nested class for casting ConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
            parent: "ConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_7560.ConnectionCompoundAnalysis":
            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(
                _4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4473.BeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4476.BevelDifferentialGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(
                _4476.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4481.BevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4486.ClutchConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ClutchConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4488.CoaxialConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4491.ConceptCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(
                _4491.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4494.ConceptGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4497.ConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4502.CouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(
                _4502.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4504.CVTBeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(
                _4504.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4510.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4512.CylindricalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4518.FaceGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4523.GearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4527.HypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4529.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(
                _4529.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4531.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(
                _4531.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4534.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4537.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4545.PartToPartShearCouplingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4547.PlanetaryConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4554.RingPinsToDiscConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.RingPinsToDiscConnectionCompoundParametricStudyTool
            )

        @property
        def rolling_ring_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4557.RollingRingConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(
                _4557.RollingRingConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4564.SpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(
                _4564.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4567.SpringDamperConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4570.StraightBevelDiffGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4573.StraightBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(
                _4573.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4582.TorqueConverterConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4582,
            )

            return self._parent._cast(
                _4582.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4588.WormGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4588,
            )

            return self._parent._cast(_4588.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "_4591.ZerolBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4591,
            )

            return self._parent._cast(
                _4591.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
        ) -> "ConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConnectionCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4352.ConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4352.ConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCompoundParametricStudyTool._Cast_ConnectionCompoundParametricStudyTool":
        return self._Cast_ConnectionCompoundParametricStudyTool(self)
