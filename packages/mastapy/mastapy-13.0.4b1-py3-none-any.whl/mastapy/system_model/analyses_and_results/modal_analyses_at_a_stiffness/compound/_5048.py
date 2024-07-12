"""CouplingHalfCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4916,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5032,
        _5037,
        _5051,
        _5091,
        _5097,
        _5101,
        _5113,
        _5123,
        _5124,
        _5125,
        _5128,
        _5129,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtAStiffness")


class CouplingHalfCompoundModalAnalysisAtAStiffness(
    _5086.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """CouplingHalfCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingHalfCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
            parent: "CouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5086.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5037.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(_5051.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5091.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(_5097.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5101.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5123.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5123,
            )

            return self._parent._cast(
                _5123.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5124.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5124,
            )

            return self._parent._cast(
                _5124.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5125.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5125,
            )

            return self._parent._cast(
                _5125.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5128.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5128,
            )

            return self._parent._cast(
                _5128.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "_5129.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5129,
            )

            return self._parent._cast(
                _5129.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "CouplingHalfCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CouplingHalfCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4916.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4916.CouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingHalfModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundModalAnalysisAtAStiffness._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness":
        return self._Cast_CouplingHalfCompoundModalAnalysisAtAStiffness(self)
