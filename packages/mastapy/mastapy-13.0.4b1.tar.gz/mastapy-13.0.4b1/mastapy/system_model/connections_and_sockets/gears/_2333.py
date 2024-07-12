"""GearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _953
    from mastapy.system_model.connections_and_sockets.gears import (
        _2319,
        _2321,
        _2323,
        _2325,
        _2327,
        _2329,
        _2331,
        _2335,
        _2338,
        _2339,
        _2340,
        _2343,
        _2345,
        _2347,
        _2349,
        _2351,
    )
    from mastapy.system_model.connections_and_sockets import _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("GearMesh",)


Self = TypeVar("Self", bound="GearMesh")


class GearMesh(_2301.InterMountableComponentConnection):
    """GearMesh

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMesh")

    class _Cast_GearMesh:
        """Special nested class for casting GearMesh to subclasses."""

        def __init__(self: "GearMesh._Cast_GearMesh", parent: "GearMesh"):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(self: "GearMesh._Cast_GearMesh") -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(self: "GearMesh._Cast_GearMesh") -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2321.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self: "GearMesh._Cast_GearMesh") -> "_2323.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2325.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2329.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "GearMesh._Cast_GearMesh") -> "_2331.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.FaceGearMesh)

        @property
        def hypoid_gear_mesh(self: "GearMesh._Cast_GearMesh") -> "_2335.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2339.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2343.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2345.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2347.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "GearMesh._Cast_GearMesh") -> "_2349.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "GearMesh._Cast_GearMesh",
        ) -> "_2351.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2351

            return self._parent._cast(_2351.ZerolBevelGearMesh)

        @property
        def gear_mesh(self: "GearMesh._Cast_GearMesh") -> "GearMesh":
            return self._parent

        def __getattr__(self: "GearMesh._Cast_GearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mesh_efficiency.setter
    @enforce_parameter_types
    def mesh_efficiency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MeshEfficiency = value

    @property
    def use_specified_mesh_stiffness(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSpecifiedMeshStiffness

        if temp is None:
            return False

        return temp

    @use_specified_mesh_stiffness.setter
    @enforce_parameter_types
    def use_specified_mesh_stiffness(self: Self, value: "bool"):
        self.wrapped.UseSpecifiedMeshStiffness = (
            bool(value) if value is not None else False
        )

    @property
    def user_specified_mesh_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedMeshStiffness

        if temp is None:
            return 0.0

        return temp

    @user_specified_mesh_stiffness.setter
    @enforce_parameter_types
    def user_specified_mesh_stiffness(self: Self, value: "float"):
        self.wrapped.UserSpecifiedMeshStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def active_gear_mesh_design(self: Self) -> "_953.GearMeshDesign":
        """mastapy.gears.gear_designs.GearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMesh._Cast_GearMesh":
        return self._Cast_GearMesh(self)
