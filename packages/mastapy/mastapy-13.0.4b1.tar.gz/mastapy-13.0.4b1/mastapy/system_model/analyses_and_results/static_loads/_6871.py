"""ConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6826,
        _6827,
        _6831,
        _6836,
        _6842,
        _6845,
        _6850,
        _6854,
        _6858,
        _6860,
        _6864,
        _6868,
        _6873,
        _6876,
        _6880,
        _6882,
        _6885,
        _6907,
        _6914,
        _6928,
        _6933,
        _6935,
        _6938,
        _6941,
        _6951,
        _6954,
        _6966,
        _6968,
        _6973,
        _6976,
        _6978,
        _6982,
        _6985,
        _6994,
        _7005,
        _7008,
    )
    from mastapy.system_model.analyses_and_results import _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionLoadCase",)


Self = TypeVar("Self", bound="ConnectionLoadCase")


class ConnectionLoadCase(_2670.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionLoadCase")

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
            parent: "ConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6831.AbstractShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(
                _6831.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6836.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6842.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6845.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6850.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6854.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6858.CoaxialConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6860.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6864.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6868.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6873.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6876.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6880.CycloidalDiscCentralBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(
                _6880.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6882.CycloidalDiscPlanetaryBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(
                _6882.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6885.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6907.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6914.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6928.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(
                _6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(
                _6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6954.PlanetaryConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6966.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6968.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6973.ShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6976.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6978.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6982.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6985.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6994.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_7005.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7005

            return self._parent._cast(_7005.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_7008.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "ConnectionLoadCase":
            return self._parent

        def __getattr__(self: "ConnectionLoadCase._Cast_ConnectionLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2292.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2292.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_load_case(self: Self) -> "_6826.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6827.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionLoadCase._Cast_ConnectionLoadCase":
        return self._Cast_ConnectionLoadCase(self)
