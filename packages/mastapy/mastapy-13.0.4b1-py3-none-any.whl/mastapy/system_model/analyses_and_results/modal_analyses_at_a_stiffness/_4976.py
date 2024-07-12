"""ShaftModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4879,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ShaftModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2502
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4880,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ShaftModalAnalysisAtAStiffness")


class ShaftModalAnalysisAtAStiffness(_4879.AbstractShaftModalAnalysisAtAStiffness):
    """ShaftModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalAnalysisAtAStiffness")

    class _Cast_ShaftModalAnalysisAtAStiffness:
        """Special nested class for casting ShaftModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
            parent: "ShaftModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_4879.AbstractShaftModalAnalysisAtAStiffness":
            return self._parent._cast(_4879.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
        ) -> "ShaftModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2502.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6972.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftModalAnalysisAtAStiffness._Cast_ShaftModalAnalysisAtAStiffness":
        return self._Cast_ShaftModalAnalysisAtAStiffness(self)
