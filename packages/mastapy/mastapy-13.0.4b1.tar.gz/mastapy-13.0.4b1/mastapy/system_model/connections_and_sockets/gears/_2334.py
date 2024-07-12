"""GearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2320,
        _2322,
        _2324,
        _2326,
        _2328,
        _2332,
        _2336,
        _2337,
        _2341,
        _2342,
        _2344,
        _2346,
        _2348,
        _2350,
        _2352,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearTeethSocket",)


Self = TypeVar("Self", bound="GearTeethSocket")


class GearTeethSocket(_2316.Socket):
    """GearTeethSocket

    This is a mastapy class.
    """

    TYPE = _GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearTeethSocket")

    class _Cast_GearTeethSocket:
        """Special nested class for casting GearTeethSocket to subclasses."""

        def __init__(
            self: "GearTeethSocket._Cast_GearTeethSocket", parent: "GearTeethSocket"
        ):
            self._parent = parent

        @property
        def socket(self: "GearTeethSocket._Cast_GearTeethSocket") -> "_2316.Socket":
            return self._parent._cast(_2316.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2320.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2322.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2324.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2326.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2332.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.FaceGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2336.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2337.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2341.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2342.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2342

            return self._parent._cast(_2342.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2344.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2344

            return self._parent._cast(_2344.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2346.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2346

            return self._parent._cast(_2346.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2348.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2348

            return self._parent._cast(_2348.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2350.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2350

            return self._parent._cast(_2350.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2352.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2352

            return self._parent._cast(_2352.ZerolBevelGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "GearTeethSocket":
            return self._parent

        def __getattr__(self: "GearTeethSocket._Cast_GearTeethSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearTeethSocket._Cast_GearTeethSocket":
        return self._Cast_GearTeethSocket(self)
