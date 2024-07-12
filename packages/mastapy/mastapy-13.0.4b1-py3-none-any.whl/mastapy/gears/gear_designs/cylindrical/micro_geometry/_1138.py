"""ModificationForCustomer102CAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODIFICATION_FOR_CUSTOMER_102CAD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ModificationForCustomer102CAD",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1127, _1141


__docformat__ = "restructuredtext en"
__all__ = ("ModificationForCustomer102CAD",)


Self = TypeVar("Self", bound="ModificationForCustomer102CAD")


class ModificationForCustomer102CAD(_0.APIBase):
    """ModificationForCustomer102CAD

    This is a mastapy class.
    """

    TYPE = _MODIFICATION_FOR_CUSTOMER_102CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModificationForCustomer102CAD")

    class _Cast_ModificationForCustomer102CAD:
        """Special nested class for casting ModificationForCustomer102CAD to subclasses."""

        def __init__(
            self: "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD",
            parent: "ModificationForCustomer102CAD",
        ):
            self._parent = parent

        @property
        def lead_modification_for_customer_102cad(
            self: "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD",
        ) -> "_1127.LeadModificationForCustomer102CAD":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1127

            return self._parent._cast(_1127.LeadModificationForCustomer102CAD)

        @property
        def profile_modification_for_customer_102cad(
            self: "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD",
        ) -> "_1141.ProfileModificationForCustomer102CAD":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1141

            return self._parent._cast(_1141.ProfileModificationForCustomer102CAD)

        @property
        def modification_for_customer_102cad(
            self: "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD",
        ) -> "ModificationForCustomer102CAD":
            return self._parent

        def __getattr__(
            self: "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModificationForCustomer102CAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "ModificationForCustomer102CAD._Cast_ModificationForCustomer102CAD":
        return self._Cast_ModificationForCustomer102CAD(self)
