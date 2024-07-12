"""Customer102ToleranceDefinition"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOMER_102_TOLERANCE_DEFINITION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Customer102ToleranceDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("Customer102ToleranceDefinition",)


Self = TypeVar("Self", bound="Customer102ToleranceDefinition")


class Customer102ToleranceDefinition(_0.APIBase):
    """Customer102ToleranceDefinition

    This is a mastapy class.
    """

    TYPE = _CUSTOMER_102_TOLERANCE_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Customer102ToleranceDefinition")

    class _Cast_Customer102ToleranceDefinition:
        """Special nested class for casting Customer102ToleranceDefinition to subclasses."""

        def __init__(
            self: "Customer102ToleranceDefinition._Cast_Customer102ToleranceDefinition",
            parent: "Customer102ToleranceDefinition",
        ):
            self._parent = parent

        @property
        def customer_102_tolerance_definition(
            self: "Customer102ToleranceDefinition._Cast_Customer102ToleranceDefinition",
        ) -> "Customer102ToleranceDefinition":
            return self._parent

        def __getattr__(
            self: "Customer102ToleranceDefinition._Cast_Customer102ToleranceDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Customer102ToleranceDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Max

        if temp is None:
            return 0.0

        return temp

    @max.setter
    @enforce_parameter_types
    def max(self: Self, value: "float"):
        self.wrapped.Max = float(value) if value is not None else 0.0

    @property
    def min(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Min

        if temp is None:
            return 0.0

        return temp

    @min.setter
    @enforce_parameter_types
    def min(self: Self, value: "float"):
        self.wrapped.Min = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def spread(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Spread

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @spread.setter
    @enforce_parameter_types
    def spread(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Spread = value

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
    def cast_to(
        self: Self,
    ) -> "Customer102ToleranceDefinition._Cast_Customer102ToleranceDefinition":
        return self._Cast_Customer102ToleranceDefinition(self)
