"""InterMountableComponentConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6836,
        _6842,
        _6845,
        _6850,
        _6854,
        _6860,
        _6864,
        _6868,
        _6873,
        _6876,
        _6885,
        _6907,
        _6914,
        _6928,
        _6935,
        _6938,
        _6941,
        _6951,
        _6966,
        _6968,
        _6976,
        _6978,
        _6982,
        _6985,
        _6994,
        _7005,
        _7008,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionLoadCase")


class InterMountableComponentConnectionLoadCase(_6871.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionLoadCase"
    )

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
            parent: "InterMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6836.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6842.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6845.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6850.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6854.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6860.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6864.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6868.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6873.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6876.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6885.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6907.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6914.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6928.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(
                _6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(
                _6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6966.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6968.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6976.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6978.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6982.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6985.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6994.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_7005.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7005

            return self._parent._cast(_7005.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_7008.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "InterMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def connection_design(self: Self) -> "_2301.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase":
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
