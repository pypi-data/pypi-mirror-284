"""AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5301,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5142,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5280,
        _5285,
        _5331,
        _5368,
        _5374,
        _5377,
        _5395,
        _5327,
        _5333,
        _5303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed(
    _5301.ConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5301.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5301.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5327.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(_5327.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(
                _5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5280.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5285.BevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5331.HypoidGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5374.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5377.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5395.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5395,
            )

            return self._parent._cast(
                _5395.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5142.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed(self)
