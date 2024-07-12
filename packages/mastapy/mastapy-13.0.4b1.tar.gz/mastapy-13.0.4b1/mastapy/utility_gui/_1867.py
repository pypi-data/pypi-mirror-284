"""ColumnInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.file_access_helpers import _1835
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements import _1628
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "ColumnInputOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
        _2575,
        _2576,
        _2577,
        _2580,
    )
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7011,
        _7012,
        _7014,
        _7015,
        _7016,
        _7017,
        _7019,
        _7020,
        _7021,
        _7022,
        _7024,
        _7025,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ColumnInputOptions",)


Self = TypeVar("Self", bound="ColumnInputOptions")


class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE = _COLUMN_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ColumnInputOptions")

    class _Cast_ColumnInputOptions:
        """Special nested class for casting ColumnInputOptions to subclasses."""

        def __init__(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
            parent: "ColumnInputOptions",
        ):
            self._parent = parent

        @property
        def boost_pressure_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2575.BoostPressureInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2575,
            )

            return self._parent._cast(_2575.BoostPressureInputOptions)

        @property
        def input_power_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2576.InputPowerInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2576,
            )

            return self._parent._cast(_2576.InputPowerInputOptions)

        @property
        def pressure_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2577.PressureRatioInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2577,
            )

            return self._parent._cast(_2577.PressureRatioInputOptions)

        @property
        def rotor_speed_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_2580.RotorSpeedInputOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2580,
            )

            return self._parent._cast(_2580.RotorSpeedInputOptions)

        @property
        def boost_pressure_load_case_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7011.BoostPressureLoadCaseInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7011,
            )

            return self._parent._cast(_7011.BoostPressureLoadCaseInputOptions)

        @property
        def design_state_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7012.DesignStateOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7012,
            )

            return self._parent._cast(_7012.DesignStateOptions)

        @property
        def force_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7014.ForceInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7014,
            )

            return self._parent._cast(_7014.ForceInputOptions)

        @property
        def gear_ratio_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7015.GearRatioInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7015,
            )

            return self._parent._cast(_7015.GearRatioInputOptions)

        @property
        def load_case_name_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7016.LoadCaseNameOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7016,
            )

            return self._parent._cast(_7016.LoadCaseNameOptions)

        @property
        def moment_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7017.MomentInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7017,
            )

            return self._parent._cast(_7017.MomentInputOptions)

        @property
        def point_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7019.PointLoadInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7019,
            )

            return self._parent._cast(_7019.PointLoadInputOptions)

        @property
        def power_load_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7020.PowerLoadInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7020,
            )

            return self._parent._cast(_7020.PowerLoadInputOptions)

        @property
        def ramp_or_steady_state_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7021.RampOrSteadyStateInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7021,
            )

            return self._parent._cast(_7021.RampOrSteadyStateInputOptions)

        @property
        def speed_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7022.SpeedInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7022,
            )

            return self._parent._cast(_7022.SpeedInputOptions)

        @property
        def time_step_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7024.TimeStepInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7024,
            )

            return self._parent._cast(_7024.TimeStepInputOptions)

        @property
        def torque_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "_7025.TorqueInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7025,
            )

            return self._parent._cast(_7025.TorqueInputOptions)

        @property
        def column_input_options(
            self: "ColumnInputOptions._Cast_ColumnInputOptions",
        ) -> "ColumnInputOptions":
            return self._parent

        def __getattr__(self: "ColumnInputOptions._Cast_ColumnInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ColumnInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ColumnTitle":
        """ListWithSelectedItem[mastapy.utility.file_access_helpers.ColumnTitle]"""
        temp = self.wrapped.Column

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ColumnTitle",
        )(temp)

    @column.setter
    @enforce_parameter_types
    def column(self: Self, value: "_1835.ColumnTitle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Column = value

    @property
    def unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.Unit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @unit.setter
    @enforce_parameter_types
    def unit(self: Self, value: "_1628.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Unit = value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "ColumnInputOptions._Cast_ColumnInputOptions":
        return self._Cast_ColumnInputOptions(self)
