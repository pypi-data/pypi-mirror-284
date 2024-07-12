"""DrawStyleBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE_BASE = python_net_import("SMT.MastaAPI.Geometry", "DrawStyleBase")

if TYPE_CHECKING:
    from mastapy.geometry import _310
    from mastapy.system_model.drawing import _2266, _2272
    from mastapy.system_model.analyses_and_results.system_deflections import _2847
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3111,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import _3892
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4047
    from mastapy.system_model.analyses_and_results.power_flows import _4100, _4144
    from mastapy.system_model.analyses_and_results.modal_analyses import _4677
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5481
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605


__docformat__ = "restructuredtext en"
__all__ = ("DrawStyleBase",)


Self = TypeVar("Self", bound="DrawStyleBase")


class DrawStyleBase(_0.APIBase):
    """DrawStyleBase

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DrawStyleBase")

    class _Cast_DrawStyleBase:
        """Special nested class for casting DrawStyleBase to subclasses."""

        def __init__(
            self: "DrawStyleBase._Cast_DrawStyleBase", parent: "DrawStyleBase"
        ):
            self._parent = parent

        @property
        def draw_style(self: "DrawStyleBase._Cast_DrawStyleBase") -> "_310.DrawStyle":
            from mastapy.geometry import _310

            return self._parent._cast(_310.DrawStyle)

        @property
        def contour_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2266.ContourDrawStyle":
            from mastapy.system_model.drawing import _2266

            return self._parent._cast(_2266.ContourDrawStyle)

        @property
        def model_view_options_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2272.ModelViewOptionsDrawStyle":
            from mastapy.system_model.drawing import _2272

            return self._parent._cast(_2272.ModelViewOptionsDrawStyle)

        @property
        def system_deflection_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2847.SystemDeflectionDrawStyle":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.SystemDeflectionDrawStyle)

        @property
        def steady_state_synchronous_response_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_3111.SteadyStateSynchronousResponseDrawStyle":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_3892.StabilityAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.StabilityAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4047.RotorDynamicsDrawStyle":
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4047

            return self._parent._cast(_4047.RotorDynamicsDrawStyle)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4100.CylindricalGearGeometricEntityDrawStyle":
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4144.PowerFlowDrawStyle":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.PowerFlowDrawStyle)

        @property
        def modal_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4677.ModalAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.ModalAnalysisDrawStyle)

        @property
        def mbd_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_5481.MBDAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(_5481.MBDAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_5783.HarmonicAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_6351.DynamicAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.DynamicAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_6605.CriticalSpeedAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.CriticalSpeedAnalysisDrawStyle)

        @property
        def draw_style_base(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "DrawStyleBase":
            return self._parent

        def __getattr__(self: "DrawStyleBase._Cast_DrawStyleBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DrawStyleBase.TYPE"):
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
    def cast_to(self: Self) -> "DrawStyleBase._Cast_DrawStyleBase":
        return self._Cast_DrawStyleBase(self)
