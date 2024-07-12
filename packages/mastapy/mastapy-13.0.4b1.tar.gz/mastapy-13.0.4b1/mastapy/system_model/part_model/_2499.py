"""VirtualComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2484
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2482,
        _2483,
        _2491,
        _2492,
        _2497,
        _2464,
        _2488,
    )
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponent",)


Self = TypeVar("Self", bound="VirtualComponent")


class VirtualComponent(_2484.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponent")

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(
            self: "VirtualComponent._Cast_VirtualComponent", parent: "VirtualComponent"
        ):
            self._parent = parent

        @property
        def mountable_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2484.MountableComponent":
            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "VirtualComponent._Cast_VirtualComponent") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def mass_disc(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2482.MassDisc":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MassDisc)

        @property
        def measurement_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2483.MeasurementComponent":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.MeasurementComponent)

        @property
        def point_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2491.PointLoad":
            from mastapy.system_model.part_model import _2491

            return self._parent._cast(_2491.PointLoad)

        @property
        def power_load(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2492.PowerLoad":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.PowerLoad)

        @property
        def unbalanced_mass(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "_2497.UnbalancedMass":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.UnbalancedMass)

        @property
        def virtual_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "VirtualComponent":
            return self._parent

        def __getattr__(self: "VirtualComponent._Cast_VirtualComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "VirtualComponent._Cast_VirtualComponent":
        return self._Cast_VirtualComponent(self)
