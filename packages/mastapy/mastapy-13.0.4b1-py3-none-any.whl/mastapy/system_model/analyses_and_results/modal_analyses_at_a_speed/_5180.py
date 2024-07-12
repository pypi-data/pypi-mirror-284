"""CVTPulleyModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5176,
        _5216,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTPulleyModalAnalysisAtASpeed")


class CVTPulleyModalAnalysisAtASpeed(_5227.PulleyModalAnalysisAtASpeed):
    """CVTPulleyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyModalAnalysisAtASpeed")

    class _Cast_CVTPulleyModalAnalysisAtASpeed:
        """Special nested class for casting CVTPulleyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
            parent: "CVTPulleyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_5227.PulleyModalAnalysisAtASpeed":
            return self._parent._cast(_5227.PulleyModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_5176.CouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
        ) -> "CVTPulleyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleyModalAnalysisAtASpeed._Cast_CVTPulleyModalAnalysisAtASpeed":
        return self._Cast_CVTPulleyModalAnalysisAtASpeed(self)
