"""SynchroniserHalfModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4995,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SynchroniserHalfModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4916,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserHalfModalAnalysisAtAStiffness")


class SynchroniserHalfModalAnalysisAtAStiffness(
    _4995.SynchroniserPartModalAnalysisAtAStiffness
):
    """SynchroniserHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserHalfModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserHalfModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
            parent: "SynchroniserHalfModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_4995.SynchroniserPartModalAnalysisAtAStiffness":
            return self._parent._cast(_4995.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_4916.CouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
        ) -> "SynchroniserHalfModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SynchroniserHalfModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2625.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6989.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfModalAnalysisAtAStiffness._Cast_SynchroniserHalfModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserHalfModalAnalysisAtAStiffness(self)
