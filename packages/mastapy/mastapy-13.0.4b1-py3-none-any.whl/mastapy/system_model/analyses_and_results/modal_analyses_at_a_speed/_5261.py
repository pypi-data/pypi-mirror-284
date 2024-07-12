"""VirtualComponentModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5213,
        _5214,
        _5225,
        _5226,
        _5260,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysisAtASpeed")


class VirtualComponentModalAnalysisAtASpeed(
    _5216.MountableComponentModalAnalysisAtASpeed
):
    """VirtualComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentModalAnalysisAtASpeed"
    )

    class _Cast_VirtualComponentModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
            parent: "VirtualComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5213.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5214.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5225.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5226.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.PowerLoadModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5260.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5260,
            )

            return self._parent._cast(_5260.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "VirtualComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "VirtualComponentModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed":
        return self._Cast_VirtualComponentModalAnalysisAtASpeed(self)
