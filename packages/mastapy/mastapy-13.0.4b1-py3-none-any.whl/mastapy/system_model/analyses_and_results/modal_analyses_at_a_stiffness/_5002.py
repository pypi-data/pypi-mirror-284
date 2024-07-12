"""VirtualComponentModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4957,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "VirtualComponentModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4954,
        _4955,
        _4966,
        _4967,
        _5001,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysisAtAStiffness")


class VirtualComponentModalAnalysisAtAStiffness(
    _4957.MountableComponentModalAnalysisAtAStiffness
):
    """VirtualComponentModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentModalAnalysisAtAStiffness"
    )

    class _Cast_VirtualComponentModalAnalysisAtAStiffness:
        """Special nested class for casting VirtualComponentModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
            parent: "VirtualComponentModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4954.MassDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(_4954.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4955.MeasurementComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4966.PointLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(_4966.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_4967.PowerLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(_4967.PowerLoadModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "_5001.UnbalancedMassModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5001,
            )

            return self._parent._cast(_5001.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
        ) -> "VirtualComponentModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "VirtualComponentModalAnalysisAtAStiffness.TYPE"
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
    ) -> "VirtualComponentModalAnalysisAtAStiffness._Cast_VirtualComponentModalAnalysisAtAStiffness":
        return self._Cast_VirtualComponentModalAnalysisAtAStiffness(self)
