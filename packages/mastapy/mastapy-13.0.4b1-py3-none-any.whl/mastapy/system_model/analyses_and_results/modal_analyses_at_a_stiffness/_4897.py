"""BoltedJointModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4978,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BoltedJointModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6852
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BoltedJointModalAnalysisAtAStiffness")


class BoltedJointModalAnalysisAtAStiffness(
    _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """BoltedJointModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointModalAnalysisAtAStiffness")

    class _Cast_BoltedJointModalAnalysisAtAStiffness:
        """Special nested class for casting BoltedJointModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
            parent: "BoltedJointModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
        ) -> "BoltedJointModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BoltedJointModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2463.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6852.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointModalAnalysisAtAStiffness._Cast_BoltedJointModalAnalysisAtAStiffness":
        return self._Cast_BoltedJointModalAnalysisAtAStiffness(self)
