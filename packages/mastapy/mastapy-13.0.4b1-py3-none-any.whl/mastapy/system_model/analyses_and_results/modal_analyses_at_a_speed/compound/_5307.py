"""CouplingHalfCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5345,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5176,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5291,
        _5296,
        _5310,
        _5350,
        _5356,
        _5360,
        _5372,
        _5382,
        _5383,
        _5384,
        _5387,
        _5388,
        _5293,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtASpeed")


class CouplingHalfCompoundModalAnalysisAtASpeed(
    _5345.MountableComponentCompoundModalAnalysisAtASpeed
):
    """CouplingHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CouplingHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
            parent: "CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5291.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5296.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5310.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5350.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5356.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5360.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(_5360.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5372.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(
                _5372.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5382.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5383.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5383,
            )

            return self._parent._cast(
                _5383.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5384.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5384,
            )

            return self._parent._cast(
                _5384.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5387.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5387,
            )

            return self._parent._cast(
                _5387.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5388.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5388,
            )

            return self._parent._cast(
                _5388.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5176.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5176.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_CouplingHalfCompoundModalAnalysisAtASpeed(self)
