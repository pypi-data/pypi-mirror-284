"""PartToPartShearCouplingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4917,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PartToPartShearCouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2609
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4978,
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PartToPartShearCouplingModalAnalysisAtAStiffness")


class PartToPartShearCouplingModalAnalysisAtAStiffness(
    _4917.CouplingModalAnalysisAtAStiffness
):
    """PartToPartShearCouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingModalAnalysisAtAStiffness"
    )

    class _Cast_PartToPartShearCouplingModalAnalysisAtAStiffness:
        """Special nested class for casting PartToPartShearCouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
            parent: "PartToPartShearCouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4917.CouplingModalAnalysisAtAStiffness":
            return self._parent._cast(_4917.CouplingModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "PartToPartShearCouplingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2609.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6953.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness":
        return self._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness(self)
