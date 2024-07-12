"""CVTModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4888,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4978,
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtAStiffness")


class CVTModalAnalysisAtAStiffness(_4888.BeltDriveModalAnalysisAtAStiffness):
    """CVTModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtAStiffness")

    class _Cast_CVTModalAnalysisAtAStiffness:
        """Special nested class for casting CVTModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            parent: "CVTModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4888.BeltDriveModalAnalysisAtAStiffness":
            return self._parent._cast(_4888.BeltDriveModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "CVTModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness":
        return self._Cast_CVTModalAnalysisAtAStiffness(self)
