"""ShaftHubConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4914,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ShaftHubConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2619
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ShaftHubConnectionModalAnalysisAtAStiffness")


class ShaftHubConnectionModalAnalysisAtAStiffness(
    _4914.ConnectorModalAnalysisAtAStiffness
):
    """ShaftHubConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_ShaftHubConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting ShaftHubConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
            parent: "ShaftHubConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4914.ConnectorModalAnalysisAtAStiffness":
            return self._parent._cast(_4914.ConnectorModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "ShaftHubConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2619.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftHubConnectionModalAnalysisAtAStiffness]

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
    ) -> "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness":
        return self._Cast_ShaftHubConnectionModalAnalysisAtAStiffness(self)
