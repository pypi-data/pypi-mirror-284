"""CouplingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4978,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4901,
        _4906,
        _4962,
        _4984,
        _4998,
        _4878,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingModalAnalysisAtAStiffness")


class CouplingModalAnalysisAtAStiffness(
    _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """CouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysisAtAStiffness")

    class _Cast_CouplingModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
            parent: "CouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4978.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4978.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4878.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4901.ClutchModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(_4901.ClutchModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4906.ConceptCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4962.PartToPartShearCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4984.SpringDamperModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.SpringDamperModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "_4998.TorqueConverterModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4998,
            )

            return self._parent._cast(_4998.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
        ) -> "CouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness":
        return self._Cast_CouplingModalAnalysisAtAStiffness(self)
