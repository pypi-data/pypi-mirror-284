"""OuterRingTolerance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_RING_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "OuterRingTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1929, _1921


__docformat__ = "restructuredtext en"
__all__ = ("OuterRingTolerance",)


Self = TypeVar("Self", bound="OuterRingTolerance")


class OuterRingTolerance(_1937.RingTolerance):
    """OuterRingTolerance

    This is a mastapy class.
    """

    TYPE = _OUTER_RING_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterRingTolerance")

    class _Cast_OuterRingTolerance:
        """Special nested class for casting OuterRingTolerance to subclasses."""

        def __init__(
            self: "OuterRingTolerance._Cast_OuterRingTolerance",
            parent: "OuterRingTolerance",
        ):
            self._parent = parent

        @property
        def ring_tolerance(
            self: "OuterRingTolerance._Cast_OuterRingTolerance",
        ) -> "_1937.RingTolerance":
            return self._parent._cast(_1937.RingTolerance)

        @property
        def interference_tolerance(
            self: "OuterRingTolerance._Cast_OuterRingTolerance",
        ) -> "_1929.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1929

            return self._parent._cast(_1929.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "OuterRingTolerance._Cast_OuterRingTolerance",
        ) -> "_1921.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1921

            return self._parent._cast(_1921.BearingConnectionComponent)

        @property
        def outer_ring_tolerance(
            self: "OuterRingTolerance._Cast_OuterRingTolerance",
        ) -> "OuterRingTolerance":
            return self._parent

        def __getattr__(self: "OuterRingTolerance._Cast_OuterRingTolerance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterRingTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OuterRingTolerance._Cast_OuterRingTolerance":
        return self._Cast_OuterRingTolerance(self)
