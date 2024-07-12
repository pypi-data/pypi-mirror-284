"""CouplingHalfCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4632
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4772,
        _4777,
        _4791,
        _4831,
        _4837,
        _4841,
        _4853,
        _4863,
        _4864,
        _4865,
        _4868,
        _4869,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysis")


class CouplingHalfCompoundModalAnalysis(_4826.MountableComponentCompoundModalAnalysis):
    """CouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysis")

    class _Cast_CouplingHalfCompoundModalAnalysis:
        """Special nested class for casting CouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
            parent: "CouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4772.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4777.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4791.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.CVTPulleyCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4831.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(
                _4831.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4837.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.PulleyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4841.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.RollingRingCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4853.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.SpringDamperHalfCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4863.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4863,
            )

            return self._parent._cast(_4863.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4864.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4865.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4865,
            )

            return self._parent._cast(_4865.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4868.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4868,
            )

            return self._parent._cast(_4868.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4869.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4869,
            )

            return self._parent._cast(_4869.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "CouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4632.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "List[_4632.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis":
        return self._Cast_CouplingHalfCompoundModalAnalysis(self)
