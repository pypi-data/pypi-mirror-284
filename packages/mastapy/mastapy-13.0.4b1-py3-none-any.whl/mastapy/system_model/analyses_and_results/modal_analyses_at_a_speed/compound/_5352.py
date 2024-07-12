"""PlanetaryGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5317,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5223,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5328,
        _5366,
        _5268,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundModalAnalysisAtASpeed")


class PlanetaryGearSetCompoundModalAnalysisAtASpeed(
    _5317.CylindricalGearSetCompoundModalAnalysisAtASpeed
):
    """PlanetaryGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
            parent: "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5317.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5317.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5328.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5268.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
        ) -> "PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "PlanetaryGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5223.PlanetaryGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PlanetaryGearSetModalAnalysisAtASpeed]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5223.PlanetaryGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PlanetaryGearSetModalAnalysisAtASpeed]

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
    ) -> "PlanetaryGearSetCompoundModalAnalysisAtASpeed._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_PlanetaryGearSetCompoundModalAnalysisAtASpeed(self)
