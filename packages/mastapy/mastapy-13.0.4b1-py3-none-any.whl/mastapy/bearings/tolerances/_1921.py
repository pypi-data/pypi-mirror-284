"""BearingConnectionComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_CONNECTION_COMPONENT = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "BearingConnectionComponent"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import (
        _1926,
        _1927,
        _1928,
        _1929,
        _1931,
        _1932,
        _1933,
        _1934,
        _1937,
        _1940,
        _1942,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingConnectionComponent",)


Self = TypeVar("Self", bound="BearingConnectionComponent")


class BearingConnectionComponent(_0.APIBase):
    """BearingConnectionComponent

    This is a mastapy class.
    """

    TYPE = _BEARING_CONNECTION_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingConnectionComponent")

    class _Cast_BearingConnectionComponent:
        """Special nested class for casting BearingConnectionComponent to subclasses."""

        def __init__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            parent: "BearingConnectionComponent",
        ):
            self._parent = parent

        @property
        def inner_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1926.InnerRingTolerance":
            from mastapy.bearings.tolerances import _1926

            return self._parent._cast(_1926.InnerRingTolerance)

        @property
        def inner_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1927.InnerSupportTolerance":
            from mastapy.bearings.tolerances import _1927

            return self._parent._cast(_1927.InnerSupportTolerance)

        @property
        def interference_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1928.InterferenceDetail":
            from mastapy.bearings.tolerances import _1928

            return self._parent._cast(_1928.InterferenceDetail)

        @property
        def interference_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1929.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1929

            return self._parent._cast(_1929.InterferenceTolerance)

        @property
        def mounting_sleeve_diameter_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1931.MountingSleeveDiameterDetail":
            from mastapy.bearings.tolerances import _1931

            return self._parent._cast(_1931.MountingSleeveDiameterDetail)

        @property
        def outer_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1932.OuterRingTolerance":
            from mastapy.bearings.tolerances import _1932

            return self._parent._cast(_1932.OuterRingTolerance)

        @property
        def outer_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1933.OuterSupportTolerance":
            from mastapy.bearings.tolerances import _1933

            return self._parent._cast(_1933.OuterSupportTolerance)

        @property
        def race_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1934.RaceDetail":
            from mastapy.bearings.tolerances import _1934

            return self._parent._cast(_1934.RaceDetail)

        @property
        def ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1937.RingTolerance":
            from mastapy.bearings.tolerances import _1937

            return self._parent._cast(_1937.RingTolerance)

        @property
        def support_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1940.SupportDetail":
            from mastapy.bearings.tolerances import _1940

            return self._parent._cast(_1940.SupportDetail)

        @property
        def support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1942.SupportTolerance":
            from mastapy.bearings.tolerances import _1942

            return self._parent._cast(_1942.SupportTolerance)

        @property
        def bearing_connection_component(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "BearingConnectionComponent":
            return self._parent

        def __getattr__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingConnectionComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingConnectionComponent._Cast_BearingConnectionComponent":
        return self._Cast_BearingConnectionComponent(self)
