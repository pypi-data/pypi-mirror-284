"""SynchroniserPartModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4916,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SynchroniserPartModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4993,
        _4996,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserPartModalAnalysisAtAStiffness")


class SynchroniserPartModalAnalysisAtAStiffness(
    _4916.CouplingHalfModalAnalysisAtAStiffness
):
    """SynchroniserPartModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserPartModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserPartModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
            parent: "SynchroniserPartModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4916.CouplingHalfModalAnalysisAtAStiffness":
            return self._parent._cast(_4916.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4993.SynchroniserHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4993,
            )

            return self._parent._cast(_4993.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4996.SynchroniserSleeveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4996,
            )

            return self._parent._cast(_4996.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "SynchroniserPartModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SynchroniserPartModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserPartModalAnalysisAtAStiffness(self)
