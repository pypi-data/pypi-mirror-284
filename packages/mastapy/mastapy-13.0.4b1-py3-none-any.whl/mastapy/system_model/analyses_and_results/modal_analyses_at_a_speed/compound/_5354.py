"""PointLoadCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5390,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PointLoadCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2491
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5225,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5345,
        _5293,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PointLoadCompoundModalAnalysisAtASpeed")


class PointLoadCompoundModalAnalysisAtASpeed(
    _5390.VirtualComponentCompoundModalAnalysisAtASpeed
):
    """PointLoadCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PointLoadCompoundModalAnalysisAtASpeed"
    )

    class _Cast_PointLoadCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PointLoadCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
            parent: "PointLoadCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5390.VirtualComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5390.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
        ) -> "PointLoadCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PointLoadCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2491.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5225.PointLoadModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PointLoadModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5225.PointLoadModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PointLoadModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PointLoadCompoundModalAnalysisAtASpeed._Cast_PointLoadCompoundModalAnalysisAtASpeed":
        return self._Cast_PointLoadCompoundModalAnalysisAtASpeed(self)
