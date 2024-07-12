"""PlanetCarrierModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetCarrierModalAnalysisAtASpeed")


class PlanetCarrierModalAnalysisAtASpeed(_5216.MountableComponentModalAnalysisAtASpeed):
    """PlanetCarrierModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierModalAnalysisAtASpeed")

    class _Cast_PlanetCarrierModalAnalysisAtASpeed:
        """Special nested class for casting PlanetCarrierModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
            parent: "PlanetCarrierModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
        ) -> "PlanetCarrierModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PlanetCarrierModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

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
    ) -> "PlanetCarrierModalAnalysisAtASpeed._Cast_PlanetCarrierModalAnalysisAtASpeed":
        return self._Cast_PlanetCarrierModalAnalysisAtASpeed(self)
