"""ClutchHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.couplings import _2605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalf",)


Self = TypeVar("Self", bound="ClutchHalf")


class ClutchHalf(_2605.CouplingHalf):
    """ClutchHalf

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalf")

    class _Cast_ClutchHalf:
        """Special nested class for casting ClutchHalf to subclasses."""

        def __init__(self: "ClutchHalf._Cast_ClutchHalf", parent: "ClutchHalf"):
            self._parent = parent

        @property
        def coupling_half(self: "ClutchHalf._Cast_ClutchHalf") -> "_2605.CouplingHalf":
            return self._parent._cast(_2605.CouplingHalf)

        @property
        def mountable_component(
            self: "ClutchHalf._Cast_ClutchHalf",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(self: "ClutchHalf._Cast_ClutchHalf") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "ClutchHalf._Cast_ClutchHalf") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(self: "ClutchHalf._Cast_ClutchHalf") -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def clutch_half(self: "ClutchHalf._Cast_ClutchHalf") -> "ClutchHalf":
            return self._parent

        def __getattr__(self: "ClutchHalf._Cast_ClutchHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_mounted_on_shaft_outer(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMountedOnShaftOuter

        if temp is None:
            return False

        return temp

    @is_mounted_on_shaft_outer.setter
    @enforce_parameter_types
    def is_mounted_on_shaft_outer(self: Self, value: "bool"):
        self.wrapped.IsMountedOnShaftOuter = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "ClutchHalf._Cast_ClutchHalf":
        return self._Cast_ClutchHalf(self)
