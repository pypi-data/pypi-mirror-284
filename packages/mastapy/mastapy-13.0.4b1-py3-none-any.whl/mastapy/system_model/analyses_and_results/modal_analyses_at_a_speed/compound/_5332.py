"""HypoidGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5274,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5202,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5330,
        _5331,
        _5302,
        _5328,
        _5366,
        _5268,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundModalAnalysisAtASpeed")


class HypoidGearSetCompoundModalAnalysisAtASpeed(
    _5274.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
):
    """HypoidGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_HypoidGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting HypoidGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
            parent: "HypoidGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5274.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5274.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5302.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5268.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
        ) -> "HypoidGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "HypoidGearSetCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2555.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2555.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5202.HypoidGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.HypoidGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5330.HypoidGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.HypoidGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5331.HypoidGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.HypoidGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5202.HypoidGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.HypoidGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCompoundModalAnalysisAtASpeed._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_HypoidGearSetCompoundModalAnalysisAtASpeed(self)
