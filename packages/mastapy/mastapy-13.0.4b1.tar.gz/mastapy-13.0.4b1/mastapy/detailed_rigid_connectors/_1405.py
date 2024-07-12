"""DetailedRigidConnectorDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_RIGID_CONNECTOR_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors", "DetailedRigidConnectorDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1406
    from mastapy.detailed_rigid_connectors.splines import (
        _1408,
        _1411,
        _1415,
        _1418,
        _1419,
        _1426,
        _1433,
        _1438,
    )
    from mastapy.detailed_rigid_connectors.keyed_joints import _1455
    from mastapy.detailed_rigid_connectors.interference_fits import _1463


__docformat__ = "restructuredtext en"
__all__ = ("DetailedRigidConnectorDesign",)


Self = TypeVar("Self", bound="DetailedRigidConnectorDesign")


class DetailedRigidConnectorDesign(_0.APIBase):
    """DetailedRigidConnectorDesign

    This is a mastapy class.
    """

    TYPE = _DETAILED_RIGID_CONNECTOR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedRigidConnectorDesign")

    class _Cast_DetailedRigidConnectorDesign:
        """Special nested class for casting DetailedRigidConnectorDesign to subclasses."""

        def __init__(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
            parent: "DetailedRigidConnectorDesign",
        ):
            self._parent = parent

        @property
        def custom_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1408.CustomSplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1408

            return self._parent._cast(_1408.CustomSplineJointDesign)

        @property
        def din5480_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1411.DIN5480SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1411

            return self._parent._cast(_1411.DIN5480SplineJointDesign)

        @property
        def gbt3478_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1415.GBT3478SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1415

            return self._parent._cast(_1415.GBT3478SplineJointDesign)

        @property
        def iso4156_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1418.ISO4156SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1418

            return self._parent._cast(_1418.ISO4156SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1419.JISB1603SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1419

            return self._parent._cast(_1419.JISB1603SplineJointDesign)

        @property
        def sae_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1426.SAESplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1426

            return self._parent._cast(_1426.SAESplineJointDesign)

        @property
        def spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1433.SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1433

            return self._parent._cast(_1433.SplineJointDesign)

        @property
        def standard_spline_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1438.StandardSplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1438

            return self._parent._cast(_1438.StandardSplineJointDesign)

        @property
        def keyed_joint_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1455.KeyedJointDesign":
            from mastapy.detailed_rigid_connectors.keyed_joints import _1455

            return self._parent._cast(_1455.KeyedJointDesign)

        @property
        def interference_fit_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "_1463.InterferenceFitDesign":
            from mastapy.detailed_rigid_connectors.interference_fits import _1463

            return self._parent._cast(_1463.InterferenceFitDesign)

        @property
        def detailed_rigid_connector_design(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
        ) -> "DetailedRigidConnectorDesign":
            return self._parent

        def __getattr__(
            self: "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedRigidConnectorDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_spline_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDSplineDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def length_of_engagement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfEngagement

        if temp is None:
            return 0.0

        return temp

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
    def halves(self: Self) -> "List[_1406.DetailedRigidConnectorHalfDesign]":
        """List[mastapy.detailed_rigid_connectors.DetailedRigidConnectorHalfDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Halves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "DetailedRigidConnectorDesign._Cast_DetailedRigidConnectorDesign":
        return self._Cast_DetailedRigidConnectorDesign(self)
