"""TorqueConverterPump"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.couplings import _2605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPump",)


Self = TypeVar("Self", bound="TorqueConverterPump")


class TorqueConverterPump(_2605.CouplingHalf):
    """TorqueConverterPump

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPump")

    class _Cast_TorqueConverterPump:
        """Special nested class for casting TorqueConverterPump to subclasses."""

        def __init__(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
            parent: "TorqueConverterPump",
        ):
            self._parent = parent

        @property
        def coupling_half(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "_2605.CouplingHalf":
            return self._parent._cast(_2605.CouplingHalf)

        @property
        def mountable_component(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "TorqueConverterPump._Cast_TorqueConverterPump") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def torque_converter_pump(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "TorqueConverterPump":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPump._Cast_TorqueConverterPump", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPump.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorqueConverterPump._Cast_TorqueConverterPump":
        return self._Cast_TorqueConverterPump(self)
