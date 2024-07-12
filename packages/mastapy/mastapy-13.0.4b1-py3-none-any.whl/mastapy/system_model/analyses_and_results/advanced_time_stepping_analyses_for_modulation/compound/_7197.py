"""ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7067,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7165,
        _7167,
        _7171,
        _7174,
        _7179,
        _7184,
        _7186,
        _7189,
        _7192,
        _7195,
        _7200,
        _7202,
        _7206,
        _7208,
        _7210,
        _7216,
        _7221,
        _7225,
        _7227,
        _7229,
        _7232,
        _7235,
        _7243,
        _7245,
        _7252,
        _7255,
        _7259,
        _7262,
        _7265,
        _7268,
        _7271,
        _7280,
        _7286,
        _7289,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7560.ConnectionCompoundAnalysis
):
    """ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7171.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7189.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7192.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7202.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7210.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7210,
            )

            return self._parent._cast(
                _7210.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7216.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7225.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7229.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7232.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7235.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7243.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7243,
            )

            return self._parent._cast(
                _7243.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7252.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7255.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7262.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7265.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7268.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7271.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7271,
            )

            return self._parent._cast(
                _7271.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7280.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7280,
            )

            return self._parent._cast(
                _7280.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7286.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7286,
            )

            return self._parent._cast(
                _7286.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7289.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7289,
            )

            return self._parent._cast(
                _7289.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
