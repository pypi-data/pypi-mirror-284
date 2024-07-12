"""PowerLoadInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2492
from mastapy._internal import constructor
from mastapy.utility_gui import _1867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "PowerLoadInputOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7022,
        _7025,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadInputOptions",)


Self = TypeVar("Self", bound="PowerLoadInputOptions")


class PowerLoadInputOptions(_1867.ColumnInputOptions):
    """PowerLoadInputOptions

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadInputOptions")

    class _Cast_PowerLoadInputOptions:
        """Special nested class for casting PowerLoadInputOptions to subclasses."""

        def __init__(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions",
            parent: "PowerLoadInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions",
        ) -> "_1867.ColumnInputOptions":
            return self._parent._cast(_1867.ColumnInputOptions)

        @property
        def speed_input_options(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions",
        ) -> "_7022.SpeedInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7022,
            )

            return self._parent._cast(_7022.SpeedInputOptions)

        @property
        def torque_input_options(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions",
        ) -> "_7025.TorqueInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7025,
            )

            return self._parent._cast(_7025.TorqueInputOptions)

        @property
        def power_load_input_options(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions",
        ) -> "PowerLoadInputOptions":
            return self._parent

        def __getattr__(
            self: "PowerLoadInputOptions._Cast_PowerLoadInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.PowerLoad

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @power_load.setter
    @enforce_parameter_types
    def power_load(self: Self, value: "_2492.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.PowerLoad = value

    @property
    def cast_to(self: Self) -> "PowerLoadInputOptions._Cast_PowerLoadInputOptions":
        return self._Cast_PowerLoadInputOptions(self)
